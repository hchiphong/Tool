import requests, bs4 ,re,yaml,time

url =["https://ncv.microsoft.com/Xw8xsgwd0u","https://ncv.microsoft.com/Xcux5dUtEB","https://ncv.microsoft.com/B6lpTPoffl"]


def tag_urls(form_tag):
    if len(form_tag) >0:
        for tag in form_tag:
            print(f"------>url in form: {tag['href']}")
        

def checker(url):
    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.content,'html.parser')
    data =''
    for script in soup.find_all('script'):
        if 'prefetchFormUrl:' in script.text:
            data=script
    print(f"Url: {url}")
    script_data=data.text.strip()[30:-1]
    goodJson = re.sub( r'\n\s*(\S+)\s*:', r'\n"\1":', script_data )
    good_script_data = yaml.full_load(goodJson)
    prefetchPageUrl = good_script_data['prefetchFormUrl']
    print(f'--> Redirected URL: {r.url}')
    print(f'----> form_url: {prefetchPageUrl}')

    form_page = requests.get(prefetchPageUrl)
    form_soup = bs4.BeautifulSoup(form_page.content,'html.parser')
    form_atags = form_soup.find_all('a')
    form_areatags=form_soup.find_all('area')
    tag_urls(form_atags)
    tag_urls(form_areatags)

for u in url:
    checker(u)
    print('====================================')
    time.sleep(1)