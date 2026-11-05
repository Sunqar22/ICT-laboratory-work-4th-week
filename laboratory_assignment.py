import string

def grade_convert():
    """
    Task 1: Grade Converter Using Conditional Operators
    """
    try:
        score = float(input("Enter the numeric grade (0-100): "))
        if 0 <= score <= 100:
            if score >= 90:
                grade = "A"
            elif score >= 75:
                grade = "B"
            elif score >= 60:   
                grade = "C"
            elif score >= 50:
                grade = "D"
            else:
                grade = "F"

            status = "Passed" if grade != "F" else "Failed"
            print(f"Score: {score}, Grade: {grade}, Status: {status}")
        else:
            print("Error: Please enter a valid numeric grade between 0 and 100.")
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")

def playlist_manager():
    """
    Task 2: Playlist Manager Using a Loop
    """
    playlist = []
    while True:
        print("\nPlaylist Manager")
        print("1. Add a song")
        print("2. Remove a song")
        print("3. View playlist")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            song = input("Enter the name of the song to add: ").strip()
            if song in playlist:
                print(f"'{song}' is already in the playlist.")
            else:
                playlist.append(song)
                print(f"'{song}' has been added to the playlist.")

        elif choice == '2':
            song = input("Enter the name of the song to remove: ").strip()
            if song in playlist:
                playlist.remove(song)
                print(f"'{song}' has been removed from the playlist.")
            else:
                print(f"'{song}' is not in the playlist.")

        elif choice == '3':
            if playlist:
                print("Current Playlist:")
                for idx, song in enumerate(playlist, start=1):
                    print(f"{idx}. {song}")
            else:
                print("The playlist is currently empty.")

        elif choice == '4':
            print("Exiting Playlist Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def temperature_conversion():
    """
    Task 3: Temperature Conversion Table Generator
    """
    try:
        step = int(input("Enter a positive step value (between 1 and 50): "))
        if 1 <= step <= 50:
            print("\nTemperature Conversion Table (Celsius to Fahrenheit)")
            print("Celsius\tFahrenheit")
            for celsius in range(0, 101, step):
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}\t{fahrenheit:.2f}")
        else:
            print("Error: Please enter a positive integer between 1 and 50.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for the step value.")

def comprehensions_filtering():
    """
    Task 4: List Comprehensions and Filtering
    """
    words = list(input("Enter a list of words separated by spaces(10 words): ").split())
    filtered_words = [word.upper() for word in words if len(word) > 4]
    print("Original words:", words)
    print("Filtered and uppercased words:", filtered_words)

def inventory():
    """
    Task 5: Inventory Using Dictionaries
    """
    inventory = {}
    while True:
        print("\nInventory Management")
        print("1. Add a new item")
        print("2. View all items")
        print("3. Search for an item by name")
        print("4. Delete an item")
        print("5. Exit the program")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            name = input("Enter the item name: ").strip().lower()
            if name in inventory:
                print(f"Item '{name}' already exists in the inventory.")
            else:
                try:
                    quantity = int(input("Enter the quantity: "))
                    if quantity < 0:
                        print("Error: Quantity cannot be negative.")
                        continue
                    else:
                        inventory[name] = quantity
                        print(f"Item '{name}' with quantity {quantity} has been added to the inventory.")
                except ValueError:
                    print("Error: Invalid quantity. Please enter a valid non-negative integer.")
        elif choice == '2':
            if not inventory:
                print("The inventory is currently empty.")
            else:
                print("Current Inventory:")
                for item, quantity in inventory.items():
                    print(f"Item: {item.capitalize()}, Quantity: {quantity}")
        elif choice == '3':
            name = input("Enter the item name to search: ").strip().lower()
            if name in inventory:
                print(f"Item found: {name}, Quantity: {inventory[name]}")
            else:
                print(f"Item '{name}' not found in the inventory.")
        elif choice == '4':
            name = input("Enter the item name to delete: ").strip().lower()
            if name in inventory:
                del inventory[name]
                print(f"Item '{name}' has been deleted from the inventory.")
            else:
                print(f"Item '{name}' not found in the inventory.")
        elif choice == '5':
            print("Exiting Inventory Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def sorting_displaying():
    """
    Task 6: Sorting and Displaying Data
    """
    products = [
        ("Laptop", 350000),
        ("Mouse", 5000),
        ("Keyboard", 15000),
        ("Monitor", 85000),
        ("Headphones", 25000),
        ("USB Cable", 2500),
    ]

    sorted_products = sorted(products, key=lambda x: x[1], reverse=False)
    print("\nSorted Products (Ascending Price):")
    for product, price in sorted_products:
        print(f"Product: {product}, Price: {price}")

    print(f"The cheapest product is: {sorted_products[0]} and the most expensive product is: {sorted_products[-1]}")

def anagram_checker():
    """
    Task 7: Anagram Checker
    """
    phrase_1 = input("Enter the first phrase or word: ")
    phrase_2 = input("Enter the second phrase or word: ")

    cleaned_phrase_1 = "".join(i.lower() for i in phrase_1 if i.isalnum())
    cleaned_phrase_2 = "".join(i.lower() for i in phrase_2 if i.isalnum())

    if sorted(cleaned_phrase_1) == sorted(cleaned_phrase_2):
        print(f"'{phrase_1}' and '{phrase_2}' are anagrams.")
    else:
        print(f"'{phrase_1}' and '{phrase_2}' are not anagrams.")

def steps_tracker():
    """
    Task 8: Daily Steps Tracker
    """
    steps_list = []
    while True:
        user_input = input("Enter steps (or 'done'): ").strip().lower()
        if user_input == 'done':
            break
        try:
            steps = int(user_input)
            if steps < 0:
                print("Error: Steps cannot be negative. Please enter a valid number.")
                continue
            else:
                steps_list.append(steps)
        except ValueError:
            print("Error: Invalid input. Please enter a non-negative integer or 'done' to finish.")

    if not steps_list:
        print("No steps were entered.")
    else:
        number_of_days = len(steps_list)
        the_average = sum(steps_list) / number_of_days
        max_steps = max(steps_list)
        min_steps = min(steps_list)

        level = {"Low": 0, "Moderate": 0, "Active": 0}
        for steps in steps_list:
            if steps < 5000:
                level["Low"] += 1
            elif 5000 <= steps <= 9999:
                level["Moderate"] += 1
            else:
                level["Active"] += 1

        print(f"\nTotal days recorded: {number_of_days}")
        print(f"Average steps per day: {the_average:.2f}")
        print(f"Highest steps in a day: {max_steps}")
        print(f"Lowest steps in a day: {min_steps}") 
        print(f"Days with Low activity: {level['Low']}")
        print(f"Days with Moderate activity: {level['Moderate']}")
        print(f"Days with Active activity: {level['Active']}")

def word_length():
    """"
    Task 9: Word Length Analyzer
    """
    text = input("Enter a sentence or a short text: ")

    cleaned_text = text.lower()
    for p in string.punctuation:
        cleaned_text = cleaned_text.replace(p, "")

    words = list(set(cleaned_text.split()))

    if not words:
        print("The text is empty or contains no valid words.")
    else:
        length_dict = {}
        for word in words:
            length = len(word)
            if length not in length_dict:
                length_dict[length] = []
            length_dict[length].append(word)

        for length in length_dict:
            length_dict[length].sort()

        print("\nWords grouped by length (descending):")
        for length in sorted(length_dict.keys(), reverse=True): 
            print(f"Length {length}: {length_dict[length]}") 

        max_len = max(length_dict.keys())
        longest_words = length_dict[max_len]
        all_words_flat = [w for w_list in length_dict.values() for w in w_list]
        avg_length = sum(len(w) for w in all_words_flat) / len(all_words_flat)

        print(f"\nLongest word(s): {longest_words}") 
        print(f"Average word length: {avg_length:.2f}")

def online_store():
    """
    Task 10: Online Store Orders System
    """
    store_orders = {}

    while True:
        print("\nOnline Store Menu:")
        print("1. Add a new customer")
        print("2. Add an order to an existing customer")
        print("3. View all customers, orders, total spent, and loyalty level")
        print("4. Show customer ranking sorted by total spent (descending)")
        print("5. Show inactive customers (no orders yet)")
        print("6. Remove a customer")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Exiting Online Store System. Goodbye!")
            break
        elif choice == "1":
            name = input("Enter customer name: ").strip()
            if name in store_orders:
                print(f"Error: Customer '{name}' already exists.")
            else:
                store_orders[name] = []
                print(f"Customer '{name}' added successfully.")
        elif choice == "2":
            name = input("Enter customer name: ").strip()
            if name not in store_orders:
                print(f"Error: Customer '{name}' does not exist.")
            else:
                try:
                    amount = float(input("Enter order amount (positive number): "))
                    if amount <= 0:
                        print("Error: Order amount must be positive.")
                    else:
                        store_orders[name].append(amount)
                        print(f"Order of {amount} added for '{name}'.")
                except ValueError:
                    print("Error: Please enter a valid number.")
        elif choice == "3":
            if not store_orders:
                print("Customer list is empty.")
            else:
                print("\nAll Customers and Orders:")
                for name, orders in store_orders.items():
                    total = sum(orders)
                    if total >= 100000:
                        level = "Gold"
                    elif total >= 30000:
                        level = "Silver"
                    else:
                        level = "Bronze"
                    print(f"- {name}: Orders: {orders}, Total: {total}, Loyalty Level: {level}")
        elif choice == "4":
            if not store_orders:
                print("Customer list is empty.")
            else:
                ranked = sorted(store_orders.items(), key=lambda x: sum(x[1]), reverse=True)
                print("\nCustomer Ranking (by Total Spent):")
                for rank, (name, orders) in enumerate(ranked, 1):
                    print(f"{rank}. {name} - Total Spent: {sum(orders)}")
        elif choice == "5":
            inactive = [name for name, orders in store_orders.items() if not orders]
            if not inactive:
                print("No inactive customers found.")
            else:
                print(f"Inactive customers (no orders yet): {inactive}")
        elif choice == "6":
            name = input("Enter customer name to remove: ").strip()
            if name in store_orders:
                del store_orders[name]
                print(f"Customer '{name}' removed.")
            else:
                print(f"Error: Customer '{name}' does not exist.")
        else:
            print("Error: Invalid menu option. Please choose between 1 and 7.")



def main():
    """Display a menu to run any of the 10 laboratory tasks."""
    tasks = {
        "1": ("Grade Converter", grade_convert),
        "2": ("Playlist Manager", playlist_manager),
        "3": ("Temperature Conversion Table", temperature_conversion),
        "4": ("List Comprehensions and Filtering", comprehensions_filtering),
        "5": ("Inventory Management", inventory),
        "6": ("Sorting and Displaying Data", sorting_displaying),
        "7": ("Anagram Checker", anagram_checker),
        "8": ("Daily Steps Tracker", steps_tracker),
        "9": ("Word Length Analyzer", word_length),
        "10": ("Online Store Orders System", online_store),
    }

    while True:
        print("\n===== PYTHON LABORATORY ASSIGNMENT =====")
        for number, (title, _) in tasks.items():
            print(f"{number}. {title}")
        print("0. Exit")

        choice = input("Choose a task (0-10): ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice in tasks:
            print(f"\n--- {tasks[choice][0]} ---")
            tasks[choice][1]()
        else:
            print("Invalid choice. Please enter a number from 0 to 10.")


if __name__ == "__main__":
    main()
