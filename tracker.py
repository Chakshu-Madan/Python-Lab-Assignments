import datetime
import os
#-----------------------------------------------------------
#Name: Chakshu Madan
#Date: 
#Title: Building a Calorie Tracking Console App
#Course: Programming for Problem Solving using Python
#-----------------------------------------------------------

def welcome_message():
    """Prints a welcome message and introduction to the tool."""
    print("=" * 40)
    print("✨WELCOME TO THE DAILY CALORIE TRACKER CLI✨")
    print("=" * 40)
    print("This simple tool helps you log your meals, track your total calorie intake,")
    print("and compare it against your daily limit.")
    print("Let's get started!\n")
    
def run_tracker():
    #Initialize lists to store our data
    meal_names = []
    calorie_amount = []
    
    #User's daily limit
    daily_limit = 0
    
    #Input and Data Collection
    try: 
        num_meals = int(input("How many meals did you eat today?"))
        if num_meals < 1:
            print("You must enter atleast one meal. Exiting.")
            return
        print("\nPlease enter the details for each meal.")
        for i in range(num_meals):
            print(f"\n---Meal {i + 1}---")
            meal = input("Enter meal name (e.g. Breakfast, Lunch etc)")
            meal_names.append(meal)         #Store the meal name in the list
            while True:
                try:
                    calories_input = input("Enter calorie amount")
                    calories = float(calories_input)
                    if calories < 0:
                        print("Calorie amount cannot e negative. Try again.")
                        continue
                    calorie_amount.append(calories)       #Store the calorie amount in the list
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for calories")
    except ValueError:
        print("\nInvalid input for the number of meals. Please run the program again.")
        return
    print("\nMeal and calorie data successfully collected! Proceeding to calculations.")

    # Calorie Calculations & Limit input
    total_calories = sum(calorie_amount)
    average_calories = total_calories/len(meal_names)
    while True:
        try:
            daily_limit = float(input("What is your daily calorie limit (in kcal)?"))
            if daily_limit < 100:
                print("Limit seems too low. Please enter a realistic limit.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for the limit.")
            
    #Exceed Limit Warning System
    limit_msg = ""
    if total_calories > daily_limit:
        limit_msg = f"⚠️❗ WARNING! You are {total_calories-daily_limit:.2f} kcal over your daily limit of {daily_limit}"
    else:
        limit_msg = f"✅️ Success! You are within your limit. You have {daily_limit-total_calories:.2f} kcal remaining."
    print("\n"+"="*40)
    print("CALORIE TRACKER REPORT")
    print("="*40)
    
    #Neatly Formatted Output
    print("Meal Name\tCalories(kcal)")              #Table Header
    print("-"*30)
    for meal,calories in zip(meal_names,calorie_amount):
        print(f"{meal:<15}\t{calories:.2f}")
    print("-"*30)
    print(f"TOTAL:\t\t{total_calories:.2f} kcal")
    print(f"AVERAGE:\t{average_calories:.2f} kcal")
    print("-"*30)
    print(limit_msg)
    print("\n"+"="*40)
    
    #Save Session Log to File
    save_option = input("Do you want to save this session log to a file? (y/n):").lower()
    if save_option == 'y':
        base_filename = "calorie_log"
        extension = ".txt"
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y%m%d_%H%M%S")
        filename = base_filename + extension            #Start with calorie_log.txt
        counter = 1
        while os.path.exists(filename):
            filename = f"{base_filename}{counter}{extension}"
            counter += 1  
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"---Calorie Log Session:{current_time.strftime('%Y-%m-%d %H:%M:%S')}---\n\n")
                file.write("Meal Name\tCalories (kcal)\n")
                file.write("-"*30 + "\n")
                for meal, calories in zip(meal_names, calorie_amount):
                    file.write(f"{meal:<15}\t{calories:.2f}\n")
                file.write("-"*30 + "\n")
                file.write(f"DAILY LIMIT:\t{daily_limit:.2f} kcal\n")
                file.write(f"TOTAL INTAKE:\t{total_calories:.2f} kcal\n\n")
                file.write(f"STATUS: {limit_msg}\n")
                print(f"\nSuccessfully saved session log to: {filename}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
    else:
        print("\nSession log not saved")
    print("\n" + "Stay fit😉👋")

#Calling the function 
if __name__ == "__main__":
    welcome_message()
    run_tracker()

        
    
    