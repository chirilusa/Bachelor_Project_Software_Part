import csv
import datetime

with open('weather.csv','r') as csvinput:
    with open('final_weather.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Place')
        all.append(row)

        for row in reader:
            tokens = row[1].split("-")
            dt = datetime.date(int(tokens[0]), int(tokens[1]), int(tokens[2]))

            hour_minute = row[2].split(":")
            t = datetime.time(int(hour_minute[0]), int(hour_minute[1]))

            # december - february
            if dt.month <= 2 or dt.month == 12:
                # sunday
                if dt.isoweekday() == 7:
                    if t.hour >= 8 and t.hour <= 20:
                        row.append("ski resort")
                    else:
                        row.append("home")
                        
                # saturday
                elif dt.isoweekday() == 6:
                    if t.hour >= 9 and t.hour <= 16:
                        row.append("shopping mall")
                    else:
                        row.append("home")
                
                # monday to friday
                else:
                    if t.hour >= 8 and t.hour <= 17:
                        row.append("office")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("gym")
                    else:
                        row.append("home")

            # march to may
            if dt.month >= 3 and dt.month <= 5:
                # sunday
                if dt.isoweekday() == 7:
                    if t.hour >= 10 and t.hour <= 13:
                        row.append("park")
                    elif t.hour >= 18 and t.hour <= 21:
                        row.append("restaurant")
                    else:
                        row.append("home")
                        
                # saturday
                elif dt.isoweekday() == 6:
                    if t.hour >= 10 and t.hour <= 16:
                        row.append("shopping mall")
                    elif t.hour >= 20 and t.hour <= 1:
                        row.append("party")
                    else:
                        row.append("home")
                
                # monday to friday
                else:
                    if t.hour >= 9 and t.hour <= 18:
                        row.append("office")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("gym")
                    else:
                        row.append("home")

            # june 
            if dt.month == 6:
                # sunday
                if dt.isoweekday() == 7:
                    if t.hour >= 10 and t.hour <= 13:
                        row.append("park")
                    elif t.hour >= 18 and t.hour <= 21:
                        row.append("party")
                    else:
                        row.append("home")
                        
                # saturday
                elif dt.isoweekday() == 6:
                    if t.hour >= 10 and t.hour <= 16:
                        row.append("shopping mall")
                    elif t.hour >= 20 and t.hour <= 23:
                        row.append("restaurant")
                    else:
                        row.append("home")
                
                # monday to friday
                else:
                    if t.hour >= 9 and t.hour <= 18:
                        row.append("office")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("gym")
                    else:
                        row.append("home")

            # july - august
            if dt.month == 7 or dt.month == 8:
                # sunday
                if dt.isoweekday() == 7:
                    if t.hour >= 10 and t.hour <= 18:
                        row.append("beach")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("restaurant")
                    else:
                        row.append("home")
                        
                # saturday
                elif dt.isoweekday() == 6:
                    if t.hour >= 10 and t.hour <= 18:
                        row.append("beach")
                    elif t.hour >= 20 and t.hour <= 1:
                        row.append("party")
                    else:
                        row.append("home")
                
                # monday to friday
                else:
                    if t.hour >= 9 and t.hour <= 18:
                        row.append("office")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("gym")
                    else:
                        row.append("home")

            # september to november
            if dt.month >= 9 and dt.month <= 11:
                # sunday
                if dt.isoweekday() == 7:
                    if t.hour >= 10 and t.hour <= 14:
                        row.append("park")
                    elif t.hour >= 19 and t.hour <= 21:
                        row.append("restaurant")
                    else:
                        row.append("home")
                        
                # saturday
                elif dt.isoweekday() == 6:
                    if t.hour >= 11 and t.hour <= 18:
                        row.append("shopping mall")
                    elif t.hour >= 21 and t.hour <= 2:
                        row.append("party")
                    else:
                        row.append("home")
                
                # monday to friday
                else:
                    if t.hour >= 10 and t.hour <= 19:
                        row.append("office")
                    elif t.hour >= 20 and t.hour <= 21:
                        row.append("gym")
                    else:
                        row.append("home")
            
            
            all.append(row)

        writer.writerows(all)