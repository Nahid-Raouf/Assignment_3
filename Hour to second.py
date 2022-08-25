S = int(input('Select : 1.hours to seconds 2.seconds to hours'))

if S == 1:
    while True:
        hour = int(input('hours: '))
        minutes = int(input('minutes: '))
        second = int(input('seconds: '))
        if (hour < 24) and (minutes < 60) and (second < 60):
            hour = hour * 3600
            minutes = minutes * 60
            sum = hour + minutes + second
            print(sum, "seconds")
            break           
        else:
            print('Error! (0 <= hour < 24),(0 <= minutes < 60),(0 <= second , 60)')
            continue

elif S == 2:
    while True:
        second = int(input('seconds: '))
        if second <= 86400 :
            minutes = int(second / 60)
            if minutes >= 60:
               hour = int(minutes / 60)
            new_minutes = int(minutes % 60)
            new_second = int(second % 60)
            print('hours:' ,hour, 'minutes:' ,new_minutes, 'seconds:' ,new_second)
            break
        else:
            print(' number should be less than 86400!')
            continue