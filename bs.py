from bs4 import BeautifulSoup
import json

with open("sample.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print(soup)
data=[]
for item in soup.find_all("li", class_="list-element"):
    trip=dict()
    picture=item.find("img")
    trip['picture']=picture['src']
    title=item.find("p", class_="vertical-activity-card__title")
    trip['title']=title.text.strip() #title
    typeof=item.find("span", class_="vertical-activity-card__activity-type c-classifier-badge")
    trip['type']=typeof.text.strip() #type
    list_features=[]
    for feature in item.find_all("li", class_="activity-attributes__attribute"):
        list_features.append(feature.text.strip())
    trip['features']=list_features #features
    data.append(trip)
    rating=item.find("span", class_="rating-overall__rating-number rating-overall__rating-number--right")
    trip['rating']=rating.text.strip() #rating
    reviews=item.find("div", class_="rating-overall__reviews")
    trip['reviews']=reviews.text.replace('(','').replace(')','').replace('reviews','').strip() #reviews
    price=item.find("div", class_="baseline-pricing__value")
    trip['price']=price.text.strip().replace("\xa0","").replace("\n","").replace(" ","").replace("From", "From ") #price
    category_price=item.find("p", class_="baseline-pricing__category")
    trip['category_price']=category_price.text.strip()

print(data)
