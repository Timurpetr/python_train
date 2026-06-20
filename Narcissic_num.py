def narcissistic( value ):
    digits = [int(i) for i in str(value)]
    length = len(digits)
    if value % 1 == 0 and sum(d ** length for d in digits) == value:
        return True
    return False

print(narcissistic(20))
