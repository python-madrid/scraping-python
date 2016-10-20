# Scrapper sobre el congreso de los diputados
La idea de este ejercicio es scrapear la página de los diputados.
* Se accede a la página de los [diputados](http://www.congreso.es/portal/page/portal/Congreso/Congreso/Diputados)
* Queremos recuperar una lista de diputados ![Principal](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/diputados.png). Para ello necesitamos acceder al enlace de *Listado completo de la composición de la cámara*
* Una vez que tenemos la lista de diputados, queremos iterar por todos ellos para recuperar su información ![Listado](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/listado_diputados.png).

Para la solución de este ejercicio se ha propuesto por @juanriaza dos aproximaciones:

* [python+lxml](https://gist.github.com/juanriaza/13117965405bff2226d55097f29cb5cc)
* [python+scrapy](https://gist.github.com/juanriaza/e9213fc1d6d017c3b750234588638875)


# Ejecución de la primera solución
* Se ha copiado en este repo la solución propuesta por @juanriaza. Para ejecutarlo, si se tienen todas las librerías y dependencias instaladas valdría con `python diputados_basico.py`.
* Los posibles problemas que se puede encontrar uno es no tener todas las dependencias perfectamente descargadas o utilizar una versión de python incorrecta:
  * Para el ejemplo se utiliza python 3.x
  * El ejemplo utiliza la librería `lxml` y `urllib`
    * `pip3 install xlml`
    * `pip3 install urllib`
* El ejemplo es tan básico que se realiza de forma secuencial, se podría paralelizar... Si todo es correcto se debería tener una ejecución como la siguiente:
![Principal](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/diputados_basico_ejecucion.png)
