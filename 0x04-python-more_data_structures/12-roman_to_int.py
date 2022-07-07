#!/usr/bin/python3

def roman_to_int(roman_string):
    val = 0
    car = {
        "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }
    lst = ["X", "V", "L", "C", "D", "M"]
    st = sorted(car)
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if len(roman_string) > 1:
        for i, x in enumerate(roman_string):
            if roman_string[i] in lst:
                if i == 0:
                    val += car.get(roman_string[i])
                else:
                    if roman_string[i - 1] == 'I':
                        val -= car.get(roman_string[i - 1])
                        val += car.get(roman_string[i - 1] + roman_string[i])
                    else:
                        val += car.get(roman_string[i])
            else:
                val += car.get(roman_string[i])
    else:
        val += car.get(roman_string)
    return val
