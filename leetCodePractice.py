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
   
    temp1 = ""
    sum = 0
    count = 0
    if len(s) == 1:
        sum = numerals[s]
    for v in s:
        print(numerals[v])
        if count > 0:
            if numerals[temp1] < numerals[v]:
                val = numerals[v] - numerals[temp1]
                sum += val
                temp1 = ""
            else:
                val = numerals[temp1]
                sum += val
        # if count == len(s)-1:
        #     endVal = numerals[temp1]
        #     sum += endVal
        count += 1
        temp1 = v
    return sum
 
print(romanToInt("VI"))