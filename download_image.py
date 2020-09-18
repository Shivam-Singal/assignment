import requests
#import beautiful soup 4
import bs4

def parse_page(url):
    response = requests.get(url)
    print(response)
    text = response.text
    soup = bs4.BeautifulSoup(text, "lxml")
    return soup


def get_flag_image(soup):
    image = soup.select('img')[0]
    return image


def get_image_url(image):
    image_src = image['src']
    image_url = f"https:{image_src}"
    return image_url


def download_and_save_image(image_url, img_name):
    response = requests.get(f"{image_url}")
    file = open(f'C:\\Users\\Eddie\\AppData\\Roaming\\Anki2\\Benutzer 1\\collection.media\\{img_name}.png', 'wb')
    file.write(response.content)
    file.close()


#test the functions
if __name__ == '__main__':

    html_soup = parse_page("https://de.wikipedia.org/wiki/Republik_Zypern")

    image = get_flag_image(html_soup)

    url = get_image_url(image)

    download_and_save_image(url, "zypern")
