N = 10
k = int(input())
if k <= 0:
    print('INVALID INPUT')
    print('Number of Candies available :',N)
else:
    print('Number of Candies Sold :',k)
    print('Number of Candies available :',N - k)