import requests

baseURL = "https://en.wikipedia.org/w/api.php"

def get_random_page():
    response = requests.get(baseURL, params = {
        "action": "query",
        "format": "json", 
        "list": "random"
    })
    data = response.json()
    page_id = data['query']['random'][0]['id']
    page_response = requests.get(baseURL, params = {
        "action": "query", 
        "format": "json", 
        "prop": "info", 
        "inprop": "url",
        "pageids": [page_id]
    })
    page_data = page_response.json()
    # The response.query.pages is mapped by ids, we get the first (or only) dict with next, iter
    pages = page_data['query']['pages']
    page = pages[next(iter(pages))]
    randomURL = page['fullurl']
    return randomURL

print(get_random_page())
