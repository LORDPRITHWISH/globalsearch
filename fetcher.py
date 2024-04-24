import requests
import json

link='https://serpapi.com/search.json?engine={}&q={}&google_domain=google.com&gl=us&hl=en&api_key=df76bd9ff6d4d2d580b10d30f077415456812407eb1e66a3124c2e29754a8666'


engines = ["google","duckduckgo","bing"]
searches = "erotica"


    res=[]

    for eng in engines :
        res.append(requests.get(link.format(eng,searches)).json())

    filtred=[]
    sets=[]


    for r in res:
        print("\n"*5)
        if 'organic_results' in r:
            # Extracting the organic results
            organic_results = r['organic_results']
            
            # Now, you can iterate through each organic result and access specific fields
            for result in organic_results:
                # Example: Extracting and printing the title and link of each result

                filtred.append({
                    "Title": result.get('title'),
                    "Link": result.get('link'),
                    
                })





# filtred = list(set(sorted(filtred, key=lambda x: x.get('Link'))))

# filtred = list({tuple(sorted(d.items(), key=lambda item: item[0])): d for d in filtred}.values())



# print(*filtred,sep="\n\n")



