#Lec_2   task2
#Write a code to suggest automatically activates for you 

import requests
response = requests.get('https://www.boredapi.com/api/activity')
data =response.json()
print(data['activity'])