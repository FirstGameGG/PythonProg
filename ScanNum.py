def calculate_digit_sum(number):
    return sum(int(digit) for digit in number if digit.isdigit())

def find_numbers_with_sum(file_path, target_sum):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if calculate_digit_sum(line) == target_sum:
                print(line)

file_path = r'C:\Users\iamfi\OneDrive\Downloads\Num.txt'  # Replace with the actual file path
target_sum = 51  # Replace with your desired target sum

find_numbers_with_sum(file_path, target_sum)
