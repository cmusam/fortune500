from urllib.request import urlopen
from multiprocessing import Pool
import datetime

base_url = 'https://money.cnn.com/magazines/fortune/fortune500_archive/full/{}/{}.html'
base_file = '../html/fortune500-{}-{}.html'


def download_list(year):
    """
    Download 5 HTML files for the given year's Fortune 500 list.
    The files include 1-100, 101-200, 201-300, 301-400 and 401-500 ranked companies respectively.
    The files are saved to directory ../html/
    """
    assert 1955 <= year <= 2005
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print('[{}] Downloading data for year {}...'.format(timestamp, year))

    for start in (1, 101, 201, 301, 401):
        url = base_url.format(year, start)
        filename = base_file.format(year, start)

        html = urlopen(url).read().decode('utf-8')  # download HTML
        with open(filename, 'w') as f:
            f.write(html)


# Use the multiprocessing package to download each year's data in parallel
years = range(1955, 2006)
p = Pool(len(years))
p.map(download_list, years)

