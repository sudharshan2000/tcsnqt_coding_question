index = 1
sum1 = 0
sum2 = 0
sum3 = 0
while(index <= 9):
    x = int(input())
    if x >= 1 and x <= 100:
        if index % 3 == 1:
            sum1 += x
        elif index % 3 == 2:
            sum2 += x
        else:
            sum3 += x
        index += 1
    else:
        print('INVALID INPUT')

avg1 = round(sum1 / 3)
avg2 = round(sum2 / 3)
avg3 = round(sum3 / 3)

if avg1 <= 70 and avg2 <= 70 and avg3 <= 70:
    print('All trainees are unfit')
else:
    if (avg1 >= avg2 and avg1 >= avg3):
        print('Trainee Number: 1')
    if (avg2 >= avg1 and avg2 >= avg3):
        print('Trainee Number: 2')
    if avg3 >= avg1 and avg3 >= avg2:
        print('Trainee Number: 3')
