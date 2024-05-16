import requests
import json 
x = input('''
Enter Your Country Code from below:-
ae: United Arab Emirates
ar: Argentina
at: Austria
au: Australia
be: Belgium
bg: Bulgaria
br: Brazil
ca: Canada
ch: Switzerland
cn: China
co: Colombia
cu: Cuba
cz: Czech Republic
de: Germany
eg: Egypt
fr: France
gb: United Kingdom
gr: Greece
hk: Hong Kong
hu: Hungary
id: Indonesia
ie: Ireland
il: Israel
in: India
it: Italy
jp: Japan
kr: South Korea
lt: Lithuania
lv: Latvia
ma: Morocco
mx: Mexico
my: Malaysia
ng: Nigeria
nl: Netherlands
no: Norway
nz: New Zealand
ph: Philippines
pl: Poland
pt: Portugal
ro: Romania
rs: Serbia
ru: Russia
sa: Saudi Arabia
se: Sweden
sg: Singapore
si: Slovenia
sk: Slovakia
th: Thailand
tr: Turkey
tw: Taiwan
ua: Ukraine
us: United States
ve: Venezuela
za: South Africa 
All Countries (default just press enter)
-------------->   ''')
y = input('''
Enter Any 1 Genre of News from below:-
1)Business
2)Entertainment
3)General
4)Health
5)Science
6)Sports
7)Technology
8)All Genres (default just press enter)
-------------->   ''')
print('')
print("--------------------------------------------")
url = "https://newsapi.org/v2/top-headlines"
params = {
    "apiKey": "5abfc8a453da45fcb746bd5ebb53c789",
    "country": "in",
    "category": y
}

response = requests.get(url, params=params)
data = response.json()

if "articles" in data:
    for article in data["articles"]:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print()
        print("--------------------------------------------")
else:
    print("No articles found.")
