import requests
from bs4 import BeautifulSoup
import csv
import time

num_articles = 1500
output_file = 'wikipedia_random_intro2.csv'

 
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Introduction']) #Column needed for CSV when load in Pandas

    for i in range(num_articles):
        try:
            
            response = requests.get('http://en.wikipedia.org/wiki/Special:Random', allow_redirects=True)
            final_url = response.url
           
            soup = BeautifulSoup(response.text, 'html.parser')
            content_div = soup.find('div', class_='mw-parser-output')

            intro_paragraphs = []
            for element in content_div.find_all(['p', 'h2'], recursive=False):
                if element.name == 'p':
                    text = element.get_text(strip=True)
                    if text:  
                        intro_paragraphs.append(text)
                elif element.name == 'h2':
                    break
            if intro_paragraphs:
                introduction = ' '.join(intro_paragraphs)

                introduction = introduction.replace('"', '')
                #writer.writerow([introduction + ";"])
                writer.writerow([introduction])
                print(f"[{i+1}/{num_articles}] Agregado: {final_url}")

            time.sleep(1) 

        except Exception as e:
            print(f"Error {i+1}: {e}")
