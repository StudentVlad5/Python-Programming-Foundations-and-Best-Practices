from termcolor import colored
import os
import pickle

# Upload contacts from a pickle file
def load_data(book, filename="addressbook.pkl"):
    if not os.path.exists(filename):
        print(f"{colored('File not found', 'red')}")
        return book

    try:
        with open(filename, "rb") as file:
            return pickle.load(file) 
    except Exception as e:
        print(f"{colored('An error occurred while loading contacts:', 'yellow')} {colored(e, 'red')}")
        return book

# Save contacts to a pickle file
def save_data(book, filename="addressbook.pkl"):
    try:
        with open(filename, "wb") as file:
            pickle.dump(book, file)  
        print(f"{colored('Contacts saved successfully', 'green')}")
    except Exception as e:
        print(f"{colored('An error occurred while saving contacts:', 'yellow')} {colored(e, 'red')}")
