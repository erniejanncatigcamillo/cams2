# Step 1: Create and write initial message
try:
     # Ask user for input
     message = input("Enter a short note/message: ")
     
     # Save to file in write mode
     with open("notes.txt", "w") as file:
         file.write(message)
     print("Message saved successfully!\n")
     # Step 2: Read and display the file
     with open("notes.txt", "r") as file:
         content = file.read()
     print("Content of notes.txt:")
     print(content, "\n")
     # Step 3: Append new data
     new_note = input("Enter another note: ")
     with open("notes.txt", "a") as file:
         file.write("\n" + new_note)
     print("Note appended successfully!\n")
     # Display updated content
     with open("notes.txt", "r") as file:
         updated_content = file.read()
     print("Updated content of notes.txt:")
     print(updated_content)
 # Step 4: Error handling
except FileNotFoundError:print("Error: The file was not found.")
except Exception as e:print(f"An unexpected error occurred: {e}")