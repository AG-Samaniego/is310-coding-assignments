from bs4 import BeautifulSoup
import requests
# if we wanna save to file, use CSV library
import csv

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class ="title><b>The Dourmouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(open("top_100_ebooks.html"), features="html.parser")

# Find the thingie (heading)
top_100_ebooks = soup.find('h2', string="Top 100 EBooks yesterday")

# if the heading is found, iterate thru ebook titles
if top_100_ebooks:
    top_100_titles = top_100_ebooks.find_next('ol')
    """for title in top_100_titles:
        print(title.get_text())"""

else:
    print("Whoops sorry bruh")

# We can use built-in find_all() method to get links from doc
""" links = soup.find_all('a', id='link1')
paragraphs = soup.find_all('p')"""

# iterates thru links soup.find_all() and prints 'href' and text
""" for link in links:
    print(link.get('href'))
    print(link.get_text())  """

""" for paragraph in paragraphs:
    print(paragraph.get_text())
    # .name gets name of the tag
    print(paragraph.name)
    # .attrs gets the attributes
    print(paragraph.attrs) """

""" for paragraph in paragraphs:
    print(paragraph.parent.prettify()) """


response = requests.get("https://www.gutenberg.org/browse/scores/top")
print("Status code:", response.status_code)
print("Headers:",response.headers)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
top_100_ebooks = soup.find(id="books-last1")
list_of_books = top_100_ebooks.find_next('ol').find_all('li')
for book in list_of_books:
    print(book.get_text())

# Getting all the top lists & storing in a dictionary
top_lists = soup.find_all("h2")

data = []
for top_list in top_lists:
    top_list_name = top_list.get_text()
    top_list_items = top_list.find_next('ol').find_all('li')
    for item in top_list_items:
        data.append({"list": top_list_name, "title": item.get_text()})

# List separated by author and books
books = []
authors = []

for top_list in top_lists:
    top_list_name = top_list.get_text()
    top_list_items = top_list.find_next('ol').find_all('li')
    for item in top_list_items:
        if "EBooks" in top_list_name:
            # wanna get the link? get the href attribute of the "a" tag
            books.append({"list": top_list_name, "title": item.get_text(),
"book_link": item.find('a').get('href')})
        else:
            authors.append({"list": top_list_name, "author": item.get_text(),
"author_link": item.find('a').get('href')})

# save your objects into a file
with open('top_100_ebooks.csv', 'w') as file:
    writer = csv.writer(file)
    # write your headers here
    writer.writerow(['top_list', 'book_title', 'book_link'])
    for book in books:
        writer.writerow([book['top_list'], book['book_title'], book['book_link']])

with open('top_100_authors.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['top_list', 'author', 'author_link'])
    for author in authors:
        writer.writerow([author['top_list'], author['author'], author['author_link']])
