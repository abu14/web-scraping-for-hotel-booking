## 🏨 **Hotel Booking Scraper**

![GitHub contributors](https://img.shields.io/github/contributors/abu14/web-scraping-for-hotel-booking)
![GitHub forks](https://img.shields.io/github/forks/abu14/web-scraping-for-hotel-booking)
![GitHub stars](https://img.shields.io/github/stars/abu14/web-scraping-for-hotel-booking)
![GitHub issues](https://img.shields.io/github/issues/abu14/web-scraping-for-hotel-booking)
![GitHub license](https://img.shields.io/github/license/abu14/web-scraping-for-hotel-booking)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/abenezer-tesfaye-191579214/)


This Python script is designed to scrape hotel information from **Booking.com** using the BeautifulSoup and Requests libraries. 
It automates the process of collecting key hotel details, such as *hotel names, locations, prices, ratings, review counts, distances from the city center, 
free cancellation status, and direct links to hotel pages*. The script sends **HTTP requests** to a user-provided Booking.com search URL, parses the HTML content, and saves the extracted data into a structured CSV file. 
To avoid detection and rate limiting, it uses a custom user agent and implements a random delay between requests, mimicking human browsing behavior.

> Note: For large-scale data scraping, I would consider using tools like ***Bright Data*** to manage proxies and avoid IP blocking when making frequent requests. Also, to use ***Selenium*** Library to manage reload time and other web page related and brwoser related issues that might arise.


### ✨ **Features**

* Scrapes detailed hotel information from Booking.com, including:

  * Hotel name
  * Location
  * Price (in USD)
  * Rating value and score
  * Review count
  * Distance from the city center
  * Free cancellation status
  * Direct link to the hotel page

> Possible to include even more features based on requirements. This is for demonstration purposes.

- Handles missing data gracefully (e.g., hotels without ratings or reviews).
- Saves output in a structured CSV file for easy analysis.
- Implements a random delay (3–7 seconds) to avoid detection and rate limiting.

### 📦 **Requirements**

```
* Python → 3.12.3
* BeautifulSoup4 → 4.13.3
* Requests → 2.32.3
* CSV (standard library)
* Time (standard library)
* Random (standard library)
```

⚙️ ### **Usage**

1. Clone the repository:
```bash
  git clone https://github.com/abu14/web-scraping-for-hotel-booking.git
  cd web-scraping-for-hotel-booking
```

2. Install dependencies:
   ```bash
    pip install beautifulsoup4 requests
   ```

3. Run the script:
   ```bash
    python webscraper.py
   ```
4. Provide inputs when prompted:

  * Enter the Booking.com search URL.
  * Specify a file name for the CSV output.

**Example:**

    > Please enter the web url: https://www.booking.com/searchresults.html?ss=Miami
    
    > Please create a file name: miami_hotels

### 📝 **License**

This project is licensed under the MIT License.  See [LICENSE](./LICENSE) file for more details.
  

<!-- CONTACT -->
### **Contact**

##### Abenezer Tesfaye

⭐️ Email - tesfayeabenezer64@gmail.com
 
Project Link: [Github Repo](https://github.com/abu14/web-scraping-for-hotel-booking)

