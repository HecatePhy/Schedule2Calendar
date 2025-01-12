import datetime
import pytz

month_brief2num = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

def transfer2localtime(timezone, year, month, date, hours, minutes, is24):
    additional_mapping = {'PDT': 'America/Los_Angeles', 'PST': 'America/Los_Angeles', 'PDT/PST': 'America/Los_Angeles', 'CST': 'ETC/GMT-8'}
    timezone_std = None
    timezone_lcl = None
    if timezone in additional_mapping.keys():
        timezone_std = pytz.timezone(additional_mapping[timezone])
    else:
        timezone_std = pytz.timezone(timezone)
    timezone2 = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    if timezone2 in additional_mapping.keys():
        timezone_lcl = pytz.timezone(additional_mapping[timezone2])
    else:
        timezone_lcl = pytz.timezone(timezone2)
    if is24 == 0 or is24 == 1 or hours == 12:
        pass
    elif is24 == 2:
        hours += 12
    time_input = datetime.datetime(year, month, date, hours, minutes)
    time_prev = timezone_std.localize(time_input)
    time_local = time_prev.astimezone(timezone_lcl)
    return time_local
