import tkinter as tk
from tkinter import ttk
from main import addition, substraction, multiplication, division

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Calculator state variables
current_input = ""
first_operand = None
operation = None
new_operand_started = True

# Create the display
display_entry = tk.Entry(root, state='readonly', width=18, font=('Arial', 20), justify='right')

# Helper function to update the display
def update_display(value):
    display_entry.config(state='normal')
    display_entry.delete(0, tk.END)
    display_entry.insert(0, str(value))
    display_entry.config(state='readonly')

# Event handler for digit and decimal buttons
def on_digit_click(digit):
    global current_input, new_operand_started
    if new_operand_started:
        current_input = ""
        new_operand_started = False
    
    if digit == "." and "." in current_input:
        return
    
    current_input += str(digit)
    update_display(current_input)

# Core calculation logic
def calculate_result():
    global first_operand, operation, current_input, new_operand_started
    if first_operand is None or operation is None or current_input == "":
        return None
    
    try:
        second_operand = float(current_input)
        result = 0
        if operation == "+":
            result = addition(first_operand, second_operand)
        elif operation == "-":
            result = substraction(first_operand, second_operand)
        elif operation == "*":
            result = multiplication(first_operand, second_operand)
        elif operation == "/":
            if second_operand == 0:
                update_display("Error")
                current_input = ""
                first_operand = None
                operation = None
                new_operand_started = True
                return None
            result = division(first_operand, second_operand)
        
        # Format result to remove trailing .0 for integers
        if result == int(result):
            result = int(result)
        return result
    except ValueError:
        update_display("Error")
        current_input = ""
        first_operand = None
        operation = None
        new_operand_started = True
        return None
    except Exception: # Catch any other calculation error
        update_display("Error")
        current_input = ""
        first_operand = None
        operation = None
        new_operand_started = True
        return None

# Event handler for operation buttons
def on_operation_click(op):
    global first_operand, operation, current_input, new_operand_started
    
    if current_input == "Error": # If previous state was error, reset for new operation
        on_clear_click() # Reset most state
        # current_input will be empty, so it won't try to parse "Error" as first_operand

    if current_input: # Only proceed if there's a current input
        try:
            current_value = float(current_input)
            if first_operand is None:
                first_operand = current_value
            else: # Chained operation
                if operation: # Ensure an operation was set
                    # Calculate previous result before setting new operation
                    result = calculate_result() # This uses first_operand, operation, and current_input (as second_operand)
                    if result is not None:
                        first_operand = result
                        update_display(first_operand)
                    else: # Error during calculation
                        # Error already displayed by calculate_result, state reset there
                        return 
                # else: if no operation, current_input becomes first_operand (handled by first_operand is None block or if current_input is not empty)
                    # This scenario (e.g. 5 = 3 +) might need more thought, but current logic:
                    # if first_operand is set, and op is clicked, it uses current_input as second_operand
                    # if first_operand is not set, it sets first_operand = current_value
            
        except ValueError: # current_input might be empty if user clicks op, then another op
            if first_operand is None: # e.g. user clicks "+", then "-"
                # Do nothing or perhaps store the latest operation
                operation = op
                new_operand_started = True
                return
            # if first_operand is not None, and current_input is empty (e.g. 5 + -), we just update operation
            # pass
    # else: current_input is empty. If first_operand is set, we just update the operation. If not, do nothing.

    operation = op
    new_operand_started = True # Ready for the next operand

# Event handler for equals button
def on_equals_click():
    global first_operand, operation, current_input, new_operand_started
    
    if first_operand is None or operation is None or current_input == "" or current_input == "Error":
        # Not enough info to calculate or already in error state
        return

    result = calculate_result()
    if result is not None:
        update_display(result)
        current_input = str(result)
        first_operand = None # Reset for next independent calculation
        operation = None     # Reset for next independent calculation
    # else, error was handled and displayed by calculate_result

    new_operand_started = True

# Event handler for clear button
def on_clear_click():
    global current_input, first_operand, operation, new_operand_started
    current_input = ""
    first_operand = None
    operation = None
    update_display("0")
    new_operand_started = True
display_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)

# Button properties
button_font = ('Arial', 18)
button_width = 4 # width in text units
button_height = 2 # height in text units
# Using padx/pady on grid cells for spacing might be better than relying on button height/width for overall layout consistency.
grid_padx = 5
grid_pady = 5

# Create GUI buttons
# Row 1
btn_7 = tk.Button(root, text="7", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("7"))
btn_8 = tk.Button(root, text="8", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("8"))
btn_9 = tk.Button(root, text="9", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("9"))
btn_divide = tk.Button(root, text="/", font=button_font, width=button_width, height=button_height, command=lambda: on_operation_click("/"))

btn_7.grid(row=1, column=0, padx=grid_padx, pady=grid_pady)
btn_8.grid(row=1, column=1, padx=grid_padx, pady=grid_pady)
btn_9.grid(row=1, column=2, padx=grid_padx, pady=grid_pady)
btn_divide.grid(row=1, column=3, padx=grid_padx, pady=grid_pady)

# Row 2
btn_4 = tk.Button(root, text="4", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("4"))
btn_5 = tk.Button(root, text="5", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("5"))
btn_6 = tk.Button(root, text="6", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("6"))
btn_multiply = tk.Button(root, text="*", font=button_font, width=button_width, height=button_height, command=lambda: on_operation_click("*"))

btn_4.grid(row=2, column=0, padx=grid_padx, pady=grid_pady)
btn_5.grid(row=2, column=1, padx=grid_padx, pady=grid_pady)
btn_6.grid(row=2, column=2, padx=grid_padx, pady=grid_pady)
btn_multiply.grid(row=2, column=3, padx=grid_padx, pady=grid_pady)

# Row 3
btn_1 = tk.Button(root, text="1", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("1"))
btn_2 = tk.Button(root, text="2", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("2"))
btn_3 = tk.Button(root, text="3", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("3"))
btn_subtract = tk.Button(root, text="-", font=button_font, width=button_width, height=button_height, command=lambda: on_operation_click("-"))

btn_1.grid(row=3, column=0, padx=grid_padx, pady=grid_pady)
btn_2.grid(row=3, column=1, padx=grid_padx, pady=grid_pady)
btn_3.grid(row=3, column=2, padx=grid_padx, pady=grid_pady)
btn_subtract.grid(row=3, column=3, padx=grid_padx, pady=grid_pady)

# Row 4
btn_clear = tk.Button(root, text="C", font=button_font, width=button_width, height=button_height, command=on_clear_click)
btn_0 = tk.Button(root, text="0", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("0"))
btn_decimal = tk.Button(root, text=".", font=button_font, width=button_width, height=button_height, command=lambda: on_digit_click("."))
btn_add = tk.Button(root, text="+", font=button_font, width=button_width, height=button_height, command=lambda: on_operation_click("+"))

btn_clear.grid(row=4, column=0, padx=grid_padx, pady=grid_pady)
btn_0.grid(row=4, column=1, padx=grid_padx, pady=grid_pady)
btn_decimal.grid(row=4, column=2, padx=grid_padx, pady=grid_pady)
btn_add.grid(row=4, column=3, padx=grid_padx, pady=grid_pady)

# Row 5
btn_equals = tk.Button(root, text="=", font=button_font, width=button_width, height=button_height, command=on_equals_click)
btn_equals.grid(row=5, column=0, columnspan=4, padx=grid_padx, pady=grid_pady, sticky="ew")

# Note: No mainloop() or if __name__ == "__main__": block as per instructions.
# Initial display
update_display("0")

if __name__ == "__main__":
    root.mainloop()
