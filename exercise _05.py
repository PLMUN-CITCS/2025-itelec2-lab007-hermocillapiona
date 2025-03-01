user_number = float(input("Enter a number to perform operations on: "))
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3
import math # Import math module (only need to do this once at the top in a real script)
sqrt_value = math.sqrt(user_number) if user_number >= 0 else "Undefined for negative numbers"
sine_value = math.sin(math.radians(user_number))  # Assuming user enters an angle in degrees
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

