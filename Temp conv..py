def cel_to_fah(cels):
    return (cels * 9 / 5) + 32
def fah_to_cel(fah):
    return (fah - 32) * 5 / 9
def main():
    while True:
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        ch = input("Enter your choice (1/2/3):")

        if ch == '1':
            cel_val = float(input("Enter temperature in Celsius: "))
            fah_val = cel_to_fah(cel_val)
            print(f"{cel_val:.2f} Degrees Celsius is equal to {fah_val:.2f} Degrees Fahrenheit.")
        elif ch == '2':
            fah_val = float(input("Enter temperature in Fahrenheit: "))
            cel_val = fah_to_cel(fah_val)
            print(f"{fah_val:.2f} Degrees Fahrenheit is equal to {cel_val:.2f} Degrees Celsius.")
        elif ch == '3':
            print("Exiting the temperature converter. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please enter a valid input.")
if __name__ == '__main__':
    main()
