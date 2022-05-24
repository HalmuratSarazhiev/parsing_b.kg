import requests
import csv
from bs4 import BeautifulSoup

url = "https://bimed.kg/"
CSV = "lekarstvenye_sredstva.cvs"

def get_html(url):
    req = requests.get(url)
    return req

html = get_html(url).text

# print(get_html(URL)) #cheking response

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('li', class_ = "product")
    # print(items) #cheking items
    with open('lekarstva.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Название', "Цена", "Наличие", "Изображение"])
        writer.writeheader()
    for item in items:
        try:
            title = item.find('h2', class_ = 'woocommerce-loop-product__title').text.strip()
        except:
            title = 'Title not Found'
        try:
            price = item.find('span', class_ = "woocommerce-Price-amount amount").text.strip().replace(" ", '').replace("\n", " ")
        except:
            price = "Price not Found"
        try:
            image = item.find('div', class_= "thumb-wrap").find('img').get('src')
        except:
            image = 'Image not Found'
        try:
            stock = item.find('span', class_ ="in-stock").text.strip()
        except:
            stock = "Нет в наличии"

        data = {
                    'Название': title,
                    'Цена': price,
                    'Наличие': stock,
                    'Изображение': image
                }
        # print(data) #cheking data
        save_info(data)

def save_info(data):
    with open('lekarstva.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Название', "Цена", "Наличие", "Изображение"])
        writer.writerow(data)

def main():
    for page in range(1, 125):
        print(f'Parsing {page} page')
        url = f"https://bimed.kg/product-category/lekarstvennye-sredstva/page/{page}"
        html = get_html(url).text
        get_content(html)
        page += 1
main()