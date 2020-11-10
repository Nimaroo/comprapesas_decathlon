# comprapesas_decathlon
COMPRAR.PY: Intenta comprar las pesas de 5Kg (se puede cambiar el peso) de Decathlon cada 5 minutos (se puede cambiar el tiempo) porque vuelan, amigos, VUELAN. No te puedes fiar de los avisos por mail

RECOGER.PY: Este script checkea si están las pesas disponibles en algunas tiendas cercanas (10 por defecto) a un códgio postal que introduzcas (hardcodeado a 08207, Sabadell). Si encuentra, te avisa por consola de la tienda y la cantidad.

Librerías que necesitas:

- Selenium (pip install selenium)
- Win10Toast (pip install win10toast)

Importante:

- NO MINIMICES la ventana que se abre o el código fallará.
- Al buscar elementos he puesto tiempos de espera que se adaptaban a mi PC/Conexión. No aseguro que no falle en otras máquinas.
- Estoy seguro que es más rentable buscar en Wallapop/Amazon o cualquier tienda física. Esto ha sido un matatiempos, al final.

Picado en Python 3.7 (x64)
