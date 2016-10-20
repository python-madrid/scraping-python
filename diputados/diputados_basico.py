import requests

from urllib.parse import urljoin
from lxml.html import fromstring


def parse_diputado(response):
    tree = fromstring(response.content)
    nombre = tree.xpath('//div[@class="nombre_dip"]/text()')[0]
    print(nombre)


def parse_lista_diputados(response):
    tree = fromstring(response.content)

    # listado de diputados
    diputados = tree.xpath('//div[@class="listado_1"]/ul/li/a/@href')
    for diputado in diputados:
        diputado_url = urljoin(response.url, diputado)
        response = requests.get(diputado_url)
        parse_diputado(response)

    # proxima pagina
    pagina_siguiente = tree.xpath('//a[contains(., "Página Siguiente")]/@href')
    if pagina_siguiente:
        pagina_siguiente_url = pagina_siguiente[0]
        response = requests.get(pagina_siguiente_url)
        parse_lista_diputados(response)

response = requests.get(
    'http://www.congreso.es/portal/page/portal/Congreso/Congreso/Diputados')
tree = fromstring(response.content)
lista_diputados_url = tree.xpath('//div[@id="btn_mas"]/a/@href')[0]
response = requests.get(lista_diputados_url)
parse_lista_diputados(response)
