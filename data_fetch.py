import requests

# 25544 is ISS
URL = 'https://db.satnogs.org/api/telemetry/?satellite=25544'
result = requests.get(URL, headers={ 'Authorization': 'Token 725e35eb8798a9153b1d393881081a0de2b52935'})
print(result.json())


