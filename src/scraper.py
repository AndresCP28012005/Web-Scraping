import requests
from bs4 import BeautifulSoup

def recolectar_datos():
    url = 'https://listado.mercadolibre.com.co/msi'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        productos = soup.find_all('li', {'class': 'ui-search-layout__item shops__layout-item ui-search-layout__stack'})
        
        datos = []
        for producto in productos:
            titulo = producto.find('h2', {'class': 'ui-search-item__title'})
            precio = producto.find('span', {'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})
            if titulo and precio:
                datos.append((titulo.text, precio.text))
        return datos
            
            