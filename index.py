from proj5 import proj5
from proj2 import proj2
from proj4 import proj4

def select_file():
    print("Select the file :")
    print("1. file_amh.txt")
    print("2. file_en.txt")

    file_map = {
        1: "file_amh.txt",
        2: "file_en.txt"
    }

    try:
        choice = int(input("Enter your choice your choice must be 1 or 2: "))
        file_path = file_map.get(choice)
        if not file_path:
            print("wrong choice. Default to file_en.txt")
            file_path = "file_en.txt"
    except ValueError:
        print("wrong input. Default to file_en.txt")
        file_path = "file_en.txt"

    return file_path

def menu(file_path):
    while True:
        print("\n1. Word Frequency")
        print("2. Character Frequency")
        print("3. Statistical Information")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your beloved choice: "))
            if choice == 0:
                print("Exiting the program. have a nice day!")
                break
            elif choice == 1:
                word_frequency(file_path)
            elif choice == 2:
                character_frequency(file_path)
            elif choice == 3:
                statistics(file_path)
            else:
                print("wrong  choice. Please enter a number between 0 and 3.")
        except (TypeError, ValueError):
            print("wrong input. Please enter a number.")

if __name__ == "__main__":
    print("***************************************************")
    print("*                                                 *")
    print("*   you are already in to text analyzer program   *")
    print("*                                                 *")
    print("***************************************************")

    file_path = select_file()
    menu(file_path)
