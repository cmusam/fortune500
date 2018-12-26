# Historical Fortune 500 company lists
The dataset can be found under the `csv/` directory.

The lists are collected from a variety of sources, because I failed to find a complete dataset that contains all lists from 1955 to 2018. The methods and sources are described below.

## 1955-2005
HTML sources are downloaded using `urllib`, parsed using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and saved as CSV. 

Data source (given as Python code):
```Python3
base = 'https://money.cnn.com/magazines/fortune/fortune500_archive/full/{}/{}.html'
urls = [base.format(year, page) for year in range(1955,2006) for page in (1,101,201,301,401)]
```

## 2006-2012

Data source:
```Python3
base = 'https://money.cnn.com/magazines/fortune/fortune500/{}/full_list/{}.html'
pages = ('index', '101_200', '201_300', '301_400', '401_500')
urls = [base.format(year, page) for year in range(2006,2013) for page in pages]
```
