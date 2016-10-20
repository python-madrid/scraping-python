import scrapy


class DiputadosSpider(scrapy.Spider):
    name = 'diputados'
    start_urls = ['http://www.congreso.es/portal/page/portal/Congreso/Congreso/Diputados']

    def parse(self, response):
        lista_diputados_url = response.xpath(
            '//div[@id="btn_mas"]/a/@href').extract_first()
        request = scrapy.Request(
            lista_diputados_url,
            callback=self.parse_lista_diputados)
        yield request

    def parse_lista_diputados(self, response):
        # listado de diputados
        diputados = response.xpath(
            '//div[@class="listado_1"]/ul/li/a/@href').extract()
        for diputado in diputados:
            request = scrapy.Request(
                response.urljoin(diputado),
                callback=self.parse_diputado)
            yield request

        # proxima pagina
        pagina_siguiente = response.xpath(
            '//a[contains(., "Página Siguiente")]/@href').extract_first()
        if pagina_siguiente:
            request = scrapy.Request(
                pagina_siguiente,
                callback=self.parse_lista_diputados)
            yield request

    def parse_diputado(self, response):
        nombre = response.xpath(
            '//div[@class="nombre_dip"]/text()').extract_first()
        diputado = {
            'nombre': nombre,
            'url': response.url}
        yield diputado
