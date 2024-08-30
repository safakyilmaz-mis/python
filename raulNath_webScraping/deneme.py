import requests
from bs4 import BeautifulSoup

# Web sayfasının URL'sini belirtin
url = 'https://www.rahulpnath.com/blog/'  # Buraya blogun URL'sini ekleyin

# Sayfayı istek ile al
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Postları bulmak için sınıf adını belirle
posts = soup.find_all('div', class_='c-post-card')

for post in posts:
    # Resim linki
    image_tag = post.find('img')
    image_url = image_tag['src'] if image_tag else 'No Image'
    
    # Başlık
    title_tag = post.find('h2', class_='c-post-card__title')
    title = title_tag.text.strip() if title_tag else 'No Title'
    
    # Kısa açıklama
    excerpt_tag = post.find('p', class_='c-post-card__excerpt')
    excerpt = excerpt_tag.text.strip() if excerpt_tag else 'No Excerpt'
    
    # Post linki
    link_tag = title_tag.find('a') if title_tag else None
    post_link = link_tag['href'] if link_tag else 'No Link'
    
    # Sonuçları yazdır
    print(f"Title: {title}")
    print(f"Image URL: {image_url}")
    print(f"Excerpt: {excerpt}")
    print(f"Post Link: {post_link}")
    print("-" * 40)
