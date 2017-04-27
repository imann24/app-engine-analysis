import requests

for n in range(20):
    print(requests.get("https://electric-nomad-165723.appspot.com/").elapsed.total_seconds())
