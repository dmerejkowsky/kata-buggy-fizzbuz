def fizz_buzz(number):
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    if number % 15 == 0:
        return "fizzbuzz"
    return str(number)
