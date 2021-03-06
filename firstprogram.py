def say_hi(name):
    if name == '':
        print("You did not enter your name!")
    else:
        print("Hey there...")
        for letter in name:
            print(letter)
name = input("Type in your name!")
say_hi(name)