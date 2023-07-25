a = int(input())
b = int(input())
if a%b == 0:
    print("%d делится на %d нацело" % (a,b))
    print("частное: %d" % (a//b))
else:
    print("%d не делится на %d" % (a,b))
    print("неполное частное: %d" % (a//b))
    print("остаток: %d" % (a%b))
