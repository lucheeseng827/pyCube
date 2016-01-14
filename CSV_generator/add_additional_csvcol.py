import csv
with open('input.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)

        for row in csv.reader(csvinput):
            if row[0] == "Name":
                writer.writerow(row+["extra_row"])
            else:
                writer.writerow(row+[row[0]])
