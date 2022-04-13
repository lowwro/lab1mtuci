import requests
city="Krasnodar,RU"
key="97c6762340f15ffdawdwa273f836e991b0"
"""
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
data = res.json()
print (data)
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
    i['weather'][0]['description'], ">")
print("____________________________")
"""
#BEGIN Home_work
#Вывести текущие:
#скорость ветра,видимость
#Недельные скорость ветра,видимость

#День
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': key})
data = res.json()

#Неделя
res7 = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric','cnt':'7','lang': 'ru', 'APPID': key})
data7 = res7.json()
print("Город:", city)
print("Текущие:")
print("\tСкорость ветра:", data['wind']['speed'])
print("\tВидимость:", data['visibility'])
print("Недельные:")
day=1
for i in data7['list']:
        print("День:",day)
        print("Скорость ветра",i['wind']['speed'])
        print("Видимость:",i['visibility'])
        print ("\n")
        day+=1
