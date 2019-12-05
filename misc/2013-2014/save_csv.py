import csv

base_file = 'source/{}.txt'
base_csv = 'fortune500-{}.csv'


def process_year(year):
    assert year in (2013, 2014)
    data = []
    filename = base_file.format(year)
    with open(filename, 'r') as f:
        for line in f.read().splitlines():
            rank, company_chinese, revenue, profit = line.split('\t')
            # print(rank, company_chinese, revenue, profit)
            idx = company_chinese.find('(')
            company_english = company_chinese[idx + 1:-1]
            data.append([rank, company_english, revenue, profit])
    assert len(data) == 500
    return data


def save_as_csv(year, data):
    filename = base_csv.format(year)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['rank', 'company', 'revenue ($ millions)', 'profit ($ millions)'])
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    for year in (2013, 2014):
        data = process_year(year)
        save_as_csv(year, data)

