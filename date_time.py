import datetime

current_utc_datetime = datetime.datetime.now()
current_datetime = datetime.datetime.utcnow()

print(current_utc_datetime)
print(current_datetime)

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()

print(current_date)
print(current_time)

current_utc_date = datetime.datetime.utcnow().date()
current_utc_time = datetime.datetime.utcnow().time()

print(current_utc_date)
print(current_utc_time)
