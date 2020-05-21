from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "20c9c0971cf659fba29b5b9f78015f8d"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        if loc is None:
            dispatcher.utter_message(template="utter_ask_location")
            return []
        print("locations is: " + str(loc))
        
        cuisine = tracker.get_slot('cuisine')
        if cuisine is None:
            dispatcher.utter_message(template="utter_ask_cuisine")
            return [SlotSet('location', loc)]
        print("cuisine is: " + str(cuisine))
        
        price = tracker.get_slot('price')
        if price is None:
            dispatcher.utter_message(template="utter_ask_price_range")
            return [SlotSet('location', loc), SlotSet('cuisine', cuisine)]
        print("price range is: " + str(price))

        people = tracker.get_slot('people')
        print("people is: " + str(people))

        dispatcher.utter_message("Getting the restaurant details...\n\n")

        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50,
                         'south indian': 85}

        flag = 0
        list_results = list()
   
        if price == '<=300':
            cheaper_restaurants = []
            for val in range(0, 100, 20):
                results = zomato.restaurant_search_iteratively(loc, lat, lon, str(cuisines_dict.get(cuisine)),
                                                                    start=val, sort="price", order="asc")
                d = json.loads(results)
                cheaper_restaurants.extend(d['restaurants'])
            
            cheaper_restaurants = sorted(cheaper_restaurants, key=lambda restaurant: restaurant['restaurant']['user_rating']['aggregate_rating'], reverse=True)
            list_results = [self.get_restaurant_params(restaurant) for restaurant in cheaper_restaurants[:10]]
        else:
            for val in range(0, 100, 20):
                results = zomato.restaurant_search_iteratively(loc, lat, lon, str(cuisines_dict.get(cuisine)),
                                                                start=val, sort="rating", order="desc")
                d = json.loads(results)
                for restaurant in d['restaurants']:
                    # Assuming average cost for single person is 75% of average cost of two person
                    cost_for_two = restaurant['restaurant']['average_cost_for_two']
                    
                    if price == '300-700' and cost_for_two >= 300 and cost_for_two <= 700 and len(list_results) <= 10:
                        print(self.get_restaurant_params(restaurant))
                        list_results.append(self.get_restaurant_params(restaurant))
                    if price == '>=700' and cost_for_two >= 700 and len(list_results) <= 10:
                        print(self.get_restaurant_params(restaurant))
                        list_results.append(self.get_restaurant_params(restaurant))

                    if len(list_results) > 9:
                        flag = 1
                        break

                if flag == 1:
                    break

        print("list of results - {}".format(list_results))
        dispatcher.utter_message("Showing you top rated restaurants:\n\
        \n----------------------------------------------------\n")
        if len(list_results) > 0:
            final_strn_to_dispatch = ""
            for i, val in enumerate(list_results[:5]):
                print("Dispatching...." + str(val))
                str1 = "{index}. {restaurant_name} in {restaurant_address} has been rated {rating}\
                \nAverage Cost for two person is Rs. {avg_cost_2}\
                \n----------------------------------------------------\n".format(
                    index= i+1,
                    restaurant_name=val['Restaurant Name'],
                    restaurant_address=val['Restaurant locality address'],
                    rating=val['Zomato User Rating'], avg_cost_2 = val['Average budget for two people'])
                
                final_strn_to_dispatch += str1
            dispatcher.utter_message(final_strn_to_dispatch)
            f = open('restaurants.txt', "w")
            f.write(json.dumps(list_results))
        else:
            dispatcher.utter_message("No results found..")
        return [SlotSet('location', loc)]

    def get_restaurant_params(self, restaurant):
        rest_name = restaurant['restaurant']['name']
        rest_add = restaurant['restaurant']['location']['address']
        avg_rating = str(restaurant['restaurant']['user_rating']['aggregate_rating'])
        avg_cost_two = str(restaurant['restaurant']['average_cost_for_two'])
        # Assuming average cost for single person is 75% of average cost of two person
        # avg_cost_one = str(restaurant['restaurant']['average_cost_for_two'] * 0.75)
        return {"Restaurant Name": rest_name, "Restaurant locality address": rest_add, "Zomato User Rating": avg_rating,
                "Average budget for two people": avg_cost_two}


class ActionCheckCityTier(Action):

    def name(self):
        return 'action_verify_city_tier'

    def run(self, dispatcher, tracker, domain):
        # List of tier 1 and tier 2 cities from http://en.wikipedia.org/wiki/Classification_of_Indian_cities
        supported_cities = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune",
                            "Agra",
                            "Ajmer",
                            "Aligarh", "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly", "Belgaum",
                            "Bhavnagar",
                            "Bhiwandi", "Bhopal",
                            "Bhubaneswar", "Bikaner", "Bilaspur", "Bokaro Steel City", "Chandigarh", "Coimbatore",
                            "Cuttack",
                            "Dehradun", "Dhanbad",
                            "Bhilai", "Durgapur", "Erode", "Faridabad", "Firozabad", "Ghaziabad", "Gorakhpur",
                            "Gulbarga",
                            "Guntur", "Gwalior", "Gurgaon",
                            "Guwahati", "Hamirpur", "Hubli–Dharwad", "Indore", "Jabalpur", "Jaipur",
                            "Jalandhar", "Jammu", "Jamnagar",
                            "Jamshedpur", "Jhansi", "Jodhpur", "Kakinada", "Kannur", "Kanpur", "Kochi", "Kolhapur",
                            "Kollam",
                            "Kozhikode", "Kurnool", "Ludhiana",
                            "Lucknow", "Madurai", "Malappuram", "Mathura", "Goa", "Mangalore", "Meerut", "Moradabad",
                            "Mysore",
                            "Nagpur", "Nanded", "Nashik", "Nellore",
                            "Noida", "Patna", "Pondicherry", "Purulia Prayagraj", "Raipur", "Rajkot", "Rajahmundry",
                            "Ranchi",
                            "Rourkela", "Salem", "Sangli", "Shimla",
                            "Siliguri", "Solapur", "Srinagar", "Surat", "Thiruvananthapuram", "Thrissur",
                            "Tiruchirappalli",
                            "Tiruppur", "Ujjain", "Bijapur",
                            "Vadodara", "Varanasi", "Vasai-Virar City", "Vijayawada", "Visakhapatnam", "Vellore",
                            "Warangal"]
        loc = tracker.get_slot('location')
        print("In ActionCheckCityTier class : " + str(loc))
        cities_lower = set([city.lower() for city in supported_cities])
        if loc is None:
            dispatcher.utter_message(template="utter_ask_location")
            return []
        loc = loc.lower()
        if loc not in cities_lower:
            # dispatcher.utter_message("We do not operate in that area yet!!!")
            dispatcher.utter_message(template="utter_unknown_location")
            return []
        return [SlotSet('location', loc)]


class ActionSendEmail(Action):

    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        print("In ActionSendEmail class :")
        from_user = 'dumsa@gmail.com'
        to_user = tracker.get_slot('emailid')
        if to_user is None:
            dispatcher.utter_message(template="utter_ask_email_id")
            return []
        dispatcher.utter_message("Sending email to {}".format(to_user))
        password = 'Dumsa@123'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_user, password)
        subject = 'Restaurant Results'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        f = open('restaurants.txt')
        restaurants = json.loads(str(f.read()))
        from jinja2 import Template
        t = Template(open('data/mail_body.html').read())
        body = t.render(restaurants=restaurants, int=int)
        with open('test_email', 'w') as f:
            f.write(body)
        msg.attach(MIMEText(body, 'html', 'utf-8'))
        text = msg.as_bytes()
        server.sendmail(from_user, to_user, text)
        print('Email sent successfully !!!')
        server.close()
        dispatcher.utter_message("Email sent successfully!!!")
        return []
