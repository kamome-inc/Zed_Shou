roman = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))


def to_roman(n):
    result = '{} = '.format(n)

    a = n//1000
    n = n % 1000
    b = n//100
    n = n % 100
    c = n//10
    d = n % 10

    result += 'M'*a
    if b == 9:
        result += 'CM'
    elif b < 9 and b > 4:
        result += 'D' + 'C'*(b-5)
    elif b == 4:
        result += 'CD'
    else:
        result += 'C'*b
    return result


def from_roman(n):
    sum = 0
    skip = False
    for i in range(len(n)-1):
        if skip:
            skip = False
            continue
        if roman[n[i]] < roman[n[i+1]]:
            sum += roman[n[i+1]] - roman[n[i]]
            skip = True
            print('A{} sum = {}, ni = {}'.format(i, sum, roman[n[i]]))
        else:
            sum += roman[n[i]]
            print('B{} sum = {}, ni = {}'.format(i, sum, roman[n[i]]))
    if not skip:
        sum += roman[n[len(n)-1]]
    return sum


print(to_roman(1434))
