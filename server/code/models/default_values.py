from uuid import uuid4
import datetime

default_uuid_value = lambda: str(uuid4())

default_year_value = 1700
default_month_value = 1
default_day_value = 1
default_date_value = datetime.datetime(default_year_value, default_month_value, default_day_value)