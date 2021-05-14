import sys
from bs4 import BeautifulSoup
import csv

filename = sys.argv[1]

def get_html_content(filename):
    with open(filename, 'r') as html_file:
        content = html_file.read()
        return content

def parse_html(content):
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    title = soup.find('h1').text.strip()
    author = soup.find('h2').text.strip()
    highlights_html_tags = soup.find_all('p')
    write_to_file(title, author, highlights_html_tags)

def write_to_file(title, author, highlights):
    
    with open('temp.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        for hl in highlights:
            if len(hl.text.strip()) != 0:
                csvwriter.writerow([hl.text.strip().encode('utf-8'), title.encode('utf-8'), author.encode('utf-8')])

def main():
    content = get_html_content(filename)
    parse_html(content)    

main()