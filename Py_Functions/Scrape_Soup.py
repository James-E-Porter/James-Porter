def scrape_url(url):
     import csv
     from bs4 import BeautifulSoup
     import requests

     #make the request
     res = requests.get(url)
     html_page = res.content
     #parse the html using bs4
     soup = BeautifulSoup(html_page, 'html.parser')
     #find all the table data
     table_data = soup.find_all('td')
     #create an empty list to store the data
     data = []

     #loop through the table data and store it in the list
     for td in table_data:
         data.append(td.text)

     #open a csv file
     with open('scraped_data.csv', 'w') as f:
         writer = csv.writer(f)
         #write the data to the csv file
         writer.writerow(data)

#call the function
scrape_url('http://example.com')
