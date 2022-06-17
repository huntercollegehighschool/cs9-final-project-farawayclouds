import time
print("The enemy is upon you the next morning. They kill all your palace staff, and you wake up the next morning in a cell. The enemy has usurped your throne, and you will likely spend your whole life down here.")
time.sleep(5)
r4 = input("What do you do? type a to try to break out of prison, type b to try to arrange negotiation.")
if "a" in r4:
  print("You decide to break out.")
  time.sleep(3)
  r5 = input("How will you accomplish this? type a to bribe a guard, type b to dig a hole")
  if "a" in r5: 
    import page7
  elif "b" in r5:
    print("You dig a hole. You get out! Congrats, you are a wanted criminal for life, and everyone hates you. You flee to a cottage byt eh ocean, and live out your days sleeping with one eye open constantly.")
  else:
    print("you didn't follow the rules. start over.")
elif "b" in r4:
  print("You arrange negotiations. The enemy crown decides to speak with you. You are humiliatingly brought to them shackled.")
  time.sleep(3)
  import page3
else:
  print("you didn't follow the rules. start over.")