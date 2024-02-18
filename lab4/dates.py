from datetime import datetime, timedelta
#1EX
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))
print()

#2EX
todayday=datetime.now()
yesterday=todayday-timedelta(days=1)
tomorrow=todayday+timedelta(days=1)
print("yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("Today: ", todayday.strftime("%Y-%m-%d"))
print("tomorrow: ", tomorrow.strftime("%Y-%m-%d"))
print()

#3EX
currentday=datetime.now()
withoutmicro=currentday.replace(microsecond=0)
print(withoutmicro)

#3EX

def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)
    return difference.total_seconds()

date_format = "%Y-%m-%d %H:%M:%S"

date_str1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

difference_seconds = date_difference_in_seconds(date1, date2)

print("Difference in seconds:", difference_seconds)

#or
def diff(d1, d2):
    date1 = datetime.strptime(d1, "%Y-%d-%m %H:%M:%S")
    date2 = datetime.strptime(d2, "%Y-%d-%m %H:%M:%S")

    res = abs(date2 - date1)

    ressec = res.total_seconds()
    return ressec

datestr1 = '2020-12-12 12:00:00'
datestr2 = '2020-12-12 11:00:00'
print(diff(datestr1, datestr2))


