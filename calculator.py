
# Custom function to read the two numbers.
def read_numbers():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    return num1, num2

# Simple menu.
print('Welcome to the calculator!')
print('Please choose an operation:')
print('    1. Addition')
print('    2. Subtraction')
print('    3. Multiplication')
print('    4. Division')
print('    5. Exit')

def main():
    
    # Main loop.
    while True:
        
        choice = input('\nEnter your choice (1-5): ')

        match choice:
            case '1':
                num1, num2 = read_numbers()
                result = num1 + num2
                print(f'Result: {result}')
            
            case '2':
                num1, num2 = read_numbers()
                result = num1 - num2
                print(f'Result: {result}')
            
            case '3':
                num1, num2 = read_numbers()
                result = num1 * num2
                print(f'Result: {result}')
            
            case '4':
                try:
                    num1, num2 = read_numbers()
                    result = num1 / num2
                    print(f'Result: {result}')
                
                except ZeroDivisionError:
                    print("Error: division by zero")
            
            case '5':
                break
            
            case _:
                print('Invalid Input')

if __name__ == "__main__":
    main()