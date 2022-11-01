from datetime import datetime

date = datetime.now()
day = datetime.today().strftime('%A')
hour = date.hour + round(date.minute/60,2) + round(date.second/3600,2)

if day != 'Sunday' or day != 'Saturday':
    if hour > 19:
        print("Ya es hora de ir a casa")
    else:
        resto = round(abs(hour - 19),2)
        print(f'Faltan {resto} hs para ir a casa')
else:
    print("En este día no trabajas")
