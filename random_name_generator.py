#!/usr/bin/env python3

import bs4
import sys
import requests

def get_page():
    name_page = "https://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=no&usage_fntsy=1"
    return (requests.get(name_page).text)

def parse_name(page):
    page_tree = bs4.BeautifulSoup(page, "html.parser")
    return (page_tree.find_all("p")[0].text.strip())

def main():
    for i in range(int(sys.argv[1])):
        print (parse_name(get_page()))

if __name__ == '__main__':
    main()
