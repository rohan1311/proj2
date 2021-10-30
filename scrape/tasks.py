from proj2.celery import app
from .models import Gainer
import logging
import requests
import json

logger = logging.getLogger('django')
url = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept-Language':'en',
}

@app.task(name='update_gainers')
def update_gainers():
    logger.info("updating gainer db")
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    gainers = data["NIFTY"]["data"]
    Gainer.objects.all().delete()
    for gainer in gainers:
        symbol = gainer['symbol']
        perChange = gainer['perChange']
        high_price = gainer['high_price']
        open_price = gainer['open_price']
        low_price = gainer['low_price']
        prev_price = gainer['prev_price']
        net_price = gainer['net_price']
        turnover = gainer['turnover']
        trade_quantity = gainer['trade_quantity']
        ltp = gainer['ltp']
        g = Gainer(symbol=symbol, perChange=perChange, high_price=high_price, open_price=open_price, low_price=low_price,
        prev_price=prev_price, net_price=net_price, turnover=turnover, trade_quantity=trade_quantity,ltp=ltp)
        g.save()

# @shared_task(bind=True)
# def run_create_obj():
#     create_test_object(name='new2021')
