# items = ["harry", 39, 3, 9, 1, 94, 23, 343]
# for item in items:
#     if str(item).isnumeric() and item < 9:
#         print(item)
#
# for i in range(1,100,10):
#     print(i, end="" )
# i = 0
# while (True):
#     if i+1 < 5:
#         i = i + 1
#         continue
#     print(i+1, end="")
#     if(i==44):
#
#        i = i + 1
while (True) :
    inp = int(input("enter a number \n"))
    if inp > 100:
        print("you can play this game\n\t")
        break
    else:
        print("your age is not enough for play this game\n")
        continue
