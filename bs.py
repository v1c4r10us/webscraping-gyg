from bs4 import BeautifulSoup
import json
import sys
import os

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
            trip['category_price']=category_price.text.strip() #category_price
            details_link=item.find("a", class_="vertical-activity-card__container gtm-trigger__card-interaction")
            details_link="https://www.getyourguide.com/"+details_link['href']
            trip['details_link']=details_link #details_link
            ##
            os.system("bash gen_dummy.sh {0}".format(details_link))
            supplier=get_detail("a", "supplier-name__link adp-simple-experiment__link", False)
            trip['supplier']=supplier #supplier
            picture_collage=get_details("img", "photo-collage__image-source", True)
            trip['picture_collage']=picture_collage #picture_collage
            includes=get_details("span", "activity-inclusions__test activity-inclusions__test--include", False)
            trip['includes']=includes #includes
            excludes=get_details("span", "activity-inclusions__test activity-inclusions__test--exclude", False)
            trip['excludes']=excludes #excludes
            ##
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
                trip['category_price']=category_price.text.strip() #category_price
                details_link=item.find("a", class_="vertical-activity-card__container gtm-trigger__card-interaction")
                details_link="https://www.getyourguide.com/"+details_link['href']
                trip['details_link']=details_link #details_link
                ##
                os.system("bash gen_dummy.sh {0}".format(details_link)) #Creating dummy.html
                supplier=get_detail("a", "supplier-name__link adp-simple-experiment__link", False)
                trip['supplier']=supplier #supplier
                picture_collage=get_details("img", "photo-collage__image-source", True)
                trip['picture_collage']=picture_collage #picture_collage
                includes=get_details("span", "activity-inclusions__test activity-inclusions__test--include", False)
                trip['includes']=includes #includes
                excludes=get_details("span", "activity-inclusions__test activity-inclusions__test--exclude", False)
                trip['excludes']=excludes #excludes
                ##
                data.append(trip)
                print(trip)
    fp.close()
    return data

def get_detail(component, class_comp, isAttribute):
    res=""
    with open('peru/html/dummy.html') as f:
        soup=BeautifulSoup(f, 'html.parser')
        result=soup.find(component, class_=class_comp)
        if isAttribute:
            res=result['href']
        else:
            res=result.text
    f.close()
    return res

def get_details(component, class_comp, isAttribute):
    res=[]
    with open('peru/html/dummy.html') as f:
        soup=BeautifulSoup(f, 'html.parser')
        result=soup.find_all(component, class_=class_comp)
        for r in result:
            if isAttribute:
                res.append(r['src'])
            else:
                res.append(r.text)
    f.close()
    return res

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
