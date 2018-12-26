import json
import csv

base_file = 'json/{}-{}.json'
base_csv = 'output/fortune500-{}.csv'


def process_year(year):
    data = []

    assert year in (2015, 2016, 2017, 2018)
    OFFSET = (-1 if year == 2017 else 0)
    for page in (0, 100, 200, 300, 400):
        f = open(base_file.format(year, page))
        j = json.loads(f.read())
        items = j['list-items']
        assert (len(items) == 100)

        for i in range(100):
            item = items[i]
            company = item['title']
            assert item['highlights'][1 + OFFSET]['field']['title'] == 'Revenues ($M)'
            revenue = item['highlights'][1 + OFFSET]['value']
            assert item['highlights'][3 + OFFSET]['field']['title'] == 'Profits ($M)'
            profit = item['highlights'][3 + OFFSET]['value']
            rank = i + page + 1
            # print(rank, company, revenue, profit)
            data.append([rank, company, revenue, profit]) # save data
    return data


def save_as_csv(year, data):
    filename = base_csv.format(year)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['rank', 'company', 'revenue ($ millions)', 'profit ($ millions)'])
        for row in data:
            writer.writerow(row)


for year in (2015, 2016, 2017, 2018):
    data = process_year(year)
    save_as_csv(year, data)


