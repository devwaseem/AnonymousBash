#!/bin/env python3
import requests,sys
print("Fetching your geolocation from your ip address...",end='\r')
data = requests.get("https://ip.zxq.co/self").json()
ip = data['ip']
city = data['city']
region = data['region']
country = data['country_full']
print(" "*50,end='\r')
print("IP\t: "+ip)
print("city\t: "+city)
print("region\t: "+region)
print("country\t: "+country)
