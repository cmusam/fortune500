import csv

base_a = 'fortune500-{}.csv.bak'
base_b = 'fortune500-{}.csv'


def remove_comma(year):
    """
    Given the CSV file for the particular year, remove comma separators
    in the revenue and profit columns. Also, remove stock symbols in the
    company name column (which is only applicable to 2006).
    """

    filename_a = base_a.format(year)  # in-file
    filename_b = base_b.format(year)  # out-file

    data = []
    with open(filename_a, 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            data.append(row)

    assert len(data)==501  # first row is header

    with open(filename_b, 'w') as f2:
        writer = csv.writer(f2)
        writer.writerow(data[0])
        for row in data[1:]:
            row[2] = row[2].replace(',', '')  # revenue numbers: remove comma separator
            row[3] = row[3].replace(',', '')  # profit numbers: remove comma separator

            # remove trailing stock symbol
            if row[1].count('('):
                assert row[1][-1] == ')'
                idx = row[1].find('(')
                assert row[1][idx-1] in ('\xa0', ' ')  # \xa0 is space for latin1 encoding
                row[1] = row[1][:idx-1]  # remove trailing stock symbol
                # print(row)
            writer.writerow(row)


if __name__ == '__main__':
    for year in range(2006, 2013):
        remove_comma(year)


