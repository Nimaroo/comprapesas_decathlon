# comprapesas_decathlon

Picado en Python 3.7 (x64)
Dos algoritmos diferentes, en dos carpetas diferentes.

## API

**recoger_api.py**:

- MÉTODO RECOMENDADO
- Librerías adicionales necesarias: _Win10Toast_
- Este algoritmo utiliza la API de Decathlon para checkear cada X tiempo si está el producto para recoger en las tiendas deseadas. 
- Para que funcione adecuadamente necesitarás el ID del producto deseado, el modelo, y las tiendas
- Ahora está hardcodeado para los 'Discos de fundición' de 5 Kg, y para tiendas cercanas a Sabadell (Barcelona), y que busque cada minuto.
- Da un aviso de Windows si encuentra el producto, o hay un problema con el request.

## Selenium

**comprar.py**:

- Librerías adicionales necesarias: _Win10Toast_, _Selenium_
- Este algoritmo intenta comprar un producto de Decathlon cada X tiempo porque vuelan, amigos, VUELAN. No te puedes fiar de los avisos por mail.
- Ahora está hardcodeado para los 'Discos de fundición' de 5 Kg, y que intente cada minuto.
- Da un aviso de Windows si encuentra el producto.
- NO MINIMICES la ventana que se abre o el código fallará.
- Al buscar elementos con 'Selenium' he puesto tiempos de espera que se adaptaban a mi PC/Conexión. No aseguro que no falle en otras máquinas.

**recoger.py**:

- Librerías adicionales necesarias: _Win10Toast_, _Selenium_
- Este algoritmo checkea cada X tiempo si está el producto para recoger en las tiendas deseadas.
- Ahora está hardcodeado para los 'Discos de fundición' de 5 Kg, y para tiendas cercanas a Sabadell (Barcelona), y que busque cada 5 minuto.
- Da un aviso de Windows si encuentra el producto.
- NO MINIMICES la ventana que se abre o el código fallará.
- Al buscar elementos con 'Selenium' he puesto tiempos de espera que se adaptaban a mi PC/Conexión. No aseguro que no falle en otras máquinas.

