from datetime import datetime, timedelta

#1
def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    print("Current date:", current_date.date())
    print("Date after subtracting 5 days:", new_date.date())

subtract_five_days()


#2
def print_dates():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)

print_dates()


#3
def drop_microseconds():
    now = datetime.now()
    new_time = now.replace(microsecond=0)
    
    print("Original datetime:", now)
    print("Without microseconds:", new_time)

drop_microseconds()



#4
def date_difference():
    date1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
    date2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

    date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

    diff_seconds = abs((date2 - date1).total_seconds())

    print("Difference in seconds:", diff_seconds)

date_difference()

