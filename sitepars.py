import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent
import time

url = 'https://kups.club/'
# user = fake_useragent.UserAgent().random
# print(user)
user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

headers = {'user-agent': user}
session = requests.Session()
# print(headers)

response = requests.get(url, headers=headers)
time.sleep(2)
soup = BeautifulSoup(response.text, 'lxml')
time.sleep(2)

all_product = soup.find('div', class_="row mt-4")
# print(all_product)
product_list = all_product.find_all('div', class_='card h-100')
# print(product_list)
for i in range(len(product_list)):
    product = product_list[i].find('h3', class_='card-title').text
    price = product_list[i].find('p', class_='card-text').text
    try:
        shop = product_list[i].find('a', class_='text-black link-default').text
        with open('my_product.txt', 'a', encoding='UTF-8') as file:
            file.write(f"{product}    Price {price}    Shop{shop}'\n'")
    except AttributeError:
        print('No shop')

