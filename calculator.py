def switch(val1, val2, opt):
    if opt == "+":
        return int(val1)+int(val2)
    elif opt == "-":
        return int(val1)-int(val2)
    elif opt == "*":
        return int(val1)*int(val2)
    else:
        return int(val1)/int(val2)

val1 = raw_input("enter the first number: ")
val2 = raw_input("enter the second number: ")
operator = raw_input("enter the operator out of + - / * : ")
opt = str(operator)

print(switch(val1, val2, opt))