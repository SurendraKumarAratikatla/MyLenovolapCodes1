import datetime
from datetime import timedelta,date

sat_days = []
list_dates = []

def daterange(start_date_from, end_date_to):
    for n in range(int((end_date_to - start_date_from).days) + 1):
        yield start_date_from + timedelta(n)

def datefilter(sat_days):
    for dt in sat_days:
        year = dt.strftime("%Y-%m-%d")[:4]
        month = dt.strftime("%Y-%m-%d")[5:7]
        day = dt.strftime("%Y-%m-%d")[8:]
        # filtering 4th saturday
        if int(day) >= 21:
            if int(day)%5 != 0:
                dy = date(int(year), int(month), 1)
                first_week = dy.isoweekday()
                if first_week == 7:
                    saturday4 = 28
                else:
                    saturday4 = 28 - first_week
                if str(date(int(year), int(month), int(saturday4))) not in list_dates:
                    list_dates.append(str(date(int(year), int(month), int(saturday4))))
        # filtering saturday divisible by 5
        elif int(day)%5 == 0:
            if int(day) <= 21:
                if dt.strftime("%Y-%m-%d") not in list_dates:
                    list_dates.append(dt.strftime("%Y-%m-%d"))


def intervalDates(start_date,end_date):
    # start date
    start_date_obj = datetime.datetime.strptime(start_date, '%Y%m%d')
    start_date_from = start_date_obj.date()
    # end date
    end_date_obj = datetime.datetime.strptime(end_date, '%Y%m%d')
    end_date_to = end_date_obj.date()
    # looping from start date to end date
    for dt in daterange(start_date_from, end_date_to):
        # filtering all saturdays and storing into list
        if dt.strftime("%A") == "Saturday":
            sat_days.append(dt)
    datefilter(sat_days)
    # changing date YYYY-MM-DD to YYYYMMDD as requested output
    for date in list_dates:
        split_str = str(date).split('-')
        print(''.join(split_str),end ='\n')

# input
start_date = input("Start date:")
end_date = input("End date:")

# validations
if len(start_date) == 8 and start_date.isnumeric() and 1900 <= int(start_date[:4]) <= 2100 and len(end_date) == 8 and end_date.isnumeric() and 1900 <= int(end_date[:4]) <= 2100:
    intervalDates(start_date,end_date)
    pass
else:
    print("please enter valid dates, Example:20180728 (YYYYMMDD)")



