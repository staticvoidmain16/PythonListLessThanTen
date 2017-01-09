list = []
new_list = []

print("Keep entering numbers until you are finished. When finished, hit return: ")

while True:
    try:
        user_input = input()
        if user_input == "":
            break
        else:       
            list.append(int(user_input))
    except ValueError:
        print("Enter intgers only!\n")

while True:
    try:
        user_number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Enter integers only!\n")

for x in list:
    if x < user_number:
        new_list.append(x)
        
print("\nAll of the numbers in the list are less than %d" % (user_number))
print(new_list)
        
        
        
