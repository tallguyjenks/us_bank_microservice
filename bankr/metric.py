import time

from ticketer.db import Metric_Table


class Metric:
    def start_timer(self) -> int:
        self.start_time = time.time()

    def end_timer(self) -> int:
        self.end_time = time.time()

    def record_metric(self, ticket_id: str) -> None:
        metric_table = Metric_Table()
        metric_table.get_ticket_id(ticket_id)
        metric_table.record_metrics_into_database(
            self._ticket_processing_duration(self.start_time, self.end_time)
        )

    def _ticket_processing_duration(self, start_time: float, end_time: float) -> int:
        """Return the time of a function in seconds."""
        return round(end_time - start_time)
