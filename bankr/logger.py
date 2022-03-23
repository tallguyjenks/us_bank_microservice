# import os

from loguru import logger as log


class Logger:
    """This class is the representation of all app logging via Loguru"""

    def __init__(self) -> None:
        ...

    def load_config(self):
        log.level("TRACE", color="<white>")
        log.level("DEBUG", color="<light-blue>")
        log.level("INFO", color="<light-white>")
        log.level("SUCCESS", color="<light-green>")
        log.level("WARNING", color="<light-yellow>")
        log.level("ERROR", color="<light-red>")
        log.level("CRITICAL", color="<bold><light-yellow><LIGHT-RED>")

        log.success("Logger initialized, tracking app events")
        # self._find_local_log_file()
        # self._initialize_local_log_file_connection()
        # self._initialize_sql_log_table_connection()

    # def _get_appdata_path(self) -> str:
    #     return f"{os.getenv('LOCALAPPDATA')}\\{{APP_NAME}}"

    # def _get_log_file(self) -> str:
    #     return f"{self._get_appdata_path()}\\app.log"

    # def _find_local_log_file(self) -> None:
    #     """This function will find the existing local log file or create it if it doesn't exist"""

    #     def make_directory(path: str) -> None:
    #         if not os.path.isdir(path):
    #             os.mkdir(path)

    #     def check_log_file(path: str) -> None:
    #         log.debug(f"Checking for log file at: {path}")
    #         with open(path, "r"):
    #             log.success("Log file found!")

    #     def make_log_file(path: str) -> None:
    #         try:
    #             with open(path, "w"):
    #                 log.success(f"Log File Created Successfully at {path}")
    #         except Exception as exception:
    #             log.error(f"Problem with {__name__}, {exception = }")
    #             log.critical(
    #                 "Unable to Create Local Log, Contact someone for assistance, Exiting..."
    #             )
    #             exit()

    #     try:
    #         log.success("SPINNING UP PROGRAM")
    #         check_log_file(self._get_log_file())
    #     except FileNotFoundError:
    #         log.error("Local Log File Not Found Attempting to Create...")
    #         make_directory(self._get_appdata_path())
    #         make_log_file(self._get_log_file())

    # def _initialize_local_log_file_connection(self) -> None:
    #     """This function will establish the loguru sink to the local log file so output is recorded somewhere and not just transient in the terminal"""
    #     log.info("Initializing log file...")
    #     log.add(
    #         self._get_log_file(),
    #         backtrace=True,
    #         diagnose=True,
    #         level="DEBUG",
    #     )
    #     log.level("TRACE", color="<white>")
    #     log.level("DEBUG", color="<light-blue>")
    #     log.level("INFO", color="<light-white>")
    #     log.level("SUCCESS", color="<light-green>")
    #     log.level("WARNING", color="<light-yellow>")
    #     log.level("ERROR", color="<light-red>")
    #     log.level("CRITICAL", color="<bold><light-yellow><LIGHT-RED>")

    #     log.success("Logger initialized, tracking app events")

    # def _initialize_sql_log_table_connection(self) -> None:
    #     """Utilize the SQL_Log_Table class to create a new Loguru sink and send output to the {{APP_NAME}} Database"""
    #     log.add(SQL_Log_Table(), level="DEBUG")

    # def turn_off_log_cli_output(self) -> None:
    #     """This will terminate the transient Loguru output to the terminal so that it does not interfere with terminal output"""
    #     log.remove(0)
