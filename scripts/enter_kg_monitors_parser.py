import requests
import csv

from bs4 import BeautifulSoup

urls = [
    'https://enter.kg/monitory_bishkek',
    'https://enter.kg/monitory_bishkek/results,101-100'
]

monitors = []
prices = []

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    monitor_text = soup.find_all('span', 'prouct_name')
    prices_text = soup.find_all('span', 'price')

    for i, (monitor, price) in enumerate(zip(monitor_text, prices_text)):
        monitors.append(monitor.text)
        prices.append(price.text)

monitor_prices = dict(zip(monitors, prices))

with open('../monitors.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in monitor_prices.items():
        writer.writerow([str(key), str(value)])
