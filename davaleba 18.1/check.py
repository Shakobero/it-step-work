def positive_check(func):
    def wrapper(num):
        if num < 0:
            raise ValueError("Number must be positive")
        else:
            return func(num)
    return wrapper

@positive_check
def return_number(num):
    return num

while True:
    try:
        user_input = int(input("Enter a number: "))
        result = return_number(user_input)
        print("Result:", result)
        break  
    except ValueError as e:
        print("Error:", e)
