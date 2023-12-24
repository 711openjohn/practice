# 2 Questions
# Max 40 mins for 1st Que
# Max 60 mins for 1st Que

# Question 1

# Given 2 non-negative integers in a binary representation as a string - return sum of them in a binary representation and discard intial zeros (if any)

# Question 2

# Given 2 non-negative double numbers first representing price of product (pp) bought by customer and second representing cash given by customer. Cashier has (100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01) as bills. Return bills returned to customer as a comma separated string. String has to be alphabetically sorted.

# example :
# input : pp: 230.0, cash: 500.0
# output: Fifty,One Hundred,One Hunded,Twenty


arr = [
    ["ONE HUNDRED", 100.00],
    ["FIFTY", 50.00],
    ["TWENTY", 20.00],
    ["TEN", 10.00],
    ["FIVE", 5.00],
    ["ONE", 1.00],
    ["HALF DOLLAR", 0.5],
    ["QUARTER", 0.25],
    ["DIME", 0.1],
    ["NICKEL", 0.05],
    ["PENNY", 0.01],
]


pp = 230
cash = 500


n = cash - pp

result = {}
for coinString in arr:
    repr, coin = coinString
    if coin > n:
        continue
    
    r = n // coin
    if r > 0:
        result[repr] = r
        n = n % coin
    else:
        continue

print(result)
