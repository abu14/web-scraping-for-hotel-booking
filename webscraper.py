#a web scraping app that scrapes from the booking.com
import requests
from bs4 import BeautifulSoup
import csv 
import time 
import random


#web_url = 'https://www.booking.com/searchresults.html?ss=Addis+Ababa%2C+Ethiopia&efdco=1&aid=355028&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-603097&dest_type=city&checkin=2025-03-16&checkout=2025-03-17&group_adults=2&no_rooms=1&group_children=0&flex_window=7'


def web_scrapper_v1(url, f_name):
    
    print("Thanks for providing the url and file name. \n The Web scrapping has began!")
    
    num = random.randint(3, 7)
    
    #processing
    time.sleep(num)

    # Set a consistent user agent
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

    response = requests.get(url, headers=header)

    #open a file for our ouptut to be save in
    with open(f'{f_name}.csv', 'w',encoding='utf-8', errors='replace') as file:
        
        writer = csv.writer(file)
        writer.writerow(['hotel_name', 'locations', 'price', 'rating_val', 'rating_score', 'review','distanc_main', 'fee_cancellation' ,'link'])
        
        if response.status_code == 200:
            print('Connection Successful!')
            soup = BeautifulSoup(response.text, 'lxml')
            hotel_divs = soup.find_all('div', role='listitem')
            for hotel in hotel_divs:
                
                # Hotel name
                hotel_name = hotel.find('div', class_='f6431b446c a15b38c233').text.strip().replace('"',"")
                hotel_name if hotel_name else 'NA'
                
                # Location
                locations = hotel.find('span', class_='aee5343fdb def9bc142a').text.strip()
                locations if locations else 'NA'
                
                # Price
                price = hotel.find('span', class_='f6431b446c fbfd7c1165 e84eb96b1f')
                price = price.text.strip().replace('US$', '') if price else 'NA'
                
                # Rating value error handling because it keeps throwing an error since some have no ratings
                rating_element = hotel.find('div', class_='a3b8729ab1 e6208ee469 cb2cbb3ccb')
                rating_val = rating_element.text.strip() if rating_element else 'N/A'
                
                # Rating score
                rating_score_element = hotel.find('div', class_='a3b8729ab1 d86cee9b25')
                rating_score = rating_score_element.text.strip().split(' ')[-1] if rating_score_element else 'N/A'
                
                #review
                review_element = hotel.find('div', class_='abf093bdfe f45d8e4c32 d935416c47')
                review = review_element.text.strip() if review_element else 'N/A'
                
                #distnance to hotel from the main
                #distnace = hotel.find('span', {'data-testid': 'distance'}).text.strip().split(' ')[0]


                distance = hotel.find('span', {'data-testid': 'distance'})
                distanc_main = distance.text.strip().split(' ')[0] if distance else 'N/A'

                
                cancelation = hotel.find('div', 'abf093bdfe d068504c75')
                fee_cancellation = cancelation.text.strip() if cancelation else 'N/A'
                free_cancellation = 'Free Cancelation' if cancelation else 'N/A'

                #link to hotel
                link = hotel.find('a', href=True).get('href') 
                link if link else 'NA'


                # save the ouptu on to a csv file
                writer.writerow([hotel_name, locations, price, rating_val, rating_score, review, distanc_main, free_cancellation, link])
            print('Data Scrapped Succesfullly!!')
        else:
            print('Connection Failed!',(response.status_code))



#
if __name__ == '__main__':
    url = input("Please enter the web url : ")
    fn = input("Please create a file name : ")


    #call the function
    web_scrapper_v1(url, fn)