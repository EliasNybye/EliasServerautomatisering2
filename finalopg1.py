import requests             
url = "http://20.91.198.208:8081"
params = {"token": "ff886162"}
response = requests.get(url, params=params)
print(response.text)
print(response.headers) 
print(response.content) 

