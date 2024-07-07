#step 1
#go to letterboxd
#go to a wishlist
#list all entries on first page

#step 2
#get the data-film-name and display that in cmd instead of entire div/class

import time, requests, bs4

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Boxer:

    def __init__(self) -> None:
        pass

    def get_watchlist(self, user):

        base_url = "https://letterboxd.com"
        url = "/".join([base_url ,user,"watchlist/"])
        res = requests.get(url)

        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(options)
        browser.get(url)
        time.sleep(0.4)
        source = browser.page_source
        
        if res.status_code >= 400:
            return None

        watchlist_page = bs4.BeautifulSoup(source, 'lxml')
        titles = []

        first_page_list = watchlist_page.find_all("li", class_= "poster-container")

        if len(first_page_list) < 1:
            return None

        for title in first_page_list:

            title_details = {'Title': title.a.text}

            title_url = title.div['data-film-link']
            title_url = "".join([base_url, title_url])
            title_details['url'] = title_url

            title_details['image'] = title.img['src']

            titles.append(title_details)

        pages = watchlist_page.find_all("li", class_="paginate-page")
        if not pages: 
            return titles

        last_page = int(pages[-1].get_text())

        for page in range(2,last_page + 1):
            
            current_page = ''.join([url,"page/",str(page)])
            browser.get(current_page)
            time.sleep(0.4)
            source = browser.page_source
            watchlist_page = bs4.BeautifulSoup(source, 'lxml')

            current_page_list = watchlist_page.find_all("li", class_="poster-container")

            for title in current_page_list:
                title_details = {'Title': title.a.text}

                title_url = title.div['data-film-link']
                title_url = "".join([base_url, title_url])
                title_details['url'] = title_url

                title_details['image'] = title.img['src']


                titles.append(title_details)
       
        browser.quit()
        return titles

    def find_intersection(self, list1, list2):
        
        intersection = [first_title for first_title in list1 if any(second_title['Title'] == first_title["Title"] for second_title in list2)]
        
        return intersection

if __name__ == "__main__":
    first_user = input("Enter first username: ")
    second_user = input("Enter second username: ")

    boxer = Boxer()

    first_user_list = boxer.get_watchlist(first_user)
    second_user_list = boxer.get_watchlist(second_user)


    neither_seen = boxer.find_intersection(first_user_list, second_user_list)

    print("Neither of you has seen:\n")

    for movie in neither_seen:
        print(f"{movie['Title']} \n")