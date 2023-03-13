import time
import requests  # бібліотека для роботи
res_monobank = requests.get('https://api.monobank.ua/bank/currency')
#for obj in res_monobank.json():
    #print(f'Object is {obj}, \nType is {type(obj)}', end='\n\n')
my_currencies = {
    980: 'EUR',
    840: 'USD',
    978: "EUR",
    # 826: '🇬🇧',
}

my_rates = []
for obj in res_monobank.json():
    #print(obj.keys())
    if obj['currencyCodeA'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)

print(my_rates)
for obj in my_rates:
    print(f"Країна: {my_currencies[obj['currencyCodeA']]}"
          f"\tКупівля {obj['rateBuy']} Продаж: {obj['rateSell']}")
time.sleep(15)
