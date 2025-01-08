# could probably make this cleaner by changing the letters
# inserted as the pattern repeats itself just with different
# letters.

'''
CHALLENGE
The challenge is to implement a function which returns a Roman numeral string when passed a number.
'''

def roman_numeral_encoder(num):

    roman_string = ''
    if num >= 10:
        digit = int(str(num)[-2])
        match digit:
            case 1:
                roman_string += 'X'
            case 2:
                roman_string += 'XX'
            case 3:
                roman_string += 'XXX'
            case 4:
                roman_string += 'XL'
            case 5:
                roman_string += 'L'
            case 6:
                roman_string += 'LX'
            case 7:
                roman_string += 'LXX'
            case 8:
                roman_string += 'LXXX'
            case 9:
                roman_string += 'XC'
            case 0:
                roman_string += ''

    last_digit = int(str(num)[-1])
    match last_digit:
        case 1:
            roman_string += 'I'
        case 2:
            roman_string += 'II'
        case 3:
            roman_string += 'III'
        case 4:
            roman_string += 'IV'
        case 5:
            roman_string += 'V'
        case 6:
            roman_string += 'VI'
        case 7:
            roman_string += 'VII'
        case 8:
            roman_string += 'VIII'
        case 9:
            roman_string += 'IX'
        case 0:
            roman_string += ''

    return roman_string

    
        