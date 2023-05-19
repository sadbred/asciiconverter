import tkinter as tk
import ctypes
import os
import webbrowser

def text_to_numbers(text):
    numbers = [str(ord(char)) for char in text]
    return ' '.join(numbers)

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

def option1():
    input_text = input("Enter the text: ")
    result = text_to_numbers(input_text)
    print("Result:", result)
    input("Task completed. Press Enter to exit...")

def option2():
    numbers = input("Enter the numbers separated by spaces: ")
    result = convert_numbers_to_ascii(numbers)
    print("ASCII text:", result)
    input("Task completed. Press Enter to exit...")
    
    

def option3():
    webbrowser.open("https://www.discord.gg/KAwB5feU7u")

def minimize_window():
    # Minimize the window
    window.iconify()

def unminimize_window():
    # Unminimize the window
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 9)

# Create the main window
window = tk.Tk()
window.title("ASCII Converter")
window.geometry("550x400")  # Set a fixed size for the window (width x height)
window.configure(bg="black")  # Set the background color to black

# Create a frame for buttons and align it to the left
button_frame = tk.Frame(window, bg="black")
button_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create buttons with custom colors and text color
button1 = tk.Button(button_frame, text="ASCII to Number", command=option1, bg="gray", fg="white")
button1.pack(pady=10, anchor=tk.W)

button2 = tk.Button(button_frame, text="Number to ASCII", command=option2, bg="gray", fg="white")
button2.pack(pady=10, anchor=tk.W)

button3 = tk.Button(button_frame, text="Discord!", command=option3, bg="gray", fg="white")
button3.pack(pady=10, anchor=tk.W)

minimize_button = tk.Button(window, text="Minimize", command=minimize_window, bg="gray", fg="white")
minimize_button.pack(pady=10)

unminimize_button = tk.Button(window, text="Unminimize", command=unminimize_window, bg="gray", fg="white")
unminimize_button.pack(pady=10)

# Start the main loop
window.mainloop()
