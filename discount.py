from datetime import date, timedelta, datetime

today = date.today()
print(today)
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)
print(type(time))  # <class 'datetime.datetime'>

print(time.hour)
print(today.day)
print(today.month)
print(today.year)

formatted_date = datetime.now().strftime('%d/%m/%y')
print(formatted_date)

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)

formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # duze/male litery maja znaczenie
print(formatted_datetime)

formatted_datetime = datetime.now().strftime("%y-%m-%d %H:%M")  # duze/male litery maja znaczenie
print(formatted_datetime)

tomorrow = today + timedelta(days=1)
print(tomorrow)

yesterday = today + timedelta(days=-1)
print(yesterday)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 20.0},
    {'sku': 4, 'exp_date': today, 'price': 50.0},
]
print(products)

for product in products:
    print(product)
    if product['exp_date'] != today:
        continue # nie wykonuj kolejnych instrukcji z petli, idz na poczatek petli, wez kolejny element

    product['price'] *= 0.8
    print(f"""
    Price for sku = {product['sku']}' 
    is now {product['price']}""")