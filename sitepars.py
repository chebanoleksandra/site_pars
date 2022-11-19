import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = 'https://kups.club/'
user = fake_useragent.UserAgent().random

headers = {'user-agent': user}
session = requests.Session()
print(headers)

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

all_product = soup.find('div', class_="row mt-4")
product_list = all_product.find_all('div', class_='product-card')
for i in range(len(product_list)):
    product = product_list[i].find('h3', class_='card-title').text
    price = product_list[i].find('p', class_='card-text').text
    shop = product_list[i].find('a', class_='text-black link-default').text
    with open('my_product.txt', 'a', encoding='UTF-8') as file:
        file.write(f"{product}    Price {price}    Shop{shop}'\n'")
    # price = product_list[i].find('span', class_='sum').text
