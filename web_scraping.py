import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def fetch_reviews(page_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    response = requests.get(page_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = []
    
    # Kullanıcı adı, yorum, puan ve tarih bilgilerini çekme
    review_containers = soup.find_all('div', class_="styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ")  # Sınıf adı değişebilir
    for container in review_containers:
        try:
            username = container.find('span', class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17").text.strip()
            review_date = container.find('p',class_="typography_body-m__xgxZ_ typography_appearance-default__AAY17").text.strip()
            review_text = container.find('p',class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn").text.strip()
            rating = container.find('div', {'data-service-review-rating': True})['data-service-review-rating']
            
            reviews.append({
                "username": username,
                "review_date": review_date,
                "review_text": review_text,
                "rating": rating
            })
        except Exception as e:
            print(f"Error parsing review: {e}")
    
    return reviews

def scrape_all_pages(start_url, max_pages=505):
    reviews = []
    for i in range(1, max_pages + 1):
        url = f"{start_url}?page={i}"
        print(f"Scraping page: {url}")
        page_reviews = fetch_reviews(url)
        if not page_reviews:
            print("No more reviews found or failed to fetch.")
            break
        reviews.extend(page_reviews)
        time.sleep(random.uniform(2, 5))  # 2 ile 5 saniye arasında bekle
    return reviews

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8-sig')  # UTF-8 Sig Türkçe karakter desteği için
    print(f"Data saved to {filename}")

# Başlangıç URL'si
start_url = "https://www.trustpilot.com/review/betterme.world"

# Tüm yorumları çekme
all_reviews = scrape_all_pages(start_url, max_pages=505)

# CSV'ye kaydetme
if all_reviews:
    save_to_csv(all_reviews, "reviews8.csv")
else:
    print("No reviews to save.")
