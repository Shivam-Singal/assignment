# anki_flag_country_import
Repository for web scraping Wikipedia to extract flags and countries and upload them to a deck in ankidroid


download_image.py containts the functions which are being used to open a wikipedia country page, select the html <img> element on that page, that contains the flag of that country, download and save the image file to a local computer.

main.py uses those functions to go through a list of countries on wikipedia which can be found under https://de.wikipedia.org/wiki/Liste_der_Staaten_der_Erde. For each country the country flag image is being downloaded. Then, main.py creates a for an Anki import usable textfile with the following structure:

`<html><img src="imagename.png"></html>`; countryname
  
Each line in the file represents one country. This format can be used for an import to AnkiDroid.
