
#? ----------------------- Chapter 5: Date and Time ---------------------?#

#? ----------- Section 5.2: Constructing timezone-aware datetimes -------?#

import calendar
from dateutil.tz import tzlocal
from datetime import datetime
from datetime import date
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))

dt = datetime(2021, 4, 27, 12, 0, 0, tzinfo=JST)

# print(dt) #todo: 2021-04-27 12:00:00+09:00
# print(dt.tzname()) #todo: UTC+09:00
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
# print(dt.tzname) #todo: 'JST'

now = datetime.now()
then = datetime(2016, 5, 23)
delta = now - then
# print(delta)


def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

# print(get_n_days_after_date())


def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m:
        m = 12
    d = min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d, month=m, year=y)


# print(datetime.now(tzlocal()).replace(microsecond=0).isoformat())
