#!/usr/bin/env python2

# how many letters are used if the numbers 1 to 1000 are written out
# eg:
# 1->5: one two three four five = 3 + 3 + 5 + 4 + 4 = 19
#
# ignore spaces and hyphens. Use 'and' between hundreds and tens

def convert_int_to_string(n):
    """Return string representation of integer n

    Only handles numbers from 1 to 1000"""
    remainder_string = ""
    if n > 1000:
        raise ValueError
    if n == 1000:
        return "one thousand"
    if n > 99:
        hundreds, remainder = n/100, n%100
        if remainder:
            remainder_string = " and " + convert_int_to_string(remainder)
        return convert_int_to_string(hundreds) + " hundred" + remainder_string
    if n > 19:
        tens, remainder = n/10, n%10
        if remainder:
            remainder_string = "-" + convert_int_to_string(remainder)
        return ["-","-","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"][tens] + remainder_string
    return ["-","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][n]

def length_of_int_strings_below(n):
    "Return total length of int strings below n"
    s = ''.join(convert_int_to_string(i) for i in range(1,n))
    # remove hypens and spaces
    s = s.replace(' ','')
    s = s.replace('-','')
    return len(s)

print length_of_int_strings_below(1001)
