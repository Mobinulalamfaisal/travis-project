known_user = ["elice", "bob", "don", "mond", "Malcom", "rees", "dewy","francis"]

while True:
    print("Hi! My name is Shakib")
    name = input("What is your name? :").strip().capitalize()
    if name in known_user:
        print("Hello{}!".format(name))
        remove = input("Would like to remove from the system (y\n)?: ").strip().lower()
        if remove =="y":
            known_user.remove(name)
        elif remove =="n":
             print("No problem!,I will not do that")
        
    else:
          print("i don't think i have your name in the list {}: ".format(name))
          add_me = input("would you like to be added in the system (y\n)?: ").strip().lower()
          if add_me =="y":
              known_user.append(name)
              print(known_user)
          elif add_me =="n":
                  print("okay {}!, see you next time: ".format(name))
              
              
