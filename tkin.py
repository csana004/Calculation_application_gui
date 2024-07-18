from tkinter import *
import datetime

def get_vals(operation, inputvalue, inputvalue2, output_label):
    try:
        num1 = float(inputvalue.get())
        num2 = float(inputvalue2.get())
        if operation == "addition":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            if num2 == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"
        output_label.config(text=f"Output: {result}")
    except ValueError:
        output_label.config(text="Error: Invalid input")

def get_24hr_clock(output_label):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    output_label.config(text=f"Output: {formatted_time} (24hr)")

def get_12hr_clock(output_label):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%I:%M:%S %p")
    output_label.config(text=f"Output: {formatted_time} (12hr)")

def get_temperature(output_label):
    temp_value_window = Toplevel()
    temp_value_window.title("Temperature Input")
    temp_value_window.geometry("300x200")
    temp_value_window.configure(bg='#f0f0f0')

    Label(temp_value_window, text="Enter temperature value:", bg='#f0f0f0').pack(pady=5)
    temp_value_entry = Entry(temp_value_window)
    temp_value_entry.pack(pady=5)

    Label(temp_value_window, text="Enter current unit (C, F, or K):", bg='#f0f0f0').pack(pady=5)
    temp_unit_entry = Entry(temp_value_window)
    temp_unit_entry.pack(pady=5)

    Label(temp_value_window, text="Enter target unit (C, F, or K):", bg='#f0f0f0').pack(pady=5)
    target_unit_entry = Entry(temp_value_window)
    target_unit_entry.pack(pady=5)

    def get_temp_and_convert():
        try:
            temp_value = float(temp_value_entry.get())
            temp_unit = temp_unit_entry.get().upper()
            target_unit = target_unit_entry.get().upper()
            convert_temperature(temp_value, temp_unit, target_unit, output_label)
            temp_value_window.destroy()
        except ValueError:
            output_label.config(text="Error: Invalid temperature value")

    Button(temp_value_window, text="Submit", command=get_temp_and_convert, bg="#4CAF50", fg="white").pack(pady=10)
    temp_value_window.mainloop()

def convert_temperature(temp_value, temp_unit, target_unit, output_label):
    if temp_unit == target_unit:
        converted_temp = temp_value
    elif temp_unit == "C":
        if target_unit == "F":
            converted_temp = (temp_value * 9 / 5) + 32
        elif target_unit == "K":
            converted_temp = temp_value + 273.15
        else:
            output_label.config(text="Error: Invalid target unit")
            return
    elif temp_unit == "F":
        if target_unit == "C":
            converted_temp = (temp_value - 32) * 5 / 9
        elif target_unit == "K":
            converted_temp = (temp_value - 32) * 5 / 9 + 273.15
        else:
            output_label.config(text="Error: Invalid target unit")
            return
    elif temp_unit == "K":
        if target_unit == "C":
            converted_temp = temp_value - 273.15
        elif target_unit == "F":
            converted_temp = (temp_value - 273.15) * 9 / 5 + 32
        else:
            output_label.config(text="Error: Invalid target unit")
            return
    else:
        output_label.config(text="Error: Invalid temperature unit")
        return
    output_label.config(text=f"Output: {converted_temp} °{target_unit}")

def simple_interest(output_label):
    si_value_window = Toplevel()
    si_value_window.title("Simple Interest Input")
    si_value_window.geometry("300x250")
    si_value_window.configure(bg='#f0f0f0')

    Label(si_value_window, text="Enter principal:", bg='#f0f0f0').pack(pady=5)
    si_principal_entry = Entry(si_value_window)
    si_principal_entry.pack(pady=5)

    Label(si_value_window, text="Enter time in months:", bg='#f0f0f0').pack(pady=5)
    si_time_entry = Entry(si_value_window)
    si_time_entry.pack(pady=5)

    Label(si_value_window, text="Enter rate of interest:", bg='#f0f0f0').pack(pady=5)
    si_rate_entry = Entry(si_value_window)
    si_rate_entry.pack(pady=5)

    def calculate_si():
        try:
            principal = float(si_principal_entry.get())
            time = float(si_time_entry.get())
            rate = float(si_rate_entry.get())
            si = (principal * time * rate) / 100
            amount = si + principal
            output_label.config(text=f"Output: Simple Interest is Rs {si}\nAmount after adding SI is Rs {amount}")
            si_value_window.destroy()
        except ValueError:
            output_label.config(text="Error: Invalid input for SI calculation")

    Button(si_value_window, text="Submit", command=calculate_si, bg="#4CAF50", fg="white").pack(pady=10)
    si_value_window.mainloop()

def compound_interest(output_label):
    ci_value_window = Toplevel()
    ci_value_window.title("Compound Interest Input")
    ci_value_window.geometry("300x300")
    ci_value_window.configure(bg='#f0f0f0')

    Label(ci_value_window, text="Enter principal:", bg='#f0f0f0').pack(pady=5)
    ci_principal_entry = Entry(ci_value_window)
    ci_principal_entry.pack(pady=5)

    Label(ci_value_window, text="Enter time in months:", bg='#f0f0f0').pack(pady=5)
    ci_time_entry = Entry(ci_value_window)
    ci_time_entry.pack(pady=5)

    Label(ci_value_window, text="Enter rate of interest:", bg='#f0f0f0').pack(pady=5)
    ci_rate_entry = Entry(ci_value_window)
    ci_rate_entry.pack(pady=5)

    Label(ci_value_window, text="Enter no. of times interest is compounded per year:", bg='#f0f0f0').pack(pady=5)
    ci_n_entry = Entry(ci_value_window)
    ci_n_entry.pack(pady=5)

    def calculate_ci():
        try:
            principal = float(ci_principal_entry.get())
            time = float(ci_time_entry.get())
            rate = float(ci_rate_entry.get())
            n = float(ci_n_entry.get())
            ci = principal * (1 + rate / (n * 100))**(n * time)
            output_label.config(text=f"Output: Compound Interest is Rs {ci - principal}\nAmount after adding CI is Rs {ci}")
            ci_value_window.destroy()
        except ValueError:
            output_label.config(text="Error: Invalid input for CI calculation")

    Button(ci_value_window, text="Submit", command=calculate_ci, bg="#4CAF50", fg="white").pack(pady=10)
    ci_value_window.mainloop()

def unit_conversion(output_label):
    conversion_window = Toplevel()
    conversion_window.title("Unit Conversion")
    conversion_window.geometry("500x500")
    conversion_window.configure(bg='#f0f0f0')

    Label(conversion_window, text="Choose conversion type:", bg='#f0f0f0').pack(pady=5)
    conversion_type = StringVar(value="Length")

    Radiobutton(conversion_window, text="Length", variable=conversion_type, value="Length", bg='#f0f0f0').pack(anchor=W)
    Radiobutton(conversion_window, text="Weight", variable=conversion_type, value="Weight", bg='#f0f0f0').pack(anchor=W)
    Radiobutton(conversion_window, text="Money", variable=conversion_type, value="Money", bg='#f0f0f0').pack(anchor=W)

    Label(conversion_window, text="Enter value to convert:", bg='#f0f0f0').pack(pady=5)
    value_entry = Entry(conversion_window)
    value_entry.pack(pady=5)

    Label(conversion_window, text="Enter current unit:", bg='#f0f0f0').pack(pady=5)
    current_unit_entry = Entry(conversion_window)
    current_unit_entry.pack(pady=5)

    Label(conversion_window, text="Enter target unit:", bg='#f0f0f0').pack(pady=5)
    target_unit_entry = Entry(conversion_window)
    target_unit_entry.pack(pady=5)

    def convert_units():
        try:
            value = float(value_entry.get())
            current_unit = current_unit_entry.get().upper()
            target_unit = target_unit_entry.get().upper()
            conversion_type_value = conversion_type.get()

            if conversion_type_value == "Length":
                result = convert_length(value, current_unit, target_unit)
            elif conversion_type_value == "Weight":
                result = convert_weight(value, current_unit, target_unit)
            elif conversion_type_value == "Money":
                result = convert_money(value, current_unit, target_unit)
            else:
                result = "Error: Invalid conversion type"

            output_label.config(text=f"Output: {result}")
            conversion_window.destroy()
        except ValueError:
            output_label.config(text="Error: Invalid input for unit conversion")

    Button(conversion_window, text="Submit", command=convert_units, bg="#4CAF50", fg="white").pack(pady=10)
    conversion_window.mainloop()

def convert_length(value, current_unit, target_unit):
    length_units = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "inches": 0.0254,
        "ft": 0.3048,
        "yards": 0.9144,
        "mili inches": 1609.34
    }
    if current_unit in length_units and target_unit in length_units:
        result = value * length_units[target_unit] / length_units[current_unit]
        return f"{value} {current_unit} is {result} {target_unit}"
    else:
        return "Error: Invalid length unit"

def convert_weight(value, current_unit, target_unit):
    weight_units = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    if current_unit in weight_units and target_unit in weight_units:
        result = value * weight_units[target_unit] / weight_units[current_unit]
        return f"{value} {current_unit} is {result} {target_unit}"
    else:
        return "Error: Invalid weight unit"

def convert_money(value, current_unit, target_unit):
    # Note: In a real application, you would use an API to get the latest exchange rates.
    # Here, we use some example rates for demonstration purposes.
    exchange_rates = {
        "USD": 1,
        "EUR": 0.85,
        "GBP": 0.75,
        "INR": 74.57,
        "JPY": 110.62,
        "CNY": 6.45
    }
    if current_unit in exchange_rates and target_unit in exchange_rates:
        result = value * exchange_rates[target_unit] / exchange_rates[current_unit]
        return f"{value} {current_unit} is {result} {target_unit}"
    else:
        return "Error: Invalid currency unit"

root = Tk()
root.title("Calculation Application")
root.geometry("600x700")
root.configure(bg='#e0e0e0')

title_frame = Frame(root, bg="#3E4149", relief=RAISED, bd=2)
title_frame.pack(side=TOP, fill="x")
title_label = Label(title_frame, text="Calculation Application", bg="#3E4149", fg="white", font=("Helvetica", 16))
title_label.pack(pady=10)

input_frame = Frame(root, bg="#f0f0f0", bd=2, relief=SUNKEN)
input_frame.pack(pady=10, padx=10, fill="x")

Label(input_frame, text="Input the first value:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
inputvalue = DoubleVar()
Entry(input_frame, textvariable=inputvalue, font=("Helvetica", 12)).grid(row=0, column=1, padx=5, pady=5)

Label(input_frame, text="Input the second value:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
inputvalue2 = DoubleVar()
Entry(input_frame, textvariable=inputvalue2, font=("Helvetica", 12)).grid(row=1, column=1, padx=5, pady=5)

output_frame = Frame(root, bg="#f0f0f0", bd=2, relief=SUNKEN)
output_frame.pack(pady=10, padx=10, fill="x")

output_label = Label(output_frame, text="", bg="#f0f0f0", font=("Helvetica", 12))
output_label.pack(pady=10)

button_frame = Frame(root, bg="#e0e0e0")
button_frame.pack(pady=10)

button_options = [
    ("Addition", lambda: get_vals("addition", inputvalue, inputvalue2, output_label)),
    ("Subtract", lambda: get_vals("subtract", inputvalue, inputvalue2, output_label)),
    ("Multiply", lambda: get_vals("multiply", inputvalue, inputvalue2, output_label)),
    ("Division", lambda: get_vals("division", inputvalue, inputvalue2, output_label)),
    ("24hr Clock", lambda: get_24hr_clock(output_label)),
    ("12hr Clock", lambda: get_12hr_clock(output_label)),
    ("Temperature", lambda: get_temperature(output_label)),
    ("Simple Interest", lambda: simple_interest(output_label)),
    ("Compound Interest", lambda: compound_interest(output_label)),
    ("Unit Conversion", lambda: unit_conversion(output_label)),
]

for text, command in button_options:
    Button(button_frame, text=text, command=command, bg="#4CAF50", fg="white", width=20, font=("Helvetica", 12)).pack(pady=5)

root.mainloop()




