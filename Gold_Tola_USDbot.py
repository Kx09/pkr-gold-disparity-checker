import requests

# Your API keys (replace with yours)
METAL_API_KEY = 'YOUR_API_KEY_HERE'
EXCHANGE_API_KEY = 'YOUR_API_KEY_HERE'


"""

Uses metal api and exchange rate API keys to get data
https://www.exchangerate-api.com/
https://www.metalpriceapi.com/
"""


def get_gold_price_usd_per_ounce():
    url = f'https://api.metalpriceapi.com/v1/latest?api_key={METAL_API_KEY}&base=USD&currencies=EUR,XAU,XAG'
    response = requests.get(url)
    data = response.json()
    print(f"the data returned from metalprice was{data}")
    return data['rates']['USDXAU']

def get_usd_to_pkr():
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/USD/PKR'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rate']

def convert_to_pkr_per_tola(gold_usd_per_oz, usd_to_pkr):
    grams_per_ounce = 31.1035
    grams_per_tola = 11.664
    gold_usd_per_gram = gold_usd_per_oz / grams_per_ounce
    gold_usd_per_tola = gold_usd_per_gram * grams_per_tola
    gold_pkr_per_tola = gold_usd_per_tola * usd_to_pkr
    return round(gold_pkr_per_tola, 2)

if __name__ == "__main__":
    gold_usd_per_oz = get_gold_price_usd_per_ounce()
    usd_to_pkr = get_usd_to_pkr()
    gold_pkr_per_tola = convert_to_pkr_per_tola(gold_usd_per_oz, usd_to_pkr)

    print(f"Live Gold Price (USD/oz): {gold_usd_per_oz}")
    print(f"USD to PKR Rate: {usd_to_pkr}")
    print(f"Fair Gold Price in PKR per Tola: Rs. {gold_pkr_per_tola}")
