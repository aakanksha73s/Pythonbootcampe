def main():
    # Example 1: Basic while loop
    print("Example 1: Counting with while loop")
    count = 0
    while count < 5:
        print(count)
        count += 1
    print()

    # Example 2: Summing numbers
    print("Example 2: Summing numbers from 1 to 10")
    number = 1
    total_sum = 0
    while number <= 10:
        total_sum += number
        number += 1
    print(f"Sum of numbers from 1 to 10 is: {total_sum}")
    print()

    # Example 3: User input loop
    print("Example 3: Loop with user input")
    user_input = None
    print("Enter numbers to sum. Enter 0 to finish.")
    while user_input != 0:
        user_input = int(input("Enter a number: "))
        if user_input != 0:
            print(f"You entered: {user_input}")
    print("Loop terminated.")
    print()

    # Example 4: While loop with break
    print("Example 4: Loop with break statement")
    count = 0
    while True:  # Infinite loop
        print(count)
        count += 1
        if count >= 5:
            break
    print("Loop ended.")
    print()

    # Example 5: Infinite loop with manual exit
    print("Example 5: Infinite loop with manual exit")
    while True:
        response = input("Type 'exit' to quit: ")
        if response == 'exit':
            print("Exiting loop.")
            break
        print(f"You typed: {response}")

if __name__ == "__main__":
    main()