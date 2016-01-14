import csv

with open("test.csv", 'rU') as input, open('test-a.csv', 'wb') as output:  #if csv.Error: new-line character seen in unquoted field - do you need to open the file in universal-newline mode? try rU else rb
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    all = []
    row = next(reader)
    row.insert(0, 'ID')
    all.append(row)
    for k, row in enumerate(reader):
        all.append([str(k+1)] + row)
    writer.writerows(all)
