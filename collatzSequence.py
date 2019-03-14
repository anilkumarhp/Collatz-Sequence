# function to find collatz sequence of a number.
def collatz(number):
    if number % 2 == 0:
        eve = number // 2
        print (eve)
        return eve
    else:
        odd = 3 * number + 1;
        print (odd)
        return odd


# Ask user to enter a integer value.
while True:
    try:
        num = int(input("Enter an integer value greater than 1: "))
        break
    except ValueError: # if entered value is not an integer.
        print("Please only integer(number) value")


# repeat until function returns 1
while num != 1:
    num = int(collatz(num))


