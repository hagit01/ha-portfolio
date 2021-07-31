import requests

r = requests.get("https://api.ncovvn.xyz/city/")

data = r.json()[0]
text = f'Dia diem: {data["dia_diem]}'
while True:
    