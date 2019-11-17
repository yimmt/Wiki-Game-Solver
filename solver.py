import api
from collections import deque

def solve():
    random_page = api.get_random_page()
    hitler_page_id = str(api.title_to_id('Adolf_Hitler'))
    visited = {random_page}
    queue = deque([random_page])

    while queue:
        page_id = queue.popleft()
        visited.add(page_id)
        print(page_id)
        if page_id == hitler_page_id:
            print("YOU FOUND HITLER!")
            return
        try:
            neighbors = api.get_links_from_page(page_id)
        except KeyError:
            neighbors = []
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


solve()
