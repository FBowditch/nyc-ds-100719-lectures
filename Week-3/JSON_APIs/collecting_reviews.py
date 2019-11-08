term = 'Plumbers'
location = 'Bushwick NY'
url_params = {  'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'limit' : 50,
                'offset' : 0
             }

url_params

headers = {'Authorization': 'Bearer {}'.format(api_key)}
response = requests.get(url, headers=headers, params=url_params)
url = 'https://api.yelp.com/v3/businesses/search'
client_id = "kSJKHzaATCEw4bxY9tJGwA"
api_key = "xZce1e9e3JthFVYS0eQm1Aa6thcOEaQ2N2hzi3PJsJrv6ga4hinQMYsPWTBYQYRikD7sN9H7HQJV9sDPBoIf-m2Ko-0rw5ouSZhGgUtQDYA5_5hEipYddHf7Ct2xXXYx"

def yelp_call(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)
    
    data = response.json()['reviews']
    return data

def parse_id_results(results):
        parsed_results = []
        plumb_list = []
        for result in results:
            yelp_dict = {}
            yelp_dict["biz_id"] = result['id']
            parsed_results.append(yelp_dict)
        
        for plumb in parsed_results:
            plumb_tuple = (plumb['biz_id'])
            plumb_list.append(plumb_tuple)
        return plumb_list


def yelp_call_reviews(api_key):
    url = ('https://api.yelp.com/v3/businesses/{}/reviews'.format(biz_id))
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)
    
    data = response.json()['reviews']
    return data





def parse_review_results(results):
        parsed_results = []
        rev_list = []
        for result in results:
            yelp_dict = {}
            yelp_dict["rev_id"] = result['id']
            yelp_dict["rev_rating"] = result['rating']
            yelp_dict["name"] = result['user']
            yelp_dict["review_text"] = result['text']
            yelp_dict["rev_date"] = result['time_created']
            parsed_results.append(yelp_dict)
        
        for rev in parsed_results:
            rev_tuple = (rev['rev_id'], rev['rev_rating'], rev['name']
                     rev['review_text'], rev['rev_date'])
            rev_list.append(rev_tuple)
        return rev_list


def db_insert_reviews(data):
        insert_statement = "INSERT INTO Plumb_biz (rev_id, rev_rating, name, review_text, rev_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(insert_statement, data)
        cnx.commit()






cur = 0  
while cur < 438:
    url_params['offset'] = cur
    results = yelp_call(url_params, api_key)
    biz_id = parse_id_results(results)
    review_results = yelp_call_review(api_key, biz_id)
    parsed_review_results = parse_review_results
    db_insert_reviews(parsed_review_results)
    time.sleep(1) #Wait a second
    cur = 50 + cur
    