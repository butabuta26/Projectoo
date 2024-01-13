import requests 
import csv 
from bs4 import BeautifulSoup

columns = ['Name', 'Year', 'finished or airing', 'rating']
csvfile = open('Anime.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(columns)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


web = requests.get('https://myanimelist.net/anime/genre/39/Detective', headers = headers).text
soup = BeautifulSoup(web, 'html.parser')

animes = soup.find_all('div', class_= 'js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')
# print(animes)

entry_num = 0

for anime in animes:
    name = anime.find('a', class_ = 'link-title').text
    # print(name)

    year = anime.find('span', class_ = 'item').text.split(', ')[-1]
    foa = anime.find('span', class_ = 'item finished').text
    rate = anime.find('div', title = 'score').text 

    entry_num += 1

    csvwriter.writerow([entry_num, name, year, foa, rate])


print(f"Done writing {entry_num} entries to the csv file!")
csvfile.close()





    
