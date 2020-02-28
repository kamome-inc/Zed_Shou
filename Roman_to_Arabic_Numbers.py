class RomanNumerals(object):
    roman = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))
    arabian = dict(zip([1, 5, 10, 50, 100, 500, 1000], ['I', 'V', 'X', 'L', 'C', 'D', 'M']))


    def digit_to_roman(number, digit):
        i = 1 * digit
        v = 5 * digit
        x = 10 * digit
        if number == 9:
            res = RomanNumerals.arabian[i] + RomanNumerals.arabian[x]
        elif 9 > number > 4:
            res = RomanNumerals.arabian[v] + RomanNumerals.arabian[i] * (number - 5)
        elif number == 4:
            res = RomanNumerals.arabian[i] + RomanNumerals.arabian[v]
        else:
            res = RomanNumerals.arabian[i] * number
        return res

    def to_roman(n):
        a = n // 1000
        n = n % 1000
        b = n // 100
        n = n % 100
        c = n // 10
        d = n % 10

        result = 'M' * a

        result += RomanNumerals.digit_to_roman(b, 100)
        result += RomanNumerals.digit_to_roman(c, 10)
        result += RomanNumerals.digit_to_roman(d, 1)

        return result

    def from_roman(n):
        sum = 0
        skip = False
        for i in range(len(n) - 1):
            if skip:
                skip = False
                continue
            if RomanNumerals.roman[n[i]] < RomanNumerals.roman[n[i + 1]]:
                sum += RomanNumerals.roman[n[i + 1]] - RomanNumerals.roman[n[i]]
                skip = True
            else:
                sum += RomanNumerals.roman[n[i]]
        if not skip:
            sum += RomanNumerals.roman[n[len(n) - 1]]
        return sum


print(RomanNumerals.to_roman(1000))
print(RomanNumerals.from_roman('M'))




