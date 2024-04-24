import requests
import json



def searchcall(searches:str):
    engines = ["google", "duckduckgo", "bing"]
    link = 'https://serpapi.com/search.json?engine={}&q={}&google_domain=google.com&gl=us&hl=en&api_key=df76bd9ff6d4d2d580b10d30f077415456812407eb1e66a3124c2e29754a8666'
    # searches = "erotica"
    res = []

    for eng in engines:
        res.append(requests.get(link.format(eng, searches)).json())

    filtered = []

    for r in res:
        if 'organic_results' in r:
            organic_results = r['organic_results']
            for result in organic_results:
                filtered.append({
                    "title": result.get('title'),
                    "link": result.get('link'),
                    "favicon": result.get('favicon'),
                })

    # Extract unique links and corresponding titles using a dictionary
    i=10
    uniqueLinks = {}
    for result in filtered:
        link = result['link']
        if link not in uniqueLinks:
            uniqueLinks[link] = {
                "title": result['title'],
                "favicon": result['favicon'],
            }
        i+=10

    # Convert dictionary to desired JSON format
    json_output = [{"title": details['title'], "link": link, "favicon": details['favicon']} for link, details in uniqueLinks.items()]


    # json_output = {details['index']: {"link":link,"title": details['title'], "favicon": details['favicon']} for link, details in uniqueLinks.items()}

    # return json_output



    return json_output


# AIzaSyDJuY7-IpeQYUDcc1iQiABHx-DHvoa1lJU
