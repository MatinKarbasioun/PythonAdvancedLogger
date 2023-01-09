from typing import Optional
import pytz


class TimeFormatter:
    def __init__(self, date_fmt: Optional[str] = "%Y-%m-%d", tz: Optional[pytz.BaseTzInfo] = pytz.UTC): 
        self.__tz = ...
        self.__dt_fmt = ...

    def get(self): ...
    def convert(self, time: float): ...
