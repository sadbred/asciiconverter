def text_to_numbers(text):
    numbers = [str(ord(char)) for char in text]
    return ' '.join(numbers)

# Example usage
input_text = input("Enter the text: ")
result = text_to_numbers(input_text)
print("Result:", result)
