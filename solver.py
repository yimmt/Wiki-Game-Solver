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
    randomURL = id_to_url(page_id)
    return randomURL


def id_to_url(id_):
    page_response = requests.get(baseURL, params = {
        "action": "query", 
        "format": "json", 
        "prop": "info", 
        "inprop": "url",
        "pageids": [id_]
    })
    page_data = page_response.json()
    # The response.query.pages is mapped by ids, we get the first (or only) dict with next, iter
    pages = page_data['query']['pages']
    page = pages[next(iter(pages))]
    url = page['fullurl']
    return url


print(get_random_page())
