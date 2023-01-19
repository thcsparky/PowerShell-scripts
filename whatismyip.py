import requests

IP = requests.get('https://api.ipify.org/').text
print(f'Your IP is: {IP}')