import requests
import re
from bs4 import BeautifulSoup

def get_soup1(URL1):
    page = requests.get(URL1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
def get_soup2(URL2):
    page = requests.get(URL2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
def get_soup3(URL3):
    page = requests.get(URL3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
def get_soup4(URL4):
    page = requests.get(URL4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
def get_soup5(URL5):
    page = requests.get(URL5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
def get_soup6(URL6):
    page = requests.get(URL6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
def get_soup7(URL7):
    page = requests.get(URL7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
def get_soup8(URL8):
    page = requests.get(URL8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup8))
    return soup8
def get_soup9(URL9):
    page = requests.get(URL9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup9))
    return soup9
def get_soup10(URL10):
    page = requests.get(URL10)
    soup10 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup10))
    return soup10
def get_soup11(URL11):
    page = requests.get(URL11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup11))
    return soup11
def get_soup12(URL12):
    page = requests.get(URL12)
    soup12 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup12))
    return soup12
def get_soup13(URL13):
    page = requests.get(URL13)
    soup13 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup13))
    return soup13
def get_soup14(URL14):
    page = requests.get(URL14)
    soup14 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup14))
    return soup14
def get_soup15(URL15):
    page = requests.get(URL15)
    soup15 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup15))
    return soup15
def get_soup16(URL16):
    page = requests.get(URL16)
    soup16 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup16))
    return soup16
def get_soup17(URL17):
    page = requests.get(URL17)
    soup17 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup17))
    return soup17
def get_soup18(URL18):
    page = requests.get(URL18)
    soup18 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup18))
    return soup18
def get_soup19(URL19):
    page = requests.get(URL19)
    soup19 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup19))
    return soup19
def get_soup20(URL20):
    page = requests.get(URL20)
    soup20 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup20))
    return soup20

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_160/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/e8302de419760afe712b955d73c6bb6c.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/ce5fc4308ce969b6027f76b57ade0bef.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/dd68fee102d6036a8f33865ba4ac6a27.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/12f343938f2e7afee46a4ed697d1205e.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/da07769414600200e71f5484d7b08955.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/4838f4a03f6b1c25029d6c9f2be0ced8.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/545c599022465f100fa6c4b07e86f7fd.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast10(soup10):
    subjects = []
    for content in soup10.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d1bm3dmew779uf.cloudfront.net/rss/show/3565559/b4e6d9eecd3e2dcc593e68a7f23bee39.png"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast10(playable_podcast10):
    items = []
    for podcast in playable_podcast10:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/663025a4830225a11003be8e5ca26472.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast12(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/5635760f79316c76d075acd8fa8c16c1.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast13(soup13):
    subjects = []
    for content in soup13.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/3fac61f086b756e4006a6bcfd8d4b080.jpg"
        }
        subjects.append(item) 
    return subjectS
def compile_playable_podcast13(playable_podcast13):
    items = []
    for podcast in playable_podcast13:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast14(soup14):
    subjects = []
    for content in soup14.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/07a0b0661992b09682c2b5fbbd084fdf.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast14(playable_podcast14):
    items = []
    for podcast in playable_podcast14:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast15(soup15):
    subjects = []
    for content in soup15.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/0b241278f2a560c142ae0c483de2ea4e.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast15(playable_podcast15):
    items = []
    for podcast in playable_podcast15:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast16(soup16):
    subjects = []
    for content in soup16.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/2515908d77dd073b381269c71ef92135.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast16(playable_podcast16):
    items = []
    for podcast in playable_podcast16:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast17(soup17):
    subjects = []
    for content in soup17.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/a8e563679317e985d4d7c5b7cc816a06.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast17(playable_podcast17):
    items = []
    for podcast in playable_podcast17:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast18(soup18):
    subjects = []
    for content in soup18.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/8cbb50c14ab64ca67f110ea31fb4f6f5.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast18(playable_podcast18):
    items = []
    for podcast in playable_podcast18:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast19(soup19):
    subjects = []
    for content in soup19.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/1bfdea54d48417fc86b622fb45e75ee7.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast19(playable_podcast19):
    items = []
    for podcast in playable_podcast19:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast20(soup20):
    subjects = []
    for content in soup20.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/1bfdea54d48417fc86b622fb45e75ee7.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast20(playable_podcast20):
    items = []
    for podcast in playable_podcast20:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

