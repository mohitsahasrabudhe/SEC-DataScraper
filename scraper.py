import pandas as pd
from sec_edgar_downloader import Downloader

x=pd.read_csv(r"/home/mohit/Dropbox/ra_tasks_ms/bailout_firms/Regular Scheduled SEC scraping/companies.csv")
x=x['Column_Name']
dl = Downloader(r"/home/mohit/Dropbox/ra_tasks_ms/bailout_firms/Regular Scheduled SEC scraping")


for i in x:
	dl.get("8-K",i, after_date="20200328")
