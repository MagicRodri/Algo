def toRoman(s: str) -> int:

    """
        This function converts an given roman string number to integer
    """
    result = 0
    roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    if len(s) <= 0:
        return 0
    elif len(s) == 1:
        result = roman[s[0]]
    else:
        if roman[s[0]] < roman[s[1]]:
            result += roman[s[1]] - roman[s[0]] + toRoman(s[2:])
        else:
            result += roman[s[0]] + toRoman(s[1:])

    return result

def romanToInt(num: int) -> str:
    ...


TestCase = [
    {'input':'','output':0},
    {'input':'III','output':3},
    {'input':'XIV','output':14}
]

for test in TestCase:
    if toRoman(test['input']) != test['output']:
        print('Test failed')
        break
else:
    print('Test passed')


