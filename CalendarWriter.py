import os
import datetime
from icalendar import Calendar, Event

def writeICSFile(outfile, event_list):
    calendar = Calendar()
    for event in event_list:
        event_ical = Event()
        event_ical.summary = event[1]
        event_ical.begin = event[2]
        event_ical.end = event[2] + datetime.timedelta(hours=event[3])
        calendar.events.append(event_ical)

    with open(outfile, 'w') as f:
        f.write(calendar.serialize())

    return

def writeCalendar(event_list):
    for event in event_list:
        calendarname = event[0]
        eventtitle = event[1].replace(' ', '_')
        year = event[2].year
        month = event[2].month
        day = event[2].day
        hours = event[2].hour
        minutes = event[2].minute
        lasthours = event[3]
        print("[EXEC] osascript calendar_event_adder.scpt %s %s %d %d %d %d %d %d" % (calendarname, eventtitle, year, month, day, hours, minutes, lasthours))
        os.system("osascript calendar_event_adder.scpt %s %s %d %d %d %d %d %d" % (calendarname, eventtitle, year, month, day, hours, minutes, lasthours))
    return
