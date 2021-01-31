from uuid import uuid4
import datetime

default_uuid_value = lambda: str(uuid4())
default_tournament_id_value = 'dda2c34f-f992-4701-a76e-e02b12cbdf0e'
default_tournament_name_id_value = '4e1f7f4b-6f3e-43ce-954d-aa9cf6ca52e4'

default_year_value = 1700
default_month_value = 1
default_day_value = 1
default_date_value = datetime.datetime(default_year_value, default_month_value, default_day_value)