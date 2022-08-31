import datetime

def fix_date(dt):
    if dt.year > 2010:
        year = dt.year - 100
    else:
        year = dt.year
    return datetime.datetime(year,dt.month,dt.day,dt.hour,dt.minute,dt.second)