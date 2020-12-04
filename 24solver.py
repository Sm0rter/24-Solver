# Setting up functions
def combinations(i,a,b,c,d):
    dictionary = {1: [a,b,c,d], 2: [a,b,d,c], 3: [a,c,b,d], 4: [a,c,d,b], 5: [a,d,c,b], 6: [a,d,b,c], 7: [b,a,c,d], 8: [b,a,d,c], 9: [b,c,a,d], 10: [b,c,d,a], 11: [b,d,c,a], 12: [b,d,a,c], 13: [c,a,b,d], 14: [c,a,d,b], 15: [c,b,a,d], 16: [c,b,d,a], 17: [c,d,a,b], 18: [c,d,b,a], 19: [d,c,b,a], 20: [d,c,a,b], 21: [d,b,a,c], 22: [d,b,c,a], 23: [d,a,b,c], 24: [d,a,c,b]}
    return dictionary[i]

def calculate(o,x):
    a = int(o[0])
    b = int(o[1])
    c = int(o[2])
    d = int(o[3])
    map = {1: [a+b+c+d], 2: [(a+b)+c+d], 3: [(a+b+c)+d], 4: [(a+b)+(c+d)], 5: [a+b+c-d], 6: [(a+b)+c-d], 7: [(a+b+c)-d], 8: [(a+b)+(c-d)], 9: [a+b+c*d], 10: [(a+b)+c*d], 11: [(a+b+c)*d], 12: [(a+b)+(c*d)], 13: [a+b+c/d], 14: [(a+b)+c/d], 15: [(a+b+c)/d], 16: [(a+b)+(c/d)], 17: [a+b-c+d], 18: [(a+b)-c+d], 19: [(a+b-c)+d], 20: [(a+b)-(c+d)], 21: [a+b-c-d], 22: [(a+b)-c-d], 23: [(a+b-c)-d], 24: [(a+b)-(c-d)], 25: [a+b-c*d], 26: [(a+b)-c*d], 27: [(a+b-c)*d], 28: [(a+b)-(c*d)], 29: [a+b-c/d], 30: [(a+b)-c/d], 31: [(a+b-c)/d], 32: [(a+b)-(c/d)], 33: [a+b*c+d], 34: [(a+b)*c+d], 35: [(a+b*c)+d], 36: [(a+b)*(c+d)], 37: [a+b*c-d], 38: [(a+b)*c-d], 39: [(a+b*c)-d], 40: [(a+b)*(c-d)], 41: [a+b*c*d], 42: [(a+b)*c*d], 43: [(a+b*c)*d], 44: [(a+b)*(c*d)], 45: [a+b*c/d], 46: [(a+b)*c/d], 47: [(a+b*c)/d], 48: [(a+b)*(c/d)], 49: [a+b/c+d], 50: [(a+b)/c+d], 51: [(a+b/c)+d], 52: [(a+b)/(c+d)], 53: [a+b/c-d], 54: [(a+b)/c-d], 55: [(a+b/c)-d], 56: [(a+b)/(c-d)], 57: [a+b/c*d], 58: [(a+b)/c*d], 59: [(a+b/c)*d], 60: [(a+b)/(c*d)], 61: [a+b/c/d], 62: [(a+b)/c/d],63: [(a+b/c)/d], 64: [(a+b)/(c/d)], 65: [a-b+c+d], 66: [(a-b)+c+d], 67: [(a-b+c)+d], 68: [(a-b)+(c+d)], 69: [a-b+c-d], 70: [(a-b)+c-d], 71: [(a-b+c)-d], 72: [(a-b)+(c-d)], 73: [a-b+c*d], 74: [(a-b)+c*d], 75: [(a-b+c)*d], 76: [(a-b)+(c*d)], 77: [a-b+c/d], 78: [(a-b)+c/d], 79: [(a-b+c)/d], 80: [(a-b)+(c/d)], 81: [a-b-c+d], 82: [(a-b)-c+d], 83: [(a-b-c)+d], 84: [(a-b)-(c+d)], 85: [a-b-c-d], 86: [(a-b)-c-d], 87: [(a-b-c)-d], 88: [(a-b)-(c-d)], 89: [a-b-c*d], 90: [(a-b)-c*d], 91: [(a-b-c)*d], 92: [(a-b)-(c*d)], 93: [a-b-c/d], 94: [(a-b)-c/d], 95: [(a-b-c)/d], 96: [(a-b)-(c/d)], 97: [a-b*c+d], 98: [(a-b)*c+d],  99: [(a-b*c)+d], 100: [(a-b)*(c+d)], 101: [a-b*c-d], 102: [(a-b)*c-d], 103: [(a-b*c)-d], 104: [(a-b)*(c-d)], 105: [a-b*c*d], 106: [(a-b)*c*d], 107: [(a-b*c)*d], 108: [(a-b)*(c*d)], 109: [a-b*c/d], 110: [(a-b)*c/d], 111: [(a-b*c)/d], 112: [(a-b)*(c/d)], 113: [a-b/c+d], 114: [(a-b)/c+d], 115: [(a-b/c)+d], 116: [(a-b)/(c+d)], 117: [a-b/c-d],118: [(a-b)/c-d], 119: [(a-b/c)-d], 120: [(a-b)/(c-d)], 121: [a-b/c*d], 122: [(a-b)/c*d], 123: [(a-b/c)*d], 124: [(a-b)/(c*d)], 125: [a-b/c/d], 126: [(a-b)/c/d], 127: [(a-b/c)/d], 128: [(a-b)/(c/d)], 129: [a*b+c+d], 130: [(a*b)+c+d], 131: [(a*b+c)+d], 132: [(a*b)+(c+d)], 133: [a*b+c-d], 134: [(a*b)+c-d], 135: [(a*b+c)-d], 136: [(a*b)+(c-d)], 137: [a*b+c*d], 138: [(a*b)+c*d], 139: [(a*b+c)*d], 140: [(a*b)+(c*d)], 141: [a*b+c/d], 142: [(a*b)+c/d], 143: [(a*b+c)/d], 144: [(a*b)+(c/d)], 145: [a*b-c+d], 146: [(a*b)-c+d], 147: [(a*b-c)+d], 148: [(a*b)-(c+d)], 149: [a*b-c-d], 150: [(a*b)-c-d], 151: [(a*b-c)-d], 152: [(a*b)-(c-d)], 153: [a*b-c*d], 154: [(a*b)-c*d], 155: [(a*b-c)*d], 156: [(a*b)-(c*d)], 157: [a*b-c/d], 158: [(a*b)-c/d], 159: [(a*b-c)/d], 160: [(a*b)-(c/d)], 161: [a*b*c+d], 162: [(a*b)*c+d], 163: [(a*b*c)+d], 164: [(a*b)*(c+d)], 165: [a*b*c-d], 166: [(a*b)*c-d], 167: [(a*b*c)-d], 168: [(a*b)*(c-d)], 169: [a*b*c*d], 170: [(a*b)*c*d], 171: [(a*b*c)*d], 172: [(a*b)*(c*d)], 173: [a*b*c/d], 174: [(a*b)*c/d], 175: [(a*b*c)/d], 176: [(a*b)*(c/d)], 177: [a*b/c+d], 178: [(a*b)/c+d], 179: [(a*b/c)+d], 180: [(a*b)/(c+d)], 181: [a*b/c-d], 182: [(a*b)/c-d], 183: [(a*b/c)-d], 184: [(a*b)/(c-d)], 185: [a*b/c*d], 186: [(a*b)/c*d], 187: [(a*b/c)*d], 188: [(a*b)/(c*d)], 189: [a*b/c/d], 190: [(a*b)/c/d], 191: [(a*b/c)/d], 192: [(a*b)/(c/d)], 193: [a/b+c+d], 194: [(a/b)+c+d], 195: [(a/b+c)+d], 196: [(a/b)+(c+d)], 197: [a/b+c-d], 198: [(a/b)+c-d], 199: [(a/b+c)-d], 200: [(a/b)+(c-d)], 201: [a/b+c*d], 202: [(a/b)+c*d], 203: [(a/b+c)*d], 204: [(a/b)+(c*d)], 205: [a/b+c/d], 206: [(a/b)+c/d], 207: [(a/b+c)/d], 208: [(a/b)+(c/d)], 209: [a/b-c+d], 210: [(a/b)-c+d], 211: [(a/b-c)+d], 212: [(a/b)-(c+d)],213: [a/b-c-d], 214: [(a/b)-c-d], 215: [(a/b-c)-d], 216: [(a/b)-(c-d)], 217: [a/b-c*d], 218: [(a/b)-c*d], 219: [(a/b-c)*d], 220: [(a/b)-(c*d)], 221: [a/b-c/d], 222: [(a/b)-c/d], 223: [(a/b-c)/d], 224: [(a/b)-(c/d)], 225: [a/b*c+d], 226: [(a/b)*c+d], 227: [(a/b*c)+d], 228: [(a/b)*(c+d)], 229: [a/b*c-d], 230: [(a/b)*c-d], 231: [(a/b*c)-d], 232: [(a/b)*(c-d)], 233: [a/b*c*d], 234: [(a/b)*c*d], 235: [(a/b*c)*d], 236: [(a/b)*(c*d)], 237: [a/b*c/d], 238: [(a/b)*c/d], 239: [(a/b*c)/d], 240: [(a/b)*(c/d)], 241: [a/b/c+d], 242: [(a/b)/c+d], 243: [(a/b/c)+d], 244: [(a/b)/(c+d)], 245: [a/b/c-d], 246: [(a/b)/c-d], 247: [(a/b/c)-d], 248: [(a/b)/(c-d)], 249: [a/b/c*d], 250: [(a/b)/c*d], 251: [(a/b/c)*d], 252: [(a/b)/(c*d)], 253: [a/b/c/d], 254: [(a/b)/c/d], 255: [(a/b/c)/d], 256: [(a/b)/(c/d)]}
    answer = map[x]
    return answer

def calc(o,x):
    a = int(o[0])
    b = int(o[1])
    c = int(o[2])
    d = int(o[3])
    map = {1: [a+b+c+d], 2: [(a+b)+c+d], 3: [(a+b+c)+d], 4: [(a+b)+(c+d)], 5: [a+b+c-d], 6: [(a+b)+c-d], 7: [(a+b+c)-d], 8: [(a+b)+(c-d)], 9: [a+b+c*d], 10: [(a+b)+c*d], 11: [(a+b+c)*d], 12: [(a+b)+(c*d)], 13: [a+b+c/d], 14: [(a+b)+c/d], 15: [(a+b+c)/d], 16: [(a+b)+(c/d)], 17: [a+b-c+d], 18: [(a+b)-c+d], 19: [(a+b-c)+d], 20: [(a+b)-(c+d)], 21: [a+b-c-d], 22: [(a+b)-c-d], 23: [(a+b-c)-d], 24: [(a+b)-(c-d)], 25: [a+b-c*d], 26: [(a+b)-c*d], 27: [(a+b-c)*d], 28: [(a+b)-(c*d)], 29: [a+b-c/d], 30: [(a+b)-c/d], 31: [(a+b-c)/d], 32: [(a+b)-(c/d)], 33: [a+b*c+d], 34: [(a+b)*c+d], 35: [(a+b*c)+d], 36: [(a+b)*(c+d)], 37: [a+b*c-d], 38: [(a+b)*c-d], 39: [(a+b*c)-d], 40: [(a+b)*(c-d)], 41: [a+b*c*d], 42: [(a+b)*c*d], 43: [(a+b*c)*d], 44: [(a+b)*(c*d)], 45: [a+b*c/d], 46: [(a+b)*c/d], 47: [(a+b*c)/d], 48: [(a+b)*(c/d)], 49: [a+b/c+d], 50: [(a+b)/c+d], 51: [(a+b/c)+d], 52: [(a+b)/(c+d)], 53: [a+b/c-d], 54: [(a+b)/c-d], 55: [(a+b/c)-d], 56: [(a+b)/(c+d)], 57: [a+b/c*d], 58: [(a+b)/c*d], 59: [(a+b/c)*d], 60: [(a+b)/(c*d)], 61: [a+b/c/d], 62: [(a+b)/c/d], 63: [(a+b/c)/d], 64: [(a+b)/(c/d)], 65: [a-b+c+d], 66: [(a-b)+c+d], 67: [(a-b+c)+d], 68: [(a-b)+(c+d)], 69: [a-b+c-d], 70: [(a-b)+c-d], 71: [(a-b+c)-d], 72: [(a-b)+(c-d)], 73: [a-b+c*d], 74: [(a-b)+c*d], 75: [(a-b+c)*d], 76: [(a-b)+(c*d)], 77: [a-b+c/d], 78: [(a-b)+c/d], 79: [(a-b+c)/d], 80: [(a-b)+(c/d)], 81: [a-b-c+d], 82: [(a-b)-c+d], 83: [(a-b-c)+d], 84: [(a-b)-(c+d)], 85: [a-b-c-d], 86: [(a-b)-c-d], 87: [(a-b-c)-d], 88: [(a-b)-(c-d)], 89: [a-b-c*d], 90: [(a-b)-c*d], 91: [(a-b-c)*d], 92: [(a-b)-(c*d)], 93: [a-b-c/d], 94: [(a-b)-c/d], 95: [(a-b-c)/d], 96: [(a-b)-(c/d)], 97: [a-b*c+d], 98: [(a-b)*c+d], 99: [(a-b*c)+d], 100: [(a-b)*(c+d)], 101: [a-b*c-d], 102: [(a-b)*c-d], 103: [(a-b*c)-d], 104: [(a-b)*(c-d)], 105: [a-b*c*d], 106: [(a-b)*c*d], 107: [(a-b*c)*d], 108: [(a-b)*(c*d)], 109: [a-b*c/d], 110: [(a-b)*c/d], 111: [(a-b*c)/d], 112: [(a-b)*(c/d)], 113: [a-b/c+d], 114: [(a-b)/c+d], 115: [(a-b/c)+d], 116: [(a-b)/(c+d)], 117: [a-b/c-d], 118: [(a-b)/c-d], 119: [(a-b/c)-d], 120: [(a-b)/(c+d)], 121: [a-b/c*d], 122: [(a-b)/c*d], 123: [(a-b/c)*d], 124: [(a-b)/(c*d)], 125: [a-b/c/d], 126: [(a-b)/c/d], 127: [(a-b/c)/d], 128: [(a-b)/(c/d)], 129: [a*b+c+d], 130: [(a*b)+c+d], 131: [(a*b+c)+d], 132: [(a*b)+(c+d)], 133: [a*b+c-d], 134: [(a*b)+c-d], 135: [(a*b+c)-d], 136: [(a*b)+(c-d)], 137: [a*b+c*d], 138: [(a*b)+c*d], 139: [(a*b+c)*d], 140: [(a*b)+(c*d)], 141: [a*b+c/d], 142: [(a*b)+c/d], 143: [(a*b+c)/d], 144: [(a*b)+(c/d)], 145: [a*b-c+d], 146: [(a*b)-c+d], 147: [(a*b-c)+d], 148: [(a*b)-(c+d)], 149: [a*b-c-d], 150: [(a*b)-c-d], 151: [(a*b-c)-d], 152: [(a*b)-(c-d)], 153: [a*b-c*d], 154: [(a*b)-c*d], 155: [(a*b-c)*d], 156: [(a*b)-(c*d)], 157: [a*b-c/d], 158: [(a*b)-c/d], 159: [(a*b-c)/d], 160: [(a*b)-(c/d)], 161: [a*b*c+d], 162: [(a*b)*c+d], 163: [(a*b*c)+d], 164: [(a*b)*(c+d)], 165: [a*b*c-d], 166: [(a*b)*c-d], 167: [(a*b*c)-d], 168: [(a*b)*(c-d)], 169: [a*b*c*d], 170: [(a*b)*c*d], 171: [(a*b*c)*d], 172: [(a*b)*(c*d)], 173: [a*b*c/d], 174: [(a*b)*c/d], 175: [(a*b*c)/d], 176: [(a*b)*(c/d)], 177: [a*b/c+d], 178: [(a*b)/c+d], 179: [(a*b/c)+d], 180: [(a*b)/(c+d)], 181: [a*b/c-d], 182: [(a*b)/c-d], 183: [(a*b/c)-d], 184: [(a*b)/(c+d)], 185: [a*b/c*d], 186: [(a*b)/c*d], 187: [(a*b/c)*d], 188: [(a*b)/(c*d)], 189: [a*b/c/d], 190: [(a*b)/c/d], 191: [(a*b/c)/d], 192: [(a*b)/(c/d)], 193: [a/b+c+d], 194: [(a/b)+c+d], 195: [(a/b+c)+d], 196: [(a/b)+(c+d)], 197: [a/b+c-d], 198: [(a/b)+c-d], 199: [(a/b+c)-d], 200: [(a/b)+(c-d)], 201: [a/b+c*d], 202: [(a/b)+c*d], 203: [(a/b+c)*d], 204: [(a/b)+(c*d)], 205: [a/b+c/d], 206: [(a/b)+c/d], 207: [(a/b+c)/d], 208: [(a/b)+(c/d)], 209: [a/b-c+d], 210: [(a/b)-c+d], 211: [(a/b-c)+d], 212: [(a/b)-(c+d)], 213: [a/b-c-d], 214: [(a/b)-c-d], 215: [(a/b-c)-d], 216: [(a/b)-(c-d)], 217: [a/b-c*d], 218: [(a/b)-c*d], 219: [(a/b-c)*d], 220: [(a/b)-(c*d)], 221: [a/b-c/d], 222: [(a/b)-c/d], 223: [(a/b-c)/d], 224: [(a/b)-(c/d)], 225: [a/b*c+d], 226: [(a/b)*c+d], 227: [(a/b*c)+d], 228: [(a/b)*(c+d)], 229: [a/b*c-d], 230: [(a/b)*c-d], 231: [(a/b*c)-d], 232: [(a/b)*(c-d)], 233: [a/b*c*d], 234: [(a/b)*c*d], 235: [(a/b*c)*d], 236: [(a/b)*(c*d)], 237: [a/b*c/d], 238: [(a/b)*c/d], 239: [(a/b*c)/d], 240: [(a/b)*(c/d)], 241: [a/b/c+d], 242: [(a/b)/c+d], 243: [(a/b/c)+d], 244: [(a/b)/(c+d)], 245: [a/b/c-d], 246: [(a/b)/c-d], 247: [(a/b/c)-d], 248: [(a/b)/(c+d)], 249: [a/b/c*d], 250: [(a/b)/c*d], 251: [(a/b/c)*d], 252: [(a/b)/(c*d)], 253: [a/b/c/d], 254: [(a/b)/c/d], 255: [(a/b/c)/d], 256: [(a/b)/(c/d)]}
    answer = map[x]
    return answer

def solver(a:int,b:int,c:int,d:int):
    group = False
    if a == b or a == c or a == d or b == c or b == d or c == d:
        for i in range(1,25):
            arrangement = combinations(i,a,b,c,d)
            for x in range(1,257):
                total = calc(arrangement, x)
                if total == [24] or total == [24.0]:
                    group == True
                    return True

    else:            
        for i in range(1,25):
            arrangement = combinations(i,a,b,c,d)
            for x in range(1,257):
                total = calculate(arrangement, x)
                if total == [24.0] or total == [24]:
                    group == True
                    return True
    if group == False:
        return False


# Main loop
while True:
    first_num = int(input("Put in the first number "))
    second_num = int(input("Put in the second number "))
    third_num = int(input("Put in the third number "))
    fourth_num = int(input("Put in the fourth number "))
    Possible = solver(first_num, second_num, third_num, fourth_num)
    if Possible == True:
        print("The 4 number group is possible.")
    elif Possible == False:
        print("The 4 number group is not possible.")
    else:
        print("The function is returning the wrong thing.")

