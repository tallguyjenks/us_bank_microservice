import pandas as pd
from loguru import logger as log
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine
from utils import get_username


class Database:
    def __initialize_database_connection(self) -> None:
        # FIXME Verify that this points to the correct database and on the correct server
        return create_engine(
            "mssql+pyodbc://@{}/{}?driver=ODBC Driver 17 for SQL Server".format(
                SERVER, DATABASE
            ),
            pool_recycle=3600,
            pool_pre_ping=True,
        )

    def query(self, query_string: str) -> any:
        with self.__initialize_database_connection().connect() as __conn:
            with __conn.begin():
                __result_set = __conn.execute(f"{query_string}")
                for __result in __result_set:
                    return __result[0]

    def pandas_query(self, query_string: str) -> DataFrame:
        try:
            return pd.read_sql_query(
                f"{query_string}",
                self.__initialize_database_connection(),
            )
        except Exception as e:
            log.error(e)
            exit()


class SQL_Log_Table(Database):
    def __init__(self) -> None:
        self.__execution_id = self.__get_execution_id()
        self.__username = get_username()

    def __get_execution_id(self) -> int:
        # TODO verify that log table below is correct
        return int(
            self.__format_pandas_dataframe_to_single_value(
                self.pandas_query(
                    "SELECT MAX(execution_id) + 1 FROM {{APP_NAME}}.app.log"
                )
            )
        )

    def __format_pandas_dataframe_to_single_value(self, value: DataFrame) -> any:
        return value.to_string(index=False, header=False, na_rep="").strip()

    def write(self, message) -> None:
        _msg = message.record
        _msg["message"] = str(_msg["message"]).replace("'", '"')
        # TODO verify that log table below is correct
        _log_string = f"""
        INSERT INTO {{APP_NAME}}.app.log (
            Execution_ID
            , Time_Stamp
            , Log_Level
            , Module
            , [Function]
            , Line_Number
            , Message
            , Username)
        Values (
            {self.__execution_id}
            , '{_msg['time'].strftime("%Y-%m-%d %H:%M:%S")}.{_msg['time'].strftime("%f")[0:3]}'
            , '{_msg['level'].name}'
            , '{_msg['name']}'
            , '{_msg['function']}'
            ,  {_msg['line']}
            , '{_msg['message']}'
            , '{self.__username}')"""
        try:
            with self.__initialize_database_connection().connect() as __conn:
                __conn.execute(_log_string)
        except Exception as e:
            log.error("Unable to write log to SQL Database Table. Unable to continue.")
            log.error(e)
            exit()
