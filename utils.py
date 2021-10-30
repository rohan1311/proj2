# import random
# from datetime import datetime
# now = datetime.now()
# num = random.randint(1, 101)
# with open('/Users/I509781/Desktop/rand.txt', 'a') as f:
#     f.write('{} - Your random number is {}\n'.format(now, num))



# import sqlite3
# try:
#     conn= sqlite3.connect('/Users/I509781/Desktop/django-project/proj2/db.sqlite3')
#     print('connected succesfully')
#     conn.execute("INSERT INTO scrape_gainer VALUES(60, 'ABC', 122.2, 145.4, 120.2, 115.2, 4.01, 2552525, 125.2, 4.01, 15151.26262)")
#     print('inserted succesfully')
# except Exception as e:
#     print("error due to ", str(e))


# #for row in results:
# #    print(row)

# conn.close()




# import requests
# import json
# url = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
#     'Accept-Language':'en',
# }
# r = requests.get(url, headers=headers)
# data = json.loads(r.text)
# gainers = data["NIFTY"]["data"]
# for gainer in gainers:
#     symbol = gainer['symbol']
#     perChange = gainer['perChange']
#     high_price = gainer['high_price']
#     print(symbol, perChange, high_price)




# from requests_html import HTMLSession
# url = 'https://www.nseindia.com/market-data/top-gainers-loosers?cat=G'
# s = HTMLSession()
# r = s.get(url)
# r.html.render(sleep = 3)
# table = r.html.find('#topGainerTable') 
# print(table)




# from helium import *
# browser = start_chrome(url, headless=True)
# html = browser.page_source
# print(html)




# from selenium import webdriver
# url = 'https://www.nseindia.com/market-data/top-gainers-loosers?cat=G'
# driver = webdriver.Chrome()
# driver.get(url)
# table=driver.find_elements_by_id('topgainer-Table')
# print(table)



