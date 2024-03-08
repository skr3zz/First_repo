from datetime import datetime
def get_days_from_today(date):
    days_from_today="2020-10-09"
    days_from_today=datetime.strptime(days_from_today,"%Y-%m-%d")
    today=datetime.now()
    difference=today-days_from_today
    return difference.days
print(get_days_from_today('date'))
