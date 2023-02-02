import requests, bs4 ,re,yaml,time

url =["https://indd.adobe.com/view/ae869ae4-0d87-408f-b5ab-2920c9414921"]


def tag_urls(form_tag):
    if len(form_tag) >0:
        tag_urls= {url['href'] for url in form_tag}
        for tag_url in tag_urls:
            print(f"------>url in form: {tag_url}")
        

def checker(url):
    form_url = f"https://indd.adobe.com/view/publication/{url.split('/')[-1]}/1/publication.html"
    r = requests.get(form_url)

    form_soup = bs4.BeautifulSoup(r.content,'html.parser')
    print(f"Url: {url}")
    print(f'----> form_url: {form_url}')

    form_atags = form_soup.find_all('a')
    form_areatags=form_soup.find_all('area')
    tag_urls(form_atags)
    tag_urls(form_areatags)

for u in url:
    checker(u)
    print('====================================')
    time.sleep(1)