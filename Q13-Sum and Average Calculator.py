def q13_sum_average():
    try:
        count   = int(input("How many numbers? "))
        numbers = []

        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        total   = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"\nSum     : {total}")
        print(f"Average : {average:.2f}")
        print(f"Maximum : {maximum}")
        print(f"Minimum : {minimum}")
    except ValueError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Count cannot be zero!")

q13_sum_average()
