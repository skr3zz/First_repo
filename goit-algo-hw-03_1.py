from datetime import datetime
def get_days_from_today(date):
    days_from_today=datetime.strptime(date,"%Y-%m-%d")
    today=datetime.now()
    difference=today-days_from_today
    return difference.days
print(get_days_from_today('2017-05-12'))
