def add(*args):
    if len(args) < 2:
        print("You need at least two numbers to add.")
        return None

    total = sum(args)
    equation = " + ".join(map(str, args))

    print(f'The sum of {equation} = {total}')


def subtract(*args):
    if len(args) < 2:
        print("You need at least two numbers for subtraction.")
        return None

    result = args[0] - sum(args[1:])
    equation = f'{args[0]} - ' + ' - '.join(map(str, args[1:]))
    print(f'The difference between {equation} = {result}')


def multiply(*args):
    if not args:
        print("No numbers provided to multiply.")
        return None

    total = 1
    equation = " * ".join(map(str, args))

    for num in args:
        total *= num

    print(f'The product of {equation} = {total}')


def divide(*args):
    if len(args) < 2:
        print("You need at least two numbers for division.")
        return None

    if any(num == 0 for num in args[1:]):
        print('Division by zero is not possible')
        return None

    quotient = args[0]
    for num in args[1:]:
        quotient /= num

    equation = f'{args[0]} / ' + ' / '.join(map(str, args[1:]))
    print(f'The quotient of {equation} is {quotient:.2f}')


def main():
    print('Welcome to the Simple Calculator')
    while True:
        while True:
            operation = input("Type the required operation in the below format\n"
                              "add\n"
                              "subtract\n"
                              "multiply\n"
                              "divide\n"
                              "exit\n").lower()
            if operation not in ['add', 'subtract', 'multiply', 'divide', 'exit']:
                print('Invalid input, try again')
                continue
            else:
                break
        if operation == 'exit':
            print('Thank you for using this program.')
            return

        numbers = []
        while True:
            num = input("Enter a number (or 'done' to finish): ")

            if num == 'done':
                break

            try:
                num = float(num)
            except ValueError:
                print("Invalid input. Please enter a number or 'done' to finish.")
                continue

            numbers.append(num)

        if not numbers:
            print("No numbers were provided.")
            continue

        if operation == 'add':
            add(*numbers)
        elif operation == 'subtract':
            subtract(*numbers)
        elif operation == 'multiply':
            multiply(*numbers)
        elif operation == 'divide':
            divide(*numbers)


if __name__ == "__main__":
    main()
