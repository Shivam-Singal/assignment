import requests
import bs4
import download_image

response = requests.get('https://de.wikipedia.org/wiki/List_of_countries_in_the_world)
text = response.text
soup = bs4.BeautifulSoup(text, "lxml")

table = soup.select('tbody')[0]
table_rows = table.select('tr')
table_rows = table_rows[6:-1]


file = open('import.txt', 'w', encoding = 'utf-8')

for table_row in table_rows:
    table_data_list = table_row.select('td')
    td = table_data_list[0]
    anchors = td.select('a')
    anchor = anchors[0]
    title = anchor["title"]
    print('anchor: ', anchor)
    print('title: ', title)
    print('\n')
    href = anchor["href"]

    country_url = 'https://de.wikipedia.org/'+href

    html_soup = download_image.parse_page(country_url)
    image = download_image.get_flag_image(html_soup)
    image_url = download_image.get_image_url(image)
    download_image.download_and_save_image(image_url, f'{title}')

    file.write(f'<html><img src="{title}.png"></html>; {title}\n')

print('Done')

file.close()
