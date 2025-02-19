from datetime import datetime, date

def get_days_from_today(date_str):

    date_format = "%Y-%m-%d"
    try:
        given_date = datetime.strptime(date_str, date_format).date()
        today = date.today()
        return (given_date - today).days
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return None 
    
print (get_days_from_today("2025-05-10"))