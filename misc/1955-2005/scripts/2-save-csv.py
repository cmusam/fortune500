from bs4 import BeautifulSoup
import csv

base_file = '../html/fortune500-{}-{}.html'
base_csv = '../csv/fortune500-{}.csv'


def process_year(year):
    assert 1955 <= year <= 2005
    data = []
    for part in (1, 101, 201, 301, 401):
        filename = base_file.format(year, part)
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f, 'lxml')
            table = soup.find('table', {'class': 'maglisttable'})
            rows = table.find_all('tr')
            for i in range(100):
                rank, company, revenue, profit = [x.text for x in rows[1+i].find_all('td')]
                revenue = revenue.replace(',', '')  # remove comma separator
                profit = profit.replace(',', '')  # remove comma separator
                data.append([rank, company, revenue, profit])  # save data
    assert len(data) == 500
    return data


def save_as_csv(year, data):
    filename = base_csv.format(year)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['rank', 'company', 'revenue ($ millions)', 'profit ($ millions)'])
        for row in data:
            writer.writerow(row)


for year in range(1955, 2006):
    data = process_year(year)
    save_as_csv(year, data)

