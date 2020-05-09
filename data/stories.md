## When User gives location, cuisine, price one by one as per the questions asked by bot - Check for invalid city
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhilwara"}
    - slot{"location": "bhilwara"}
    - action_verify_city_tier
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## When User gives location, cuisine, price one by one as per the questions asked by bot
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## When user gives fires a query with location + affirm intent
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## When user gives fires a query with location + goodbye intent
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye


## When user provides cusine and location at one shot + goodbye intent
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye


## When user provides cuisine and location at one shot + affirm intent
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_verify_city_tier
    - utter_ask_price_range
* restaurant_search{"price": ["300","700"]}
    - slot{"price": ["300","700"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    
## When user provides location, cuisine, number of people and price range at one shot
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "cuisine": "chinese", "people":"4", "price":["mid"]}
    - slot{"location": "delhi"}
    - action_verify_city_tier    
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": ["mid"]}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid":"xyz@gmail.com"}
    - slot{"emailid": "xyz@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bhilwara"}
    - slot{"location": "bhilwara"}
    - action_verify_city_tier
    - utter_goodbye
* goodbye


## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* send_email{"emailid": "ahbcdj@dkj.com"}
    - slot{"emailid": "ahbcdj@dkj.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_city_tier
    - slot{"location": "Rishikesh"}
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_city_tier
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": ">=700"}
    - slot{"price": ">=700"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_ask_email_id
* send_email{"emailid": "xyz@sth.edu"}
    - slot{"emailid": "xyz@sth.edu"}
    - action_send_email
* goodbye
    - utter_goodbye


<!-- Stories added Later -->
## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search{"location": "bhandup"}
    - slot{"location": "bhandup"}
    - action_verify_city_tier
    - slot{"location": "bhandup"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cusine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_id
* stop
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bhandup"}
    - slot{"location": "Bhandup"}
    - action_verify_city_tier
    - utter_ask_location

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "abcd"}
    - slot{"location": "abcd"}
    - action_verify_city_tier
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price": ">=700"}
    - slot{"price": ">=700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_id
* others
    - action_send_email
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* others
    - utter_default
    - utter_ask_howcanhelp
* others
    - utter_default
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "<=300"}
    - slot{"price": "<=300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_id
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* others
    - utter_default
    - utter_ask_location
* restaurant_search{"location": "Firozabad"}
    - slot{"location": "Firozabad"}
    - action_verify_city_tier
    - slot{"location": "firozabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "firozabad"}
    - utter_ask_email_id
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - action_send_email
* stop
    - utter_goodbye

## interactive_story_1
* goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price": "<=300"}
    - slot{"price": "<=300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "300-700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "300-700"}
    - action_verify_city_tier
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_verify_city_tier
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price": ">=700"}
    - slot{"price": ">=700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_email_id
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_verify_city_tier
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_email_id
* stop
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"price": "300-700", "location": "baroda"}
    - slot{"location": "baroda"}
    - slot{"price": "300-700"}
    - action_verify_city_tier
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - action_search_restaurants
    - slot{"location": "baroda"}
    - utter_ask_email_id
* stop
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* stop
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_city_tier
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* send_email{"emailid": "ahbcdj@dkj.com"}
    - slot{"emailid": "ahbcdj@dkj.com"}
    - action_send_email
* stop
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_city_tier
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_city_tier
    - action_verify_city_tier
    - utter_ask_location
* restaurant_search{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - action_verify_city_tier
    - slot{"location": "warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price": ">=700"}
    - slot{"price": ">=700"}
    - action_search_restaurants
    - slot{"location": "warangal"}
    - utter_ask_email_id
* send_email{"emailid": "xyz@sth.edu"}
    - slot{"emailid": "xyz@sth.edu"}
    - action_send_email
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_verify_city_tier
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price": "<=300"}
    - slot{"price": "<=300"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_id
* affirm
    - utter_ask_email_id
* send_email{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
* send_email{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_city_tier
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_city_tier
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price": "<=300"}
    - slot{"price": "<=300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email_id
* affirm
    - utter_ask_email_id
* send_email{"emailid": "jddk.2jmd@kdl.co.in"}
    - slot{"emailid": "jddk.2jmd@kdl.co.in"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": ">=700", "location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"price": ">=700"}
    - action_verify_city_tier
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* send_email{"emailid": "rohitshende16@gmail.com"}
    - slot{"emailid": "rohitshende16@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* affirm{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - action_search_restaurants
    - slot{"location": "guwahati"}
    - utter_ask_email_id
* others{"emailid": "rohit@abc.xom"}
    - slot{"emailid": "rohit@abc.xom"}
    - action_send_email
* affirm
    - utter_goodbye
