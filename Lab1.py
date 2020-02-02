def binarify(num):
    #convert positive integer to base 2
    digits=[]
    while True:
        if num%2==0:
            digits.append("0")
            num=num//2
        elif num<=0:
            return "0"
        else:
            digits.append("1")
            num=num//2
        if num==0:
            return "".join(digits[::-1])

def int_to_base(num,base):
    #convert positive integer to a string in any base
    digits=[]
    while True:
        if num%base==0:
            digits.append("0")
            num=num//base
        elif num<=0:
            return "0"
        else:
            digits.append(str(num%base))
            num=num//base
        if num==0:
            return "".join(digits[::-1])
        
def base_to_int(string, base):
    #take a string-formatted number and its base and return the base-10 integer
    string=string[::-1]
    result=0
    for i in range(len(string)):
        result=base**i*int(string[i])+result
    return result


def flexibase_add(str1, str2, base1, base2):
    #add two numbers of different bases and return the sum
    str1=str1[::-1]
    result1=0
    for i in range(len(str1)):
        result1=base1**i*int(str1[i])+result1
    
    str2=str2[::-1]
    result2=0
    for i in range(len(str2)):
        result2=base2**i*int(str2[i])+result2
    tmp=result1+result2
    result=int_to_base(tmp, base1)
    return result

def flexibase_multiply(str1, str2, base1, base2):
    #multiply two numbers of different bases and return the product
    str1=str1[::-1]
    result1=0
    for i in range(len(str1)):
        result1=base1**i*int(str1[i])+result1
    str2=str2[::-1]
    result2=0
    for i in range(len(str2)):
        result2=base2**i*int(str2[i])+result2
    tmp=result1*result2
    result = int_to_base(tmp, base1)
    return result

def romanify(num):
    #given an integer, return the Roman numeral version
    if num > 3999:
            raise ValueError('Values over 3999 are not allowed: {}'.format(num))
    if num < 0:
            raise ValueError('Negative values are not allowed: {}'.format(num))
    to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM', 0:""}
    first=num%10
    second=(num-first)%100
    third=(num-second-first)%1000
    forth=(num-third-second-first)
    roman=to_roman[forth]+to_roman[third]+to_roman[second]+to_roman[first]
    return roman
    
