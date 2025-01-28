def main():
    # Welcome message
    print("=== Welcome to Time Conversion Application ===")
    print("Press Enter to start...")
    input()

    time_conversion()


def time_conversion():
    # List of valid time units
    valid_units = ['second', 'minute', 'hour']

    # Input initial time unit
    while True:
        initial_unit = input("Enter initial time unit (second/minute/hour): ").lower()
        if initial_unit in valid_units:
            break
        print("Invalid time unit. Please try again.")

    # Input time amount
    while True:
        try:
            amount = float(input("Enter the amount of time: "))
            break
        except ValueError:
            print("Input must be a number. Please try again.")

    # Input target time unit
    while True:
        target_unit = input("Enter target time unit (second/minute/hour): ").lower()
        if target_unit in valid_units:
            break
        print("Invalid time unit. Please try again.")

    # Convert to seconds
    if initial_unit == 'minute':
        seconds = amount * 60
    elif initial_unit == 'hour':
        seconds = amount * 3600
    else:
        seconds = amount

    # Convert from seconds to target unit
    if target_unit == 'minute':
        result = seconds / 60
    elif target_unit == 'hour':
        result = seconds / 3600
    else:
        result = seconds

    # Display result
    print(f"{amount} {initial_unit}(s) = {result} {target_unit}(s)")


# Run the function
if __name__ == "__main__":
    main()