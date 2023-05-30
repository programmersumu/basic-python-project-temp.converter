def temperature_converter():
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

    if unit.upper() == "C":
        converted_temperature = (temperature * 9/5) + 32
        print("Converted temperature:", converted_temperature, "F")
    elif unit.upper() == "F":
        converted_temperature = (temperature - 32) * 5/9
        print("Converted temperature:", converted_temperature, "C")
    else:
        print("Invalid unit!")

temperature_converter()
