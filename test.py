import requests
from bs4 import BeautifulSoup

# Set a consistent user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://www.booking.com/searchresults.html?ss=Addis+Ababa%2C+Ethiopia&efdco=1&aid=355028&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-603097&dest_type=city&checkin=2025-03-16&checkout=2025-03-17&group_adults=2&no_rooms=1&group_children=0&flex_window=7'
response = requests.get(url, headers=headers)



if response.status_code == 200:
    print('Connection Successful!')
    soup = BeautifulSoup(response.text, 'lxml')
    hotel_divs = soup.find_all('div', role='listitem')
    for hotel in hotel_divs:
        # Hotel name
        hotel_name = hotel.find('div', class_='f6431b446c a15b38c233').text.strip()
        
        # Location
        locations = hotel.find('span', class_="aee5343fdb def9bc142a").text.strip()
        
        # Price
        price = hotel.find('span', class_='f6431b446c fbfd7c1165 e84eb96b1f').text.strip().replace('US$', '')
        
        # Rating value (with check)
        rating_element = hotel.find('div', class_='a3b8729ab1 e6208ee469 cb2cbb3ccb')
        rating_val = rating_element.text.strip() if rating_element else 'N/A'
        
        # Rating score (with check)
        rating_score_element = hotel.find('div', class_='a3b8729ab1 d86cee9b25')
        rating_score = rating_score_element.text.strip() if rating_score_element else 'N/A'
        
        print(hotel_name)
        print(locations)
        print(price)
        print(rating_val)
        print(rating_score)
        print('-----------------------------------')

else:
    print('Connection Failed!',(response.status_code))