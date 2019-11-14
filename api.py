import requests

baseURL = "https://en.wikipedia.org/w/api.php"

def get_random_page():
    response = requests.get(baseURL, params = {
        "action": "query",
        "format": "json", 
        "list": "random",
        "rnnamespace": 0
    })
    data = response.json()
    page_id = data['query']['random'][0]['id']
    randomURL = id_to_url(page_id)
    return randomURL


def get_only_page_from_query(page_data):
    # Response is mapped by ids, sometimes we only look for one page so we return the first/only one with next, iter
    pages = page_data['query']['pages']
    only_page = pages[next(iter(pages))]
    return only_page


def id_to_url(id_):
    page_response = requests.get(baseURL, params = {
        "action": "query", 
        "format": "json", 
        "prop": "info", 
        "inprop": "url",
        "pageids": [id_]
    })
    page_data = page_response.json()
    page = get_only_page_from_query(page_data)
    url = page['fullurl']
    return url


def get_links_from_page(id_):
    response = requests.get(baseURL, params = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "pageids": [id_]
    })
    data = response.json()
    page = get_only_page_from_query(data)
    links = page['links']
    return links
