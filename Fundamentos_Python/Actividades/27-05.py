sum = 0;
num = int(input("Insert the number\t"));
min = num;
big = num;
equale = bool;
if(num != 0):
    while (True):
        num = int(input("Insert the number\t"));
        sum += num;
        if(num == 0):
            break;
        big = (big, num)[num > big];
        min = (min, num)[num < min];
        equale = num == big and num == min;
    print("----------------/-/-/-/-/-/-/-/-/-/-/-/-/----------------\n",
        "The sum of the numbers is:\t", sum);
    print(" The minor number is:\t", min);
    print(" The bigger number is:\t", big);
    h = (" They are not the same", "They are equal")[equale];
    print(h);
else:
    print("Error, solo se ingresó un número");
