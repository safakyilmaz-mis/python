import time
import smtplib
import requests
from datetime import datetime

MY_LAT =  # Your latitude
MY_LONG =   # Your longitude
text = "hey look up iss is going over from your city!"
neg_text = "nope iss is even not close to your city"
email = "safakyilmaz.g@gmail.com"
password = "fcwdwmbeckdnfnfu"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_h = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_h = data["results"]["sunset"].split("T")[1].split(":")[0]

sunrise_m = data["results"]["sunrise"].split("T")[1].split(":")[1]
sunset_m = data["results"]["sunset"].split("T")[1].split(":")[1]

time_now = datetime.now()

while True:
    if time_now.hour < int(sunrise_h) and time_now.minute < sunrise_m or time_now.hour > int(
            sunset_h) and time_now.minute > sunset_m:
        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(from_addr=email,
                                    to_addrs="safak.yilmaz@atos.net",
                                    msg=f"subject:ISS is on your city. Look up!\n\n{text}")
        else:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(from_addr=email,
                                    to_addrs="safak.yilmaz@atos.net",
                                    msg=f"subject:ISS is far away from your city\n\n{neg_text}")
    else:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(from_addr=email,
                                to_addrs="safak.yilmaz@atos.net",
                                msg=f"subject:Daytime Error\n\n{"you are in daytime you cant see ISS now!"}")
    time.sleep(60)
