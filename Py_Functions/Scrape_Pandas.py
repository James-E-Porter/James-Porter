import pandas as pd

def scrape_url(url):
    df = pd.read_html(url)[0]
    df.to_csv('output.csv', index=False)

scrape_url('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')
