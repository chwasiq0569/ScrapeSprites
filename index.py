import matplotlib.pyplot as plt
import matplotlib.image as mpim
from bs4 import BeautifulSoup
import requests


# inputTag = soup.findAll(attrs={"class" : "img-fixed", "class": "icon-pkmn"})
# # output = inputTag['data_src']

# print(inputTag[i].attrs["data-src"])

# for i in range(len(inputTag)):
# print(inputTag[0].attrs["data-src"])
# img = mpim.imread(inputTag[0].attrs["data-src"])
# imgplot = plt.imshow(img)
# plt.show()

# # len(inputTag)

# len(inputTag)




html_page = requests.get('https://pokemondb.net/sprites')

soup = BeautifulSoup(html_page.content, 'html.parser')

warning = soup.find_all('span', class_="img-fixed")
# data-src
# print(warning)

# print(soup.find('span', class_="img-fixed").data_src)

inputTag = soup.findAll(attrs={"class" : "img-fixed", "class": "icon-pkmn"})
# # output = inputTag['data_src']


# for i in range(len(inputTag)):
#   print(inputTag[i].attrs["data-src"])

# image_count = 1
# for i in range(len(inputTag)):
#   print(inputTag[i].attrs["data-src"])
#   with open('image_'+str(image_count)+'.png', 'wb') as f:
#        f.write(inputTag[i].attrs["data-src"])
#   
# import requests

image_count = 1  
for image in inputTag:
    print(image.attrs['data-src'])
    with open('./images/image_'+str(image_count)+'.png', 'wb') as f:
       f.write(requests.get(image.attrs['data-src']).content)
    image_count = image_count+1    
