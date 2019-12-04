# Fortune 500 company lists (1955-2019)

## Usage
The dataset is under the `csv/` directory.

> The Fortune 500 is an annual list compiled and published by [Fortune](https://en.wikipedia.org/wiki/Fortune_(magazine)) magazine that ranks 500 of the largest United States corporations by total revenue for their respective fiscal years.

## How is this dataset collected?
The data come from a variety of sources, as I failed to find a single complete dataset that contains all lists from 1955 to 2018.

## 2019-
I'll be manually updating them.
- 2019: https://fortune.com/fortune500/2019/search/


## 2015-2018
http://fortune.com/fortune500/2015/list only loads the top 20 companies. More rows can be loaded by scrolling down to page bottom.

1. On the webpage, open [Developer Tools](https://developers.google.com/web/tools/chrome-devtools/).
2. Scroll to page bottom to load the next 30 companies (ranked 21 through 50).
3. In the **Network** panel, you can find a request whose type is [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).
4. Right click on the request to reveal link `http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/20/30`
5. After inspecting, we find that `/20/30` means **skip 20 and take 30**, equivalent to getting row 21 through row 50.
6. It seems this API gives at most 100 rows per call. So, we can access `http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/0/100` to get the first 100 companies, and `http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/100/100` to get the next 100, and so on.
7. Finally, use the Python `json` package to parse the JSON files, and build the CSV files.

Data source:
- homepage for 2015: http://fortune.com/fortune500/2015/list
- 1-100: http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/0/100
- 101-200: http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/100/100
- 201-300: http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/200/100
- 301-400: http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/300/100
- 401-500: http://fortune.com/api/v2/list/1141696/expand/item/ranking/asc/400/100


## 2013-2014
The data are from [FortuneChina.com](http://www.FortuneChina.com), the official website of Fortune magazine for China.

Data source: 
```Python3
url_2013 = 'http://www.fortunechina.com/fortune500/c/2013-05/06/content_154796.htm'
url_2014 = 'http://www.fortunechina.com/fortune500/c/2014-06/02/content_207496.htm'
```

## 2006-2012
The data are scrapped manually from the sources below, because the HTML pages containing 2006-2012 data do not follow a uniform structure.

Data source:
```Python3
base = 'https://money.cnn.com/magazines/fortune/fortune500/{}/full_list/{}.html'
pages = ('index', '101_200', '201_300', '301_400', '401_500')
urls = [base.format(year, page) for year in range(2006,2013) for page in pages]
```

## 1955-2005
HTML sources are downloaded using `urllib`, parsed using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and saved as CSV. 

Data source:
```Python3
base = 'https://money.cnn.com/magazines/fortune/fortune500_archive/full/{}/{}.html'
urls = [base.format(year, page) for year in range(1955,2006) for page in (1,101,201,301,401)]
```

