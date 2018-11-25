import json
from pprint import pprint
import qrcode
from bs4 import BeautifulSoup

with open("input/e27.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

data = []

for item in soup.find_all('li', class_='catalog__item'):
    print('-------------------------------------')

    name = item.find('p', class_='catalog__name')
    if not name: continue
    name = name.a.string.strip()

    articul = item['data-art']

    price = item.find('p', class_='catalog__price')
    price = price.contents[0] + price.contents[1].text

    link = item.find('a', href=True)['href']

    image = item.find('img')['src']

    data.append({
        'name': name,
        'articul': articul,
        'price': price,
        'link': link,
        'image': image,
    })

    # QR code maker
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(articul)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr/{articul}.png", "PNG")

    # img = qrcode.make(articul)


print('*************************************************')
pprint(data)
print(len(data))

with open('data.json', 'w') as fp:
    json.dump(data, fp, ensure_ascii=False)
