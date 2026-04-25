
# BMI Calculator - Medical Edition

from datetime import date

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def ideal_weight(height):
    return round(22 * (height ** 2), 1)

def daily_calories(weight, height, age, gender):
    if gender == "m":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    return round(bmr, 1)

def save_result(name, age, bmi, category, ideal, calories):
    with open("results.txt", "a") as f:
        f.write(f"Date: {date.today()}\n")
        f.write(f"Name: {name} | Age: {age}\n")
        f.write(f"BMI: {bmi} | Category: {category}\n")
        f.write(f"Ideal Weight: {ideal} kg\n")
        f.write(f"Daily Calories: {calories} kcal\n")
        f.write("-" * 30 + "\n")

def main():
    print("=== BMI Calculator - Medical Edition ===\n")
    name = input("Patient name: ")
    age = int(input("Age: "))
    gender = input("Gender (m/f): ").lower()
    weight = float(input("Weight (kg): "))
    height_cm = float(input("Height (cm): "))
    height = height_cm / 100

    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)
    ideal = ideal_weight(height)
    calories = daily_calories(weight, height, age, gender)

    print(f"\n{'='*35}")
    print(f"Patient: {name} | Age: {age}")
    print(f"BMI: {bmi} → {category}")
    print(f"Ideal Weight: {ideal} kg")
    print(f"Daily Calories Needed: {calories} kcal")
    print(f"{'='*35}")

    save = input("\nSave results? (y/n): ")
    if save == "y":
        save_result(name, age, bmi, category, ideal, calories)
        print("Results saved to results.txt ✓")

main()
