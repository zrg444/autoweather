import requests
import json
from datetime import datetime
from twilio.rest import Client

account_sid = ("AC761e2aad0c2959eee6fb7b9988155456")
auth_token = ('20856f1ea8454f4a60821a97f6f9dc7f')
client = Client(account_sid, auth_token)

today = datetime.today().strftime("%Y-%m-%d")
day = datetime.today().strftime("%B, %d")

api_key = "1fd0613b9e714ebeac032374c5c4e2a2"
base_url = "http://api.weatherbit.io/v2.0/forecast/daily?"
city_name = "York,PA,USA"
url = base_url+"city="+city_name+"&units=I"+"&key="+api_key

response = requests.get(url)
data = response.json()
y = data['data'][1]

date = today
high_temp = y['high_temp']
low_temp = y['low_temp']
precip_chance = y['precip']
wind_dir = y['wind_cdir']
wind_speed = y['wind_spd']
sunrise = y['sunrise_ts']
sunset = y['sunset_ts']

hightemp_str = str(int(high_temp).__round__(0))
lowtemp_str = str(int(low_temp).__round__(0))
precipchance_str = str(int(precip_chance).__round__(0))
windspeed_str = str(int(wind_speed).__round__(0))
sunrise_time = datetime.fromtimestamp(sunrise).strftime("%H:%M")
sunset_time = datetime.fromtimestamp(sunset).strftime("%H:%M")

weather_message = """
                Good morning Zach! Today is {} and the high is {}. The low is {} and there is a {} percent chance of rain. The wind is blowing {} at {} MPH. The sun will rise at {} and set at {}.
                Have a great day!
                """.format(day,hightemp_str,lowtemp_str,precipchance_str,
                        wind_dir,windspeed_str,sunrise_time,sunset_time)

message = client.messages .create(
    body = (weather_message),
    from_ = "+14125577235",
    to = "+14126895814")
print(message.sid)

print("\nText sent!\n")