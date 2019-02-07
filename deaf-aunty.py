status = True

while status:
    answer = input("Say something: ")
    if answer == "I love you aunty, I have to go now":
        status = False
        print("ok. Goodbye.")
    elif answer == answer.lower():
        print("WHAT? SPEAK UP!")
    elif answer == answer.upper():
        print("YOU ARE VERY RUDE!")
    else:
        print("SHOW SOME RESPECT!")
