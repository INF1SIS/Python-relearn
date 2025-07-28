
# simple program that repeats a string 5 times, then asks the user if they want to repeat again

def repeater():
    text = ("You will never win")
    for i in range(5):
        print(text)
    repeat = input("Do you want to repeat? (y/n): ")
    if repeat.lower() == 'y':
        repeater()
    else:
        print("Bye Loser")
        exit()


repeater()


