def play_again():
    while True:
        if choice == "yes":
            return True 
        elif choice == "no":
            print("thank you for playing! goodbye!")
            return False
        else:
            print("please type yes or no ")
def display_response(response):
    print("\n🔮 The Magic 8-Ball says:", response, "\n")
