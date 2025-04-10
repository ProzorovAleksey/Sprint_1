temporary_values = '1h 45m,360s,25m,30m 120s,2h 60s'

result_minutes = 0
for time in temporary_values.replace(',', ' ').split(' '):
    if 'h' in time: 
        result_minutes += int(time[:-1]) * 60 
    elif 'm' in time:
        result_minutes += int(time[:-1]) 
    else:
        result_minutes += int(time[:-1]) // 60

print('Общее количество минут: ' + str(result_minutes))