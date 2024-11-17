from bs4 import BeautifulSoup
import requests
import csv
# import re library to use regex
import re

# Fandom of Choice: Undertale

# Making the HTTP requests
url = "https://undertale.fandom.com/wiki/Category:Boss#List_of_Midbosses_and_Minibosses#List%20of%20Midbosses%20and%20Minibosses"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    bosses = soup.find_all('a', class_='category-page__member-link')

    with open('undertale_boss_list.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Link'])

        for boss in bosses:
            boss_name = boss.get_text()
            boss_link = "https://undertale.fandom.com" + boss.get('href')
            writer.writerow([boss_name, boss_link])
    print("Characters saved successfully! Information saved to undertale_boss_list.csv")
else:
    print("Error: Could not retrieve the page.")
        


# Include data in a CSV or JSON file!!!!