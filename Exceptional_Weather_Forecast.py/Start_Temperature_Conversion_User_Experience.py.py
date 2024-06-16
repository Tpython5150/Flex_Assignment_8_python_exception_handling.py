'''
Exceptional Weather Forecast 1 task 1-Start, 2-Temperature Conversion, 3-User Experience

Objective: The aim of this assignment is to enance your understanding of exeption handling by creating a weather 
           forecast appplication that gracefully handles unexpected user input and provides userfriendly error
           messages.

'''
def farenheit_to_celcius(farenheit):
    return (farenheit - 32) * 5/9
while True: 
        try: 
            farenheit = float(input("Please enter the temperature in farenheit: "))
            celcius = farenheit_to_celcius(farenheit)
            print(f"{farenheit:.2f} Farenheit is eqivalent to {celcius:.2f} Celcius.")
        except ValueError:
            print("Invalid input. Please provide a numerical value.")
        except ZeroDivisionError:
            print("Error: Division by zero occured during division.")
        else: 
            print(f"{celcius:.2f}")
            break
        finally:
            print("Thank you for usng our weather forcast application!")



