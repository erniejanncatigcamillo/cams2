# Step 1: Get user input
try:
     username = input("Enter username: ")
     age = int(input("Enter age: "))
     # Step 3: Save data if input is valid
     with open("users.txt", "a") as file:
         file.write(f"{username} - {age}\n")
except ValueError:
     print("Error: Age must be a number.")
 # Step 4: Display all saved users
print("\n--- Saved Users ---")
try:
     with open("users.txt", "r") as file:
         content = file.read()
         print(content)
except FileNotFoundError:
     print("No users found.")
 # Step 5: Always display
print("System complete.")