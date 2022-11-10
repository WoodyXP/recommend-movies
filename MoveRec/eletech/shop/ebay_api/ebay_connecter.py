import json
import datetime
from ebaysdk.finding import Connection as finding  # install with pip
from bs4 import BeautifulSoup  # install with pip


def get_kw(search_string):
    Searches = search_string
    Keywords = Searches
    return Keywords


def get_items(Keywords):
    api = finding(appid='Michaeld-M151Ele-PRD-9e90acf8a-494310b7', siteid='EBAY-CH', config_file=None)  # change country with 'siteid='
    api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}
    response = api.execute('findItemsByKeywords', api_request)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.find_all('item')
    return items


def res_print(items):
    product_list = []
    for item in items:
        cat = item.categoryname.string.lower()
        title = item.title.string.lower().strip()
        price = int(round(float(item.currentprice.string)))
        url = item.viewitemurl.string.lower()
        seller = item.sellerusername.text.lower()
        product_dict = {"Title": title, "Category": cat, "Price": price, "Url": url, "Seller": seller}
        product_list.append(product_dict)
    return (product_list)


today = str(datetime.date.today())
ebay_results = 'ebay_results-' + today + '.json'


def wr_json(items):
    tdat = {}
    idat = {}
    with open(ebay_results, "a+") as json_file:
        for item in items:
            idat["cat"] = item.categoryname.string.lower()
            idat["title"] = item.title.string.lower().strip()
            idat["price"] = int(round(float(item.currentprice.string)))
            idat["url"] = item.viewitemurl.string.lower()
            idat["seller"] = item.sellerusername.text.lower()
            idat["title"] = item.title.string.lower().strip()
            tdat.update(idat)
            json.dump(tdat, json_file)
            json_file.write('\n')


def read_json():
    with open(ebay_results) as json_file:
        data = json_file.read()
    print(data)


####################### main ##########################

#Keywords = get_kw()  # text file in same dir - one search term per line

#for i in range(len(Keywords)):
 #   x = get_items(Keywords[i])
  #  wr_json(x)

#read_json()  # appends at moment, may make new one, with date/time in filename.
