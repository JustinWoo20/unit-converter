from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
FONT = ("Arial", 12, "bold")
# Set window
window = Tk()
window.title("Unit Converter")
window.minsize(height=400, width=600)
window.config(padx=100, pady=25)


# Conversion logic dictionary
conversion_functions = {
    "miles_to_km": lambda x: x * 1.609,
    "km_to_miles": lambda x: x / 1.609,
    "c_to_f": lambda x: (x * 9/5) + 32,
    "f_to_c": lambda x: (x - 32) * 5/9,
    "cm_to_feet": lambda x: x / 30.48,
    "feet_to_cm": lambda x: x * 30.48,
    "in_to_cm": lambda x: x * 2.54,
    "cm_to_in": lambda x: x / 2.54,
}

# make labels function
def make_labels_inputs(unit_text1, row, unit_text2, conversion_key):
    #make input field 1
    input_field = Entry(width=25)
    input_field.grid(column=0, row=row, pady=10)
    #make left side unit
    unit_label1 = Label(text=unit_text1, font=FONT)
    unit_label1.grid(column=1, row=row, pady=10)
    #equal sign
    equal_label = Label(text="=")
    equal_label.grid(column=2, row=row, padx=25, pady=10)
    #Output
    output_number = Label(text="0", font=FONT)
    output_number.grid(column=3, row=row)
    #output unit label
    output_label = Label(text=unit_text2, font=FONT)
    output_label.grid(column=4, row=row, pady=10)
    #Convert Button
    convert_button = Button(text="Convert", command=lambda: convert(conversion_key, input_field, output_number))
    convert_button.grid(column=5, row=row, padx=10)

make_labels_inputs(unit_text1="miles", row=0, unit_text2="km", conversion_key="miles_to_km")
make_labels_inputs(unit_text1="km", row=1, unit_text2="miles", conversion_key="km_to_miles")
make_labels_inputs(unit_text1="°C", row=2, unit_text2="°F", conversion_key="c_to_f")
make_labels_inputs(unit_text1="°F", row=3, unit_text2="°C", conversion_key="f_to_c")
make_labels_inputs(unit_text1="cm", row=4, unit_text2="feet", conversion_key="cm_to_feet")
make_labels_inputs(unit_text1="feet", row=5, unit_text2="cm", conversion_key="feet_to_cm")
make_labels_inputs(unit_text1="in", row=6, unit_text2="cm", conversion_key="in_to_cm")
make_labels_inputs(unit_text1="cm", row=7, unit_text2="in", conversion_key="cm_to_in")

#conversion functions
def convert(conversion_key, input_field, output_number):
    try:
        value = float(input_field.get())
        converted = conversion_functions[conversion_key](value)
        output_number.config(text=str(round(converted, 2)))
    except ValueError:
        output_number.config(text="Error")

window.mainloop()