import sys

two_digit_number = input('Enter a number >>> ')  # Taking the number as input in string format.

def findSum(number):
    '''
  You can find the sum of the digits by running a for loop taking each element one by one and summing them up and returning it.
    '''
    sum = 0
    for num in number:
        if not num.isdigit():
           print('The number you entered is not a number it contains characters other then 0-9 also.')
           sys.exit()
        num = int(num)
        sum += num
    return sum

sum = findSum(two_digit_number)
print(sum)
