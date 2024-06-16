'''
The Recipe Ratio Adjuster 2 Task 1

Objectve: The aim of this assignment is to create a program tat adjustmthe quantities of a recipe based on 
          the number of servings, handling any type of arithmatice errors or user input exceptions.

Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.


Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.
'''
while True:  
    try:
        original_servings = float(input("How many servings orginally asked for: "))
        desired_servings = float(input("How many servings are you going to make: "))
        actual_servings = desired_servings / original_servings
        print(f"Original servings asked for: {desired_servings}")
        print(f"Desired servings added: {desired_servings}")
    except ValueError:
        print("Invalid input. You must enter a numerical value.")
    except ZeroDivisionError:
        print("Can't divide by zero. Please correct by making values above zero.")
    else:
        print(f"Actual Servings: {actual_servings}")
        break
    finally:
        print("I encourage you to enjoy cooking. Regardless its worth the challenge.")
        

   