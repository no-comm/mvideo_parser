import requests
import config_search
import config_list
import config_list2
class find:
    def name(how):
        list = find.list(how)
        list_return = find.search(list)
        list_return2 = find.list2(list)
        list1 = list_return2[0]
        list2 = list_return2[1]
        list = [[], [], []]
        for i in list_return:
            list[0].append(i)
        for i in list1:
            list[1].append(i)
        for i in list2:
            list[2].append(i)
        return list
    def list2(list):
        json_data = {
    'productIds': list,
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}
        response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=config_list2.cookies, headers=config_list2.headers, json=json_data)
        r = response.json()['body']['products']
        names = []
        images = []
        for i in r:
            names.append(i['name'])
            images.append(i['image'])
        return [names, images]
    
    def list(how):
        config_list.params = {
            'query': how,
            'offset': '0',
            'limit': '24',
        }
        response = requests.get('https://www.mvideo.ru/bff/products/search', params=config_list.params, cookies=config_list.cookies, headers=config_list.headers)
        r = response.json()['body']['products']
        list = []
        for i in r:
            list.append(i)
        return list
    def search(ids):
        params = {
    'productIds': ','.join(ids),
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}
        response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=config_search.cookies, headers=config_search.headers)
        r = response.json()['body']['materialPrices']
        list = []
        for i in r:
            list.append(i['price']['salePrice'])
        
        return list
