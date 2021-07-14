def two_numbers(my_numbers, target_sum):
    output = []
    for x in range(0, len(my_numbers) - 1):
        attempt_a = my_numbers[x]
        for y in range(x + 1, len(my_numbers)):
            attempt_b = my_numbers[y]
            sum = attempt_a + attempt_b
            if sum == target_sum:
                output.append([attempt_a, attempt_b])
                print(output)


if __name__ == "__main__":
    two_numbers([6, 5, -4, 8, 11, 1, -1, 6], 10)
