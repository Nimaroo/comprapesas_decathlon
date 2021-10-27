import requests
import time
from datetime import datetime
import json
from win10toast import ToastNotifier
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

GLOBVARS = {
    'USERNAME': '',
    'PASSWORD': '',
    'BASE-URL': 'https://www.decathlon.es/es/ajax/rest/model/com/decathlon/cube/commerce/inventory/InventoryActor/getStoreAvailability',
}


def get_product_id(product):
    modelId = ''
    if product == 'Discos':
        modelId = '1042303'
    return modelId


def get_peso_id(peso):
    skuId = ''
    if peso == 5:
        skuId = '969885'
    elif peso == 10:
        skuId = '969931'
    return skuId


def check_cantidad(content):
    disp = {}
    s_disp = ''
    for stores in content:
        cantidad = stores['quantity']
        if cantidad != 0:
            disp[stores['storeName']] = cantidad
            s_disp += stores['storeName'] + ': ' + str(cantidad) + '\n'
    return disp, s_disp


def main(peso, product):
    skuId = get_peso_id(peso)
    modelId = get_product_id(product)
    '''storeIds = ['0070189601896', '0070062300623', '0070054700547', '0070008600086', '0070245002450', '0070187701877',
                '0070010200102', '0070011400114', '0070040100401', '0070140601406', '0070025700257', '0070014200142',
                '0070050600506', '0070038500385', '0070221102211', '0070032800328', '0070029900299', '0070013700137']'''
    storeIds = ['0070189601896', '0070062300623', '0070245002450', '0070010200102']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/95.0.4638.54 Safari/537.36'}
    wait_time = 1
    # Start the search
    intentos = 1
    toast = ToastNotifier()
    while True:
        response_raw = requests.get(GLOBVARS['BASE-URL'], headers=headers,
                                    params={'storeIds': ','.join(storeIds), 'skuId': skuId, 'modelId': modelId,
                                            'displayStoreDetails': False}, verify=False)
        if response_raw.status_code == 200:
            response = response_raw.json()
            content = response['responseTO']['data']
            disp, s_disp = check_cantidad(content)
            if bool(disp):
                print(s_disp)
                toast.show_toast('¡PRODUCTO ENCONTRADO!',
                                 s_disp,
                                 threaded=True)
                break
            else:
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print("Fecha y hora: " + now)
                print("Intento número: " + str(intentos))
                print("---------------------------------------\n")
                intentos += 1
                time.sleep(wait_time * 60)
        else:
            # Delete the ZIP file in the local repository
            print('There was an error getting the Confluence content. The error returned is [{}] with number [{}]'.format(response['responseTO']['errors'], response['responseTO']['httpStatus']))
            toast.show_toast('ERROR', 'Ha habido un problema al hacer el request. Mira la consola para más info!')
            break
    return


if __name__ == "__main__":
    main(5, 'Discos')
