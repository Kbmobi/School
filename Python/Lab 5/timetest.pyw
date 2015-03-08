import datetime

start=raw_input('start time (4 digits): ')
end= raw_input('end time (4 digits): ')
start_dt = datetime.datetime.strptime(start, '%H%M')
end_dt = datetime.datetime.strptime(end, '%H%M')
diff = end_dt - start_dt
diff = str(diff)
diff = diff.strip('-1, day, :00')
diff = diff.split(':')
print diff[0],"Hours, and",diff[1],"Minutes."