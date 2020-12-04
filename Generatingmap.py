# Variables
a = 0
# Functions
def choose(chooser):
    if chooser == 1:
        string = "+"
    elif chooser == 2:
        string = "-"
    elif chooser == 3:
        string = "*"
    elif chooser == 4:
        string = "/"
    else:
        print("There is something wrong.")
    return string


# Main Loop Generator
for i in range(1,5):
    slot1 = choose(i)
    for x in range(1,5):
        slot2 = choose(x)
        for y in range(1,5):
            slot3 = choose(y)
            for z in range(1,5):
                slot4 = choose(z)
                a += 1
                first_part = str(a)
                if z == 1:
                    string = (first_part + ": " + "[" + "a" + slot1 + "b" + slot2 + "c" + slot3 + "d" + "]" + ", ")
                elif z == 2:
                    string = (first_part + ": " + "[" + "(" "a" + slot1 + "b" + ")" + slot2 + "c" + slot3 + "d" + "]" + ", ")
                elif z == 3:
                    string = (first_part + ": " + "[" + "("  + "a" + slot1 + "b" + slot2 + "c" + ")" + slot3 + "d" + "]" + ", ")
                elif z == 4:
                    string = (first_part + ": " + "[" + "(" + "a" + slot1 + "b" + ")" + slot2 + "(" + "c" + slot3 + "d" + ")" + "]" + ", ")
                print(string)
