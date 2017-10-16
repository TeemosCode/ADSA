from bs4 import BeautifulSoup
import requests
# Opening a file to store all the links
file = open("cnet_dump.txt",'w+')
for i in range(1,10):
    #loop to ru.n through x no of pages of the website
    url2= requests.get("https://www.cnet.com/news/"+str(i))
    # Traersing throguh multiple pages o the website
    soup = BeautifulSoup(url2.content,'html.parser')
    links=[]
    # Finding all the a tags - for links on the current page
    for link in soup.find_all('a'):
        # print(link)
        # print(link.get("href"))
        links.append(link.get('href'))
        # Grabbing all the links from the page
    sample12='/news'
    for i in range(len(links)):
        # Checking for keywors in the linka rray and then  
        # writing it on thefile
        if sample12 in str(links[i]) and len(links[i])>20:
            file.write(links[i]+"\n")
file.close()