import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=5b79508949bb7ef46f90124386e740eeq='
city = raw_input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']
print(format_add)