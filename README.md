# Schedule2Calendar

Sometimes I want to subscribe the new season schedules of my favourite sports teams.
However, I'm not addicted to any social media.
Therefore I decide to use the traditional way -- add the schedules to my Mac Calendar.

This is a scripting tool to transfer events from html sources to iCalendar files (or directly add to Mac Calendar). 

## Prerequisites

First, of course, you need to have `Python`...

Here are all the required modules:

- `requests`
  + [requests](https://pypi.org/project/requests/) for downloading web sources; not required if directly provide html file;
- `urllib`
  + [urllib3](https://pypi.org/project/urllib3/) same as `requests`
- `icalendar`
  + [icalendar](https://pypi.org/project/icalendar/) for operating calendar events and writing iCal files
- `Beautiful Soup`
  + [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup) for parsing html
- `pytz`
  + [pytz](https://pypi.org/project/pytz/) for managing timezone

## Usage

### Quick Start

Run by:

```
$ python main.py ${html_filepath/website_link}
```

An example is (actually, currently only supports dodgers 2025 schedule):

```
$ python main.py testcases/dodgers_2025_schedule/dodgers_2025_schedule.htm
```

### Customize

TBD

## TODO

1. provide config file to manage options for this tool
2. better html lexer to abstract the schedule events (easy to support more team schedules)
3. maybe apply llm to find the pattern of sports team schedule (now observed by myself)
4. better way to get complete website sources 
...

## Misc
