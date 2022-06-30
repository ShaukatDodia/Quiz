# Computer Quiz

playing = input("Do You want to play?\n ")
if playing.lower() != "yes":
    quit()
print("Ok! let's play :)")
score = 0

answer = input("what is full form of CPU \n")
if answer.lower() == "center processing unit":
    print("correct!")
    score += 1
    print(score)
else:
    print("incorrect!")

answer = input("what is full form of SSD \n")
if answer.lower() == "common management admission test":
    print("correct!")
    score += 1
    print(score)
else:
    print("incorrect!")

answer = input("what is full form of RAM \n")
if answer.lower() == "random access memory ":
    print("correct!")
    score += 1
    print(score)
else:
    print("incorrect!")


answer = input("what is full form of PSU \n")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
    print(score)
else:
    print("incorrect!")

answer = input("what is full form of GPU \n")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
    print(score)
else:
    print("incorrect!")

print("congratulation you got " + str(score) + " Question correct.")
print("You got" + str((score / 5) * 100) + "%.")