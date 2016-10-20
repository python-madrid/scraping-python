# Scrapper sobre el congreso de los diputados
La idea de este ejercicio es scrapear la página de los diputados.
* Se accede a la página de los [diputados](http://www.congreso.es/portal/page/portal/Congreso/Congreso/Diputados)
* Queremos recuperar una lista de diputados ![Principal](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/diputados.png). Para ello necesitamos acceder al enlace de *Listado completo de la composición de la cámara*
* Una vez que tenemos la lista de diputados, queremos iterar por todos ellos para recuperar su información ![Listado](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/listado_diputados.png).

Para la solución de este ejercicio se ha propuesto por @juanriaza dos aproximaciones:

* [python+lxml](https://gist.github.com/juanriaza/13117965405bff2226d55097f29cb5cc)
* [python+scrapy](https://gist.github.com/juanriaza/e9213fc1d6d017c3b750234588638875)
