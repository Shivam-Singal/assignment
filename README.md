# anki_flag_country_import
Repository for web scraping Wikipedia to extract flags and countries and upload them to a deck in Anki.

## File Description
### download_image.py
download_image.py contains the functions which are being used to open a wikipedia country page, select the html <img> element on that page, that contains the flag of that country, download and save the image file to a local computer.

### main.py
main.py uses those functions in download_image.py to go through a list of countries on wikipedia which can be found under https://de.wikipedia.org/wiki/Liste_der_Staaten_der_Erde. For each country the country flag image is being downloaded. Then, main.py creates a for an Anki import usable textfile with the following structure:
`<html><img src="imagename.png"></html>`; countryname
  
Each line in the file represents one country. This format can be used for an import to akn.

## Step-by-Step instructions on how to get the deck with country flags into Anki
1. Fork this Repository
1. Run main.py in your command line
1. In your current working directory this should have created a textfile with the name 'import.txt'
1. Open your Anki application on your computer
1. Create a new Anki deck for your cards
1. Go into the new deck by selecting it
1. Click on the tab file and choose import (alternatively ctrl+shift+I)
1. Choose import.txt as the file that you would like to import
1. Select the checkbox that says 'Allow HTML in Fields'
1. Click on 'Import' button

## Remarks
Right now, this only works with with German country names, as the web scraping has been programmed to work with the link https://de.wikipedia.org/wiki/Liste_der_Staaten_der_Erde, which contains a list of all country names in German. Since the site with English country names has a different build-up, the scraping of this site does not work yet.
