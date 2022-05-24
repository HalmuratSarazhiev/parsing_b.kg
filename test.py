import requests
from bs4 import BeautifulSoup


r = requests.get('https://bimed.kg/product-category/lekarstvennye-sredstva/').text

soup = BeautifulSoup(r, 'lxml')

# b = soup.find_all('li', class_='product')
# list_ = []
# for i in b:
#     title = soup.find('h2', class_='woocommerce-loop-product__title').text
#     list_.append(title)

# print(list_)

b = soup.find('main')
a = soup.find('li', class_='product').find('img', class_='attachment-woocommerce_thumbnail').get('src')
image = requests.get(a).content
with open(f'hfhfhfhf{}.jpg', 'wb') as img:
    img.write(image)

# print(image)

