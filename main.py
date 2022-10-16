start = int(input("Can you please give me a starting number? "))
stop = int(input("What number would you like me to stop at? "))
step = int(input("Finally, what increment do you want me to use? "))
print("Ok calculating now...")

for i in range (start, stop, step):
  print(i)