from datetime import datetime, date

def get_days_from_today(date_str):

    date_format = '%Y-%m-%d'
    given_date = datetime.strptime(date_str, date_format).date()
    today = date.today()
    
    days_difference = (given_date - today).days
    
    return days_difference
print (get_days_from_today("2021-10-09"))