import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier


def get_selenium_element(driver, command, time_wait=2, mode='xpath'):
    element = []
    if mode == 'xpath':
        element = WebDriverWait(driver, time_wait).until(
            EC.element_to_be_clickable((By.XPATH, command))
        )
    elif mode == 'class':
        element = WebDriverWait(driver, time_wait).until(
            EC.element_to_be_clickable((By.CLASS_NAME, command))
        )
    return element


def log_in(driver):
    login = get_selenium_element(driver, '//*[@id="header"]/nav/div[3]/div[3]/a')
    login.click()
    mail = get_selenium_element(driver, '//*[@id="login"]')
    my_mail = input('Introduce tu mail: ')
    mail.send_keys(my_mail)
    cont = get_selenium_element(driver, '//*[@id="validate-block"]/button')
    cont.click()
    captcha = True
    while captcha:
        try:
            my_password = input('Introduce tu password: ')
            password = get_selenium_element(driver, '//*[@id="password"]')
            password.send_keys(my_password)
            captcha = False
        except TimeoutException:
            manual = input('Creo que hay un captcha! resuelvelo y pulsa cualquier tecla para continuar: ')
    start = get_selenium_element(driver, '//*[@id="signin-block"]/button')
    start.click()
    return


def hard_click(driver, element):
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)  # Click mediante javascript
    return


def seleccionar_peso(l_pesas, peso):
    pesas = []
    if peso == 0.5:
        pesas = l_pesas[0]
    elif peso == 1:
        pesas = l_pesas[1]
    elif peso == 2:
        pesas = l_pesas[2]
    elif peso == 5:
        pesas = l_pesas[3]
    elif peso == 10:
        pesas = l_pesas[4]
    elif peso == 20:
        pesas = l_pesas[5]
    return pesas


def seleccionar_producto(driver, peso):
    tamanyos = get_selenium_element(driver, 'sizes__button', 5, 'class').click()
    try:
        l_pesas = driver.find_elements_by_class_name('sizes__size')
    except NoSuchElementException:
        print('Ha habido un problema intentando seleccionar el tamaño de las pesas')
        return 1
    pesas = seleccionar_peso(l_pesas, peso)
    hard_click(driver, pesas)
    return 0


def anyadir_cesta(driver, cantidad=4):
    cesta = get_selenium_element(driver, '//*[@id="ctaButton"]', 3)
    hard_click(driver, cesta)
    mi_cesta = get_selenium_element(driver, 'cart-button', 2, 'class')
    hard_click(driver, mi_cesta)
    # Añadimos la cantidad
    cantidad_final = 1
    while cantidad_final != cantidad:
        try:
            more = get_selenium_element(driver, 'icon-plus', 2, 'class')
            hard_click(driver, more)
            cantidad_final += 1
        except TimeoutException:
            print('El límite que se podía añadir ha sido ' + str(cantidad_final))
            break
    return cantidad_final


def check_disponible(driver):
    check = False
    try:
        no_disponible = driver.find_element_by_class_name('stock-notification__invite--active')
    except NoSuchElementException:
        # Si entra aquí es que ya hay disponibles!!
        check = True
    return check


def buscar_pesas(driver, peso=5):
    # Barra de búsqueda
    buscar = get_selenium_element(driver, '//*[@id="search-autocomplete"]')
    buscar.send_keys('Disco de fundición')
    buscar.send_keys(Keys.ENTER)

    # Primer artículo (parece que va directamente al pulsar enter)
    try:
        articulo = get_selenium_element(driver, '//*[@id="product_7278"]/div[2]/div/div/div/a/img').click()
    except TimeoutException or NoSuchElementException:
        # Asumimos que estamos ya en el producto
        pass

    # Vemos si esta disponible o no!
    toast = ToastNotifier()
    intentos = 1
    while True:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Fecha y hora: " + now )
        print("Intento número: " + str(intentos))
        print("---------------------------------------\n")
        # Añadimos a la cesta la pesa deseada
        resul = seleccionar_producto(driver, peso)
        if resul != 0:
            return resul
        # Si no lo encuentra, esperamos 5 mins
        if check_disponible(driver):
            break
        intentos += 1
        time.sleep(5 * 60)
        driver.refresh()

    # Si pasa esto asumo que es porque SÍ estan disponibles!
    cantidad_final = anyadir_cesta(driver)
    toast.show_toast("¡Pesas disponibles!", "He añadido " + str(cantidad_final) + " de ellas a la bolsa.")
    return 0


def main():
    # Usamos chromedriver y entramos en carrefour
    chrome_path = '\\'.join(os.path.realpath(__file__).split('\\')[:-1]) + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://www.decathlon.es/es/')

    # Logeamos
    # log_in(driver)

    # Buscamos las pesas de 5Kg y las añadimos a la cesta
    resul = buscar_pesas(driver)
    if resul != 0:
        print('Ha habido algún problema buscando las pesas!')
    else:
        print('Pesas añadidad sin problema a la cesta!')

    # Función comprar!

    # Fin
    driver.quit()


if __name__ == '__main__':
    main()
