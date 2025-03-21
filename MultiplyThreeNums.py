# MultiplyThreeNums.py

def multiply_three_numbers(a, b, c):
    return a * b * c

if __name__ == '__main__':
    try:
        a = float(input("Input your first number: "))
        b = float(input("Input your second number: "))
        c = float(input("Input your third number: "))

       
        result = multiply_three_numbers(a, b, c)
        print("The result is:", result)
    except ValueError:
        print("Error，place input your number！")
