from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.spreaker.com/show/2137305/episodes/feed" #ACRHallofFame
url2 = "https://www.spreaker.com/show/1241448/episodes/feed" #ACR
url3 = "https://www.spreaker.com/show/1396285/episodes/feed"#BOILERROOM
url4 = "https://www.spreaker.com/show/1506555/episodes/feed" #ELECTRICCARTALK
url5 = "https://www.spreaker.com/show/2952257/episodes/feed" #GLOBALRESEARCHNEWSHOUR
url6 = "https://www.spreaker.com/show/1423846/episodes/feed" #JAYSANALYSIS
url7 = "https://www.spreaker.com/show/1605149/episodes/feed" #MIDWEEKMIRE
url8 = "https://www.spreaker.com/show/2018742/episodes/feed" #On the QT with 21WireTV
url9 = "https://www.spreaker.com/show/2067315/episodes/feed" #Patrick Henningsen Live
url10 = "https://www.spreaker.com/show/3565559/episodes/feed" #PRIMALEDGEHEALTH
url11 = "https://www.spreaker.com/show/3083653/episodes/feed" #PRIMECAST
url12 = "https://www.spreaker.com/show/1243073/episodes/feed" #Sunday Wire with Patrick Henningsen
url13 = "https://www.spreaker.com/show/1849441/episodes/feed" #UKColumnRadio
url14 = "https://www.spreaker.com/show/1665382/episodes/feed" #Synesthesia Radio
url15 = "https://www.spreaker.com/show/1275891/episodes/feed" #HESSIANSESSION
url16 = "https://www.spreaker.com/show/1275655/episodes/feed" #ANARCHY_WITH_SPORE
url17 = "https://www.spreaker.com/show/2630557/episodes/feed" #Fvnk$oulsMixTape
url18 = "https://www.spreaker.com/show/2692227/episodes/feed" #FUSIONWITHRANDY.J
url19 = "https://www.spreaker.com/show/1276675/episodes/feed" #CORKSCREWSTWISTEDMIX
url20 = "https://www.spreaker.com/show/1267518/episodes/feed" #DIRECTEDENERGY

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30098), 
            'path': "https://d2a481t1usahi0.cloudfront.net/live/5697075.mp3?episode_id=5697075&show_id=1241448&user_id=7623132&tenant=SPREAKER&timestamp=1570339149&station_hash=server_17625_live_5697075&preroll=false",
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg", 
            'is_playable': True},
        {
            'label': plugin.get_string(30099), 
            'path': "https://api.spreaker.com/v2/episodes/19377921/stream",
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg", 
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_160/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/9aba0f2576c2e636ffe06095cb3bfc0f.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/e8302de419760afe712b955d73c6bb6c.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/ce5fc4308ce969b6027f76b57ade0bef.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/dd68fee102d6036a8f33865ba4ac6a27.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/12f343938f2e7afee46a4ed697d1205e.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/da07769414600200e71f5484d7b08955.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/4838f4a03f6b1c25029d6c9f2be0ced8.jpg"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/545c599022465f100fa6c4b07e86f7fd.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://d1bm3dmew779uf.cloudfront.net/rss/show/3565559/b4e6d9eecd3e2dcc593e68a7f23bee39.png"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/663025a4830225a11003be8e5ca26472.jpg"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/5635760f79316c76d075acd8fa8c16c1.jpg"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/3fac61f086b756e4006a6bcfd8d4b080.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/07a0b0661992b09682c2b5fbbd084fdf.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/0b241278f2a560c142ae0c483de2ea4e.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/2515908d77dd073b381269c71ef92135.jpg"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/a8e563679317e985d4d7c5b7cc816a06.jpg"},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/8cbb50c14ab64ca67f110ea31fb4f6f5.jpg"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/1bfdea54d48417fc86b622fb45e75ee7.jpg"},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/1bfdea54d48417fc86b622fb45e75ee7.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(URL4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(URL8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(URL9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(URL10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(URL11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(URL12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(URL13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(URL14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(URL15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(URL16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(URL17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(URL18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(URL19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(URL20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items

if __name__ == '__main__':
    plugin.run()
