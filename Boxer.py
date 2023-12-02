#step 1
#go to letterboxd
#go to a wishlist
#list all entries on first page

#step 2
#get the data-film-name and display that in cmd instead of entire div/class

import time, webbrowser, requests, bs4, os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Boxer:

    def __init__(self) -> None:
        pass

    def get_watchlist(self, user):

        url = "/".join(["https://letterboxd.com/",user,"watchlist/"])
        res = requests.get(url)
        watchlist_page = bs4.BeautifulSoup(res.text, 'html.parser')

        titles = []

        first_page_list = watchlist_page.find_all("div", class_= "film-poster")

        for title in first_page_list:
            title_details = {'Title': title.img['alt']}

            titles.append(title_details)


        last_page = int(watchlist_page.find_all("li", class_="paginate-page")[-1].get_text())

        for page in range(2,last_page + 1):
            current_page = '/'.join([url,"page",str(page)])
            res = requests.get(current_page)
            watchlist_page = bs4.BeautifulSoup(res.text, 'html.parser')

            current_page_list = watchlist_page.find_all("div", class_="film-poster")

            for title in current_page_list:
                title_details = {'Title': title.img['alt']}

                titles.append(title_details)
        return titles

    def find_intersection(self, list1, list2):
        
        intersection = [first_title['Title'] for first_title in list1 if any(second_title['Title'] == first_title["Title"] for second_title in list2)]
        

        '''
        for title in list1:
            print(title['Title'])
        '''
        
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
        print(f"{movie} \n")