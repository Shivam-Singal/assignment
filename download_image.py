import requests

import bs4

def parse_page(url):
    response = requests.get(url) 
    text = response.text
    soup = bs4.BeautifulSoup(text, "lxml")
    return soup

def get_flag_image(soup):
    #select the list of tables with class infobox
    tables = soup.select('.infobox') 
    if len(tables) == 0:
        tables = soup.select('.wikitable')

    outer_table = tables[0] 
    index = 0
    image = outer_table.select('img')[index]
    
    while int(image["height"]) < 25 or int(image["width"]) < 25:
        image = outer_table.select('img')[index]
        index +=1 
    return image

def get_image_url(image):
    image_src = image['src']
    image_url = f"https:{image_src}"
    return image_url


def download_and_save_image(image_url, img_name):
    response = requests.get(f"{image_url}")
    file = open(f'C:\\~\\collection.media\\{img_name}.png', 'wb') #fill in your own user path here
    file.write(response.content)
    file.close()

#test the functions
if __name__ == '__main__':

    html_soup = parse_page("https://de.wikipedia.org/wiki/india")

    image = get_flag_image(html_soup)

    url = get_image_url(image)

    download_and_save_image(url, "india")
