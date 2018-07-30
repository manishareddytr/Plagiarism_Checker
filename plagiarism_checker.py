from googleapiclient.discovery import build
import urllib.request
import re

my_api_key = "YOUR_API_KEY"
my_cse_id = "YOUR_CSE_ID"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

with open('ourtext.txt','r') as ourtext:
    ourtext=ourtext.read()

search_string=ourtext    

results = google_search(search_string, my_api_key, my_cse_id, num=10)

links=[]
for result in results:
	links.append(result['link'])

search_string=search_string.split()
size = len(search_string)

count=0
for link in links:
#print(link)   
	try:
	    urllib.request.urlretrieve(link,'webtext.txt')
	except:
	    pass
	with open('webtext.txt','rb') as webtext:
		try:
			webtext = webtext.read().decode(encoding="utf-8")
			webtext = (re.sub('<[^>]*>','',webtext))
			webtext = webtext.split()
			lines_in_common = len([x for x in search_string if x in webtext])
			count = int(lines_in_common) /int( size)
			if count > 0.5:
				print(link+" with percentage "+str(count*100))
			
		except:
			pass	

        

