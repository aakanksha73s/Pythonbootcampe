from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Example usage
birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print(f"You are {age} years old.")