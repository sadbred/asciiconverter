import os

def convert_numbers_to_ascii(numbers):
    ascii_chars = []
    number_list = numbers.split()

    for num in number_list:
        try:
            ascii_char = chr(int(num))
            ascii_chars.append(ascii_char)
        except ValueError:
            pass

    ascii_text = ''.join(ascii_chars)
    return ascii_text

numbers = input("Enter the numbers separated by spaces: ")
result = convert_numbers_to_ascii(numbers)
print("ASCII text:", result)

input("Press Enter to clear the screen...")
os.system('cls' if os.name == 'nt' else 'clear')
input("Task completed. Press Enter to exit...")
