import csv
import re

with open('final_weather.csv', 'r') as weather:
    with open('clothes_recommendation.csv', 'r') as clothes:
        with open('final_dataset.csv', 'w') as final:
            writer = csv.writer(final, lineterminator='\n')
            w_reader = csv.reader(weather)
            c_reader = csv.reader(clothes)

            all = []
            row = next(w_reader)
            row.append('Clothes')
            all.append(row)

            for w_row in w_reader:
                clothes.seek(1)
                for c_row in c_reader:
                    # If weather condition contains clothes condition
                    if re.search(c_row[0], w_row[4], re.IGNORECASE):
                        # Weather place is the same with clothes place
                        if w_row[8] == c_row[1]:
                            interval = list(map(int, c_row[2].split(":")))
                            wt = float(w_row[3])
                            # Weather temperature between condition interval temperature
                            if interval[0] <= wt and wt <= interval[1]:
                                w_row.append(c_row[3])
                                break
                
                all.append(w_row)

            writer.writerows(all)
                            
                            

                
                


