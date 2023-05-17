import csv
import re

with open('../datasets/weather.csv','r') as csvinput:
    with open('../datasets/weather_rain_condition.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Rain')
        all.append(row)
        for row in reader:
            if re.search("rain", row[4], re.IGNORECASE):
                row.append(1)
            else:
                row.append(0)
         
            all.append(row)

        writer.writerows(all)