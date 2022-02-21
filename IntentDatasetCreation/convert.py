import csv
csv_file = '../Keywords/All_Keywords.csv'
txt_file = 'keywords.txt'
with open(txt_file, "w") as output_file:
    with open(csv_file, "r") as input_file:
        reader = csv.reader(input_file)
        next(reader) # Ignore first row
        next(reader) # Ignore second row

        for row in reader:
            output_file.write("".join(row[1])+'\n')
    output_file.close()