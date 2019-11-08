def yelp_call(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    response = requests.get(url, headers=headers, params=url_params)
    
    data = response.json()['reviews']
    return data

def parse_results(results):
        parsed_results = []
        plumb_list = []
        for result in results:
            yelp_dict = {}
            yelp_dict["biz_id"] = result['id']
            yelp_dict["biz_name"] = result['name']
            yelp_dict["rating"] = result['rating']
            yelp_dict["review_count"] = result['review_count']
            parsed_results.append(yelp_dict)
        
        for plumb in parsed_results:
            plumb_tuple = (plumb['biz_id'], plumb['biz_name'], 
                     plumb['rating'], plumb['review_count'])
            plumb_list.append(plumb_tuple)
        return plumb_list


def db_insert(data):
    insert_statement = "INSERT INTO Plumb_biz (biz_id, biz_name, rating, review_count) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_statement, data)
    cnx.commit()


num = response.json()['total']
print('{} total matches found.'.format(num))
cur = 0
    
while cur < num and cur < 1000:
    url_params['offset'] = cur
    results = yelp_call(url_params, api_key)
    parsed_results = parse_results(results)
    db_insert(parsed_results)
    time.sleep(1) #Wait a second
    cur = 50 + cur
    