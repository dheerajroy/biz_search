import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

q = input("Business name/type: ")
URL = f'https://www.indiafilings.com/search/company-search?search_text={q}'
res = requests.get(URL)

if res.status_code > 300:
    raise Exception("Error with the url response, update the code")

soup = BeautifulSoup(res.text, 'html.parser')
businesses = soup.find_all('a', {'class': 'underline text-xs sm:text-sm'})
businesses = [business['href'] for business in businesses]

data = {'Name': [], 'Address': [], 'Email': []}

for business in tqdm(businesses, desc=f"Scraping {q.title()} Businesses", ascii=True):
    try:
        res = requests.get(business)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        name = soup.find('td', string='LLP Name').find_next('td').text if soup.find('td', string='LLP Name') else 'N/A'
        address = soup.find('td', string='Registered Address').find_next('td').text if soup.find('td', string='Registered Address') else 'N/A'
        email = soup.find('td', string='Email Id').find_next('td').text if soup.find('td', string='Email Id') else 'N/A'
        
        data['Name'].append(name)
        data['Address'].append(address)
        data['Email'].append(email)
    except Exception:
        continue

df = pd.DataFrame(data)
df.to_excel(f'{q}.xlsx', index=False)

print(f"Scraping completed. Data saved to {q}.xlsx")
