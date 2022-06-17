import time
print("You bribe a guard.")
time.sleep(2)
print("Well, you try to, and get stabbed in the stomach.")
time.sleep(2)
r9 = input("Do you want to die? y // n")
if "y" in r9:
  print("You die.")
elif "n" in r9:
  print("Okay! Try again. :)")
  time.sleep(2)
  import main.py
else:
  print("you didn't follow the rules. start over.")