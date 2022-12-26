import requests
import bs4
import download_image

#send a request to wikipedia website with a list of all states
response = requests.get('https://de.wikipedia.org/wiki/List_of_countries_in_the_world)
text = response.text
soup = bs4.BeautifulSoup(text, "lxml")
#print(soup)

#select the table from the soup
table = soup.select('tbody')[0]
table_rows = table.select('tr')
#exclude table_rows that do not contain countries (title rows at the beginning and end and the unions)
table_rows = table_rows[6:-1]
#print(table_rows)

#create a new file to which will be written
file = open('import.txt', 'w', encoding = 'utf-8')

#for each country in the table
for table_row in table_rows:
    table_data_list = table_row.select('td')
    td = table_data_list[0]
    anchors = td.select('a')
    anchor = anchors[0]
    title = anchor["title"]
    print('anchor: ', anchor)
    print('title: ', title)
    print('\n')
    #get href attribute in anchor
    href = anchor["href"]

    #concatenate href with domain name to get full url path
    country_url = 'https://de.wikipedia.org/'+href

    #download and save image from the website
    html_soup = download_image.parse_page(country_url)
    image = download_image.get_flag_image(html_soup)
    image_url = download_image.get_image_url(image)
    download_image.download_and_save_image(image_url, f'{title}')

    file.write(f'<html><img src="{title}.png"></html>; {title}\n')

print('Done')

#close the file
file.close()
