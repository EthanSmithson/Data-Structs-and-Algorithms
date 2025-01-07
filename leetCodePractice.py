def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    count = 0

    for i in s:
        print(i)
        if i in numerals:
            print(numerals[i])
            count += numerals[i]
            
    print(count)

romanToInt("IV")