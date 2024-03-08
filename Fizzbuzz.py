# FizzBuzz challenge 3/8/2024, INFOTC 4320, Devon Landry
def fizzbuzz():
    for num in range(1, 101):  # Iterate over numbers from 1 to 100
        if num % 3 == 0 and num % 5 == 0:  # Check if number is divisible by both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Check if number is divisible by 3
            print("Fizz")
        elif num % 5 == 0:  # Check if number is divisible by 5
            print("Buzz")
        else:
            print(num)  # If none of the above conditions are met, print the number itself

fizzbuzz()  # Call the fizzbuzz function to execute the FizzBuzz logic
