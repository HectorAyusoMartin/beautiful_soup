from bs4 import BeautifulSoup
import requests
import pandas as pd


def main():
    
    #Caso práctico:
    """
    Queremos acceder a una página web de manera programática, utilizando Python y 
    procesar algunos de sus componentes.
    Ejemplo: 'Hacker News'.
    Esta página tiene una serie de artículos, y cada artículo tiene ciertas propiedades:
    (rating, comentarios, el propio enlace a la noticia...)
    Nuestro objetivo es conseguir toda la información que aparece en la página y quedarnos
    con algunos componentes relevantes, por ejemplo el titulo del artículo, el enlace y el
    numemero de puntos que tienen. Podríamos hacer uso de Selenium para tal proposito también,
    pero vamos a usar bs4 de manera que no tendramos que acceder de manera dinámica al navegador
    para poder obtener estos elementos.
    """
    
    #Primero: descargar la web
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    #Aqui podemos ver todo el código HTML que ha descargado, pero sin procesar
    #   print(response.content)
    #beautiful_soup_4 lo que nos permite es procesar todo este código para poder acceder a sus elementos
    #de manera mucho mas programática y sencilla.
    soup = BeautifulSoup(response.content,'html.parser')
    #Ahora vamos a extraer ciertos elementos, como los titulos, los links, y los scores.
    titles = []
    links = []
    scores= []
    
    for item in soup.find_all('tr', class_='athing'):
        title_line = item.find('span',class_='titleline')
        if title_line:
            title = title_line.text
            title_link = title_line.find('a')
            link = title_link['href']
            score = item.find_next_sibling('tr').find('span',class_='score')
            if score:
                score = score.text
            else:
                score = 'None'
            titles.append(title)
            links.append(link)
            scores.append(score)
        else:
            print('No se encontró un titulo para el elemento')  
            
    df = pd.DataFrame({
        
        'Title' : title,
        'Link' : links,
        'Score': scores 
               
    })
    
    print(df)
    





if __name__ == '__main__':
    
    main()
    

