import time
print("You kneel on the ground. You tell the other rulers about your situation, and why things turned out this way.")
time.sleep(3)
print("They offer you a choice: life in jail or life under them.")
r6 = input("What will you do? type a to spend life in jail, type b to spend life living a peacful life, type c if you think this isn't a choice. ")
if "a" in r6:
  print("You decide to stay in jail rather than ever submit to them. You are escorted back to your cell.")
  time.sleep(3)
  print("Will you break out?")
  r7 = input("What will you do? type a to try to break out of prison, type b to cry in your cell forever.")
  if "a" in r7:
    print("You decide to break out.")
    time.sleep(3)
    r8 = input("How will you accomplish this? type a to bribe a guard, type b to dig a hole")
    if "a" in r8: 
      import page7
    elif "b" in r8:
      print("You dig a hole. You get out! Congrats, you are a wanted criminal for life, and everyone hates you. You flee to a cottage by the ocean, and live out your days sleeping with one eye open constantly.")
    else:
      print("you didn't follow the rules. start over.")
  elif "b" in r7:
    print("You cry in your cell forever.")
  else: 
    print("you didn't follow the rules. start over.")
elif "b" in r6:
  print("You decide to submit to the enemy. You leave to live life in a seaside cottage peacefully before angry citizens find you and murder you in your sleep.")
else:
  print("you didn't follow the rules. start over.")