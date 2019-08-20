# -*- coding: utf-8 -*-
import requests
import bs4
import pandas as pd

df = pd.DataFrame()
url_data = [] # you dont need to fill here.
brand_list = [] # fill your competitors domain name.
#sample
#brand_list = ['amazon.com','rakuten.com']

while True :
    print ('If you want to finish it, type "Done"')
    keyword_search = input('Keyword ?　') 
    if keyword_search == 'Done' :
        break
    else:
        # Default is Japanese Serp, If you need please change the default url.
        serp = requests.get('https://www.google.co.jp/search?hl=ja&num=100&q=' + ''.join(keyword_search), headers = {'User-agent': 'your bot 0.1'})
        serp.raise_for_status()
        bs4_google = bs4.BeautifulSoup(serp.text, 'html.parser')
        # Google sometimes changes the name of class. If it is not working properly, Please check the class
        url_google = bs4_google.select('div.kCrYT > a')
        for i in range(len(url_google)):
            site_url = url_google[i].get('href').split('&sa=U&')[0].replace('/url?q=', '')
            url_data.append(site_url)
        df[keyword_search] = pd.Series(url_data)
        for brand in brand_list :

            rank = df.loc[df[keyword_search].str.contains(brand, na=False),keyword_search].index
            if len(rank) != 0 :
                print('%s ： Rank %d' % (brand, rank[0] + 1))
            else :
                print('%s ： %s' % (brand, '-'))
        url_data = []