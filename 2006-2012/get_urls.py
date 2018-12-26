base = 'https://money.cnn.com/magazines/fortune/fortune500/{}/full_list/{}.html'
pages = ('index', '101_200', '201_300', '301_400', '401_500')
urls = [base.format(year, page) for year in range(2006,2013) for page in pages]

for url in urls:
    print(url)

