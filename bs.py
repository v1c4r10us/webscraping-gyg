from bs4 import BeautifulSoup
import json
import sys

def get_data(url):
    data=[]
    with open(url) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        for item in soup.find_all("div", class_="activity-card-block activity-card-block--vertical"):
            trip=dict()
            picture=item.find("source")
            if picture.has_attr('srcset'): trip['picture']=picture['srcset']
            if picture.has_attr('data-srcset'): trip['picture']=picture['data-srcset'] #picture url
            title=item.find("p", class_="vertical-activity-card__title")
            trip['title']=title.text.strip() #title
            typeof=item.find("span", class_="vertical-activity-card__activity-type c-classifier-badge")
            trip['type']=typeof.text.strip() #type
            list_features=[]
            for feature in item.find_all("li", class_="activity-attributes__attribute"):
                list_features.append(feature.text.strip())
            trip['features']=list_features #features
            rating=item.find("span", class_="rating-overall__rating-number rating-overall__rating-number--right")
            if rating != None: trip['rating']=rating.text.strip() #rating
            reviews=item.find("div", class_="rating-overall__reviews")
            if reviews != None: trip['reviews']=reviews.text.replace('(','').replace(')','').replace('reviews','').strip() #reviews
            price=item.find("div", class_="baseline-pricing__value")
            trip['price']=price.text.strip().replace("\xa0","").replace("\n","").replace(" ","").replace("From", "From ") #price
            category_price=item.find("p", class_="baseline-pricing__category")
            trip['category_price']=category_price.text.strip()
            data.append(trip)
            print(trip)
        if len(data)==0:
            for item in soup.find_all("li", class_="list-element"):
                trip=dict()
                picture=item.find("source")
                if picture.has_attr('srcset'): trip['picture']=picture['srcset']
                if picture.has_attr('data-srcset'): trip['picture']=picture['data-srcset'] #picture url
                title=item.find("p", class_="vertical-activity-card__title")
                trip['title']=title.text.strip() #title
                typeof=item.find("span", class_="vertical-activity-card__activity-type c-classifier-badge")
                trip['type']=typeof.text.strip() #type
                list_features=[]
                for feature in item.find_all("li", class_="activity-attributes__attribute"):
                    list_features.append(feature.text.strip())
                trip['features']=list_features #features
                rating=item.find("span", class_="rating-overall__rating-number rating-overall__rating-number--right")
                if rating != None: trip['rating']=rating.text.strip() #rating
                reviews=item.find("div", class_="rating-overall__reviews")
                if reviews != None: trip['reviews']=reviews.text.replace('(','').replace(')','').replace('reviews','').strip() #reviews
                price=item.find("div", class_="baseline-pricing__value")
                trip['price']=price.text.strip().replace("\xa0","").replace("\n","").replace(" ","").replace("From", "From ") #price
                category_price=item.find("p", class_="baseline-pricing__category")
                trip['category_price']=category_price.text.strip()
                data.append(trip)
                print(trip)
    fp.close()
    return data

def create_json(data, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
    f.close()

def main():
    page=str(sys.argv[1])
    data=get_data("peru/html/p{0}.html".format(page))
    data={'p{0}'.format(page):data}
    create_json(data, "peru/json/p{0}.json".format(page))

if __name__=="__main__":
    main()
