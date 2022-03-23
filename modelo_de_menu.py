def print_menu():       ## Your menu design here
    print(30 * "-" , "GloboTechBook" , 30 * "-")
    print("1. Create User")
    print("2. Post")
    print("3. Comment")
    print("4. Exclude Post")
    print("5. Exclude Comment")
    print("6. Exit")
    print(67 * "-")

loop=True

while loop:
    print_menu()
    choice = input("Enter your choice [1-6]: ")

    if choice==1:
        print("Teste 1")

    elif choice==2:
        print("Teste 2")

    elif choice==3:
        print("Teste 3")

    elif choice==4:
        print("Teste 4")

    elif choice==5:
        print("Teste 5")

    elif choice==6:
        print("Teste 6")
        loop=False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")