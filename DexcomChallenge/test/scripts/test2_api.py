import sys
sys.path.append(sys.path[0] + "/...")
import requests

# the session will be released after use
with requests.Session() as session:
    session.auth = ('codechallenge','Password123')
    response = session.get('https://clarity.dexcom.com')

# You can inspect the response
print(response.headers)

