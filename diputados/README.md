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

# Ejecución de la segunda solución (hacerlo con scrapy)
Esta solución es más avanzada ya que de primeras hay que tener instalado scrapy en el sistema para poder llevarla acabo. Para poder hacer eso de una forma limpia (no instalar scrapy directamente en el sistema, ya que tiene un montón de dependencias que al instalarlas nos puede dar problemas con otras librerías que dependían de ellas y se queden rotas), se recomienda el uso de una `virtualenv`. En caso de utilizar Ubuntu, hay un blogpost muy interesante [Virtualenv para python en Ubuntu](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu). Los pasos resumidos podrían ser los siguientes:

## Instalación de un virtualenv

* `sudo apt-get install python3-pip` Instalar pip para python3
* `pip3 completion --bash >> ~/.bashrc` Permitir el completado automático para pip3.
* `source ~/.bashrc` Habilitar la funcionalidad anterior
* `pip3 install --user virtualenvwrapper` Instalar *virtualenvwrapper* que ofrece comandos sencillos para manejar los entornos virtuales.
* `echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc` Para añadir al path de la terminal *VIRTUALENVWRAPPER_PYTHON*
* `echo "source ~/.local/bin/virtualenvwrapper.sh" >> ~/.bashrc` Habilitar la funcionalidad anterior.
* `export WORKON_HOME=~/.virtualenvs` Crear una variable de entorno que apunte a donde crearemos nuestros entornos virtuales.
* `mkdir $WORKON_HOME` Crear el directorio de los entornos virtuales.
* `echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc` Introducir la variable de entorno en nuestro bash local para tenerlo siempre disponible.
* `echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bashrc` Truco para decir a python que la creación de entornos virtuales tiene que ser en *$WORKON_HOME*.
* `source ~/.bashrc` Habilitar los cambios anteriores en el sistema.


Ahora falta testear lo que hemos configurado:
* `mkvirtualenv -p python3 test` .... ERRORRRRRRRRRRRRRRR, para solucionar este error he necesitado instalar *virtualenv* mediante el gestor de paquetes de ubuntu:
  * `sudo apt install virtualenvwrapper` Ahora parece que todo funciona...
![virtualenv](https://github.com/python-madrid-learn/scrapping-python/blob/master/resources/virtualenv_test.png)

## Ejecución del ejemplo con scrapy

* `pip3 install scrapy` Instala scrapy en tu entorno virtual que este activado.
* `scrapy runspider diputados_scrapy.py` corre el script de en la consola
* `scrapy runspider diputados_scrapy.py -o diputados.csv` misma ejecución, pero pinta los resultados en un csv.

Posibles problemas con dependencias:
* `sudo apt-get install libssl-dev python3-dev` Instalar las dependencias de desarrollo de python y criptographycs
