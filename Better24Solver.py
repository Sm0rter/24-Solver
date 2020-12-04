# Setting up Functions
def combinations(i,a,b,c,d):
    dictionary = {1: [a,b,c,d], 2: [a,b,d,c], 3: [a,c,b,d], 4: [a,c,d,b], 5: [a,d,c,b], 6: [a,d,b,c], 7: [b,a,c,d], 8: [b,a,d,c], 9: [b,c,a,d], 10: [b,c,d,a], 11: [b,d,c,a], 12: [b,d,a,c], 13: [c,a,b,d], 14: [c,a,d,b], 15: [c,b,a,d], 16: [c,b,d,a], 17: [c,d,a,b], 18: [c,d,b,a], 19: [d,c,b,a], 20: [d,c,a,b], 21: [d,b,a,c], 22: [d,b,c,a], 23: [d,a,b,c], 24: [d,a,c,b]}
    return dictionary[i]

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

def calculator(a, o1:str, o2:str, o3:str, z:int):
    num1 = str(a[0])
    num2 = str(a[1])
    num3 = str(a[2])
    num4 = str(a[3])
    if z == 1:
        total = ("(" + num1 + o1 + num2 + ")" + o2 + num3 + o3 + num4)
        n_total = eval(total)
    elif z == 2:
        total = ("(" + num1 + o1 + num2 + o2 + num3 + ")" + o3 + num4)
        n_total = eval(total)
    elif z == 3:
        total = ("(" + num1 + o1 + num2 + ")" + o2 + "(" + num3 + o3 + num4 + ")")
        n_total = eval(total)
    elif z == 4:
        total = (num1 + o1 + num2 + o2 + num3 + o3 + num4)
        n_total = eval(total)
#    elif z == 5:
#        total = (num1 + o1 + "(" + num2 + o2 + num3 + ")" + o3 + num4)
#        n_total = eval(total)
#    elif z == 6:
#        total = (num1 + o1 + num2 + o2 + "(" + num3 + o3 + num4 + ")")
#        n_total = eval(total)
#    elif z == 7:
#        total = (num1 + o1 + "(" + num2 + o2 + num3 + o3 + num4 + ")")
#        n_total = eval(total)
    total_list = [n_total, total]
    return total_list

def calc(a, o1:str, o2:str, o3:str, z:int):
    num1 = str(a[0])
    num2 = str(a[1])
    num3 = str(a[2])
    num4 = str(a[3])
    if num3 == num4:
        if o2 == "/":
            if o3 == "-":
                if z == 3:
                    o3 = "+"
    if z == 1:
        total = ("(" + num1 + o1 + num2 + ")" + o2 + num3 + o3 + num4)
        n_total = eval(total)
    elif z == 2:
        total = ("(" + num1 + o1 + num2 + o2 + num3 + ")" + o3 + num4)
        n_total = eval(total)
    elif z == 3:
        total = ("(" + num1 + o1 + num2 + ")" + o2 + "(" + num3 + o3 + num4 + ")")
        n_total = eval(total)
    elif z == 4:
        total = (num1 + o1 + num2 + o2 + num3 + o3 + num4)
        n_total = eval(total)
#    elif z == 5:
#        total = (num1 + o1 + "(" + num2 + o2 + num3 + ")" + o3 + num4)
#        n_total = eval(total)
#    elif z == 6:
#        total = (num1 + o1 + num2 + o2 + "(" + num3 + o3 + num4 + ")")
#        n_total = eval(total)
#    elif z == 7:
#        total = (num1 + o1 + "(" + num2 + o2 + num3 + o3 + num4 + ")")
#        n_total = eval(total)
    total_list = [n_total, total]
    return total_list

def solver(a:int, b:int, c:int, d:int):
    Group = False
    if a == b or a == c or a == d or b == c or b == d or c == d:
        for i in range(1,25):
            arrangement = combinations(i,a,b,c,d)
            for i in range(1,5):
                Operator1 = choose(i)
                for x in range(1,5):
                    Operator2 = choose(x)
                    for y in range(1,5):
                        Operator3 = choose(y)
                        for z in range(1,8):
                            total = calc(arrangement, Operator1, Operator2, Operator3, z)
                            if total[0] == 24 or total[0] == 24.0:
                                return total[1]

    else:
        for i in range(1,25):
            arrangement = combinations(i,a,b,c,d)
            for i in range(1,5):
                Operator1 = choose(i)
                for x in range(1,5):
                    Operator2 = choose(x)
                    for y in range(1,5):
                        Operator3 = choose(y)
                        for z in range(1,8):
                            total = calculator(arrangement, Operator1, Operator2, Operator3, z)
                            if total[0] == 24 or total[0] == 24.0:
                                return total[1]
    if Group == False:
        return False


# Main Loop
while True:
    first_num = int(input("Put in the first number "))
    second_num = int(input("Put in the second number "))
    third_num = int(input("Put in the third number "))
    fourth_num = int(input("Put in the fourth number "))
    Possible = solver(first_num, second_num, third_num, fourth_num)
    if Possible == False:
        print("The 4 number group is not possible.")
    else:
        print("The 4 number group is possible.")
        print(Possible)