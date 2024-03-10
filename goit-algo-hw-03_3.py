from datetime import datetime, timedelta
users = [{"name": "Illya", "birthday": "2008.03.12"},{"name": "Vova", "birthday": "2012.03.9"},{"name": "Natalie", "birthday": "1979.12.18"}]
def find_next_weekday(d, weekday: int):  
    days_ahead = weekday - d.weekday()  
    if days_ahead <= 0:  
        days_ahead += 7  
    return d + timedelta(days=days_ahead)  

def get_upcoming_birthdays(users):
    prepared_users = [] 
    for user in users: 
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            prepared_users.append({"name": user['name'], 'birthday': birthday})  
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  

    days = 7  
    today = datetime.today().date()  

    upcoming_birthdays = []  
    for user in prepared_users:  
        birthday_this_year = user["birthday"].replace(year=today.year)  

        if birthday_this_year < today:  
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

        if 0 <= (birthday_this_year - today).days <= days:  
            if birthday_this_year.weekday() >= 5:  
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  
            upcoming_birthdays.append({  
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список іменинників на цьому тижні:", upcoming_birthdays)