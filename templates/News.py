import requests
from bs4 import BeautifulSoup

res1 = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?next=27690906&n=31')
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links1 = soup1.select('.title')
subtext1 = soup1.select('.subtext')
links2 = soup2.select('.title')
subtext2 = soup2.select('.subtext')

big_sub = subtext1 + subtext2
big_link = links1 + links2

print(big_sub, big_link)



def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
				with open('data_info.csv','w', newline='') as my_file:
					hn2 = str(hn)
					my_file.writelines(hn2)

create_custom_hn(big_link, big_sub)







