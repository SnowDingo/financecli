import requests

# when using we need to append the currency code
url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/'

def fetchCurrentExchangeRate(old, newcurrency):
    urltemp = url + old+ ".json"
    response = requests.get(urltemp)
    # res is response in json
    if response.status_code == 200:
        res = response.json()
        return res.get(old).get(newcurrency)
    else:
        print("**DATA FETCH FAILED!!**")
        return