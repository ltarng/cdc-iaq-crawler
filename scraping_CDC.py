import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import datetime

url = "https://pm25.lass-net.org/IAQ/detail.php?city=iaq-cdc"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

datetime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

rows = soup.find('table').find_all('tr')
for row in rows:
    json_url = row.find_all('td')[3].find('a')['href']
    download_url = "https://pm25.lass-net.org" + json_url

    # Create files for each device, and save json for each device
    device_id = row.find_all('td')[2].text
    path = "./" + device_id
    os.makedirs(path, exist_ok=True)

    file_name = device_id + " " + datetime + ".json"
    save_path = path + '/' + file_name
    urlretrieve(download_url, save_path)

    print(device_id + " download completed.")
