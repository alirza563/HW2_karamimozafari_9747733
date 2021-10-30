import urllib.request
sites = [{"name": "stackoverflow.com", "link": "https://stackoverflow.com/"},
         {"name": "wikipedia.org", "link": "https://www.wikipedia.org/"},
         {"name": "w3schools.com", "link": "https://www.w3schools.com/"},
         {"name": "downloadly.ir", "link": "https://downloadly.ir/"},
         {"name": "soft98.com", "link": "https://soft98.ir/"},
         {"name": "whatsapp.com", "link": "https://www.whatsapp.com/"},
         {"name": "el.yazd.ac.ir", "link": "https://el.yazd.ac.ir/"},
         {"name": "geeksforgeeks.org", "link": "https://www.geeksforgeeks.org/"},
         ]

for site in sites:
    html_res = urllib.request.urlopen(site["link"])
    html_content = html_res.read()
    path = "serverFile/" + site["name"] + ".html"
    try:
        file = open(path, 'w')
        file.write(html_content.decode())
    except UnicodeEncodeError:
        file = open(path, 'w', encoding='UTF-8')
        file.write(html_content.decode())
    file.close()