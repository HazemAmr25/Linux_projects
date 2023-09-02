#Lec_2   task3
#Write a code to Get your public IP and information of location 


import requests
response = requests.get('https://api.ipify.org/?format=json')
data =response.json()
Location_info = requests.get('https://ipinfo.io/{}/geo'.format(data['ip']))
data =Location_info.json()
print(data)