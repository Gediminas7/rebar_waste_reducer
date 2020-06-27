
def leftovers_dic(leftfile):
    import csv
    with open(leftfile) as file:
        leftovers = dict()
        reader = csv.reader(file)
        count = 0
        for row in reader:
            row = row[0].split(';')
            if count > 0:
                leftovers[row[0]] = (row[1], row[2], row[3])
            count += 1
    return leftovers

