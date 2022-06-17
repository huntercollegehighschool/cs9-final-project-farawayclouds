import time
time.sleep(3)
print("The working class is greatly angered by the increase in taxes. ")
time.sleep(2)
print("The peasants decide to rebel.")
time.sleep(2)
r2 = input("What should you do? type a to go and talk to your people, type b to ignore the rebellion, and type c to have your army ride out and beat them up. ")
if "a" in r2:
  print("You decide to go and try and reason with your people. However, as you ride out of the palace, you feel as though they might harm you like they harmed your father due to their anger and bring some guards with you for backup.")
  time.sleep(4)
  print("You reach the area where the rebellion is strongest.     People are smashing windows of a government building, and laughing as they set it ablaze. A leader of the rebellion approaches you.")
  time.sleep(4)
  print("'Oh, here comes the cowardly ruler, here to steal from us like the last one. ' The man sees that you brought backup and he looks angry. 'Do you plan on fighting us, Your Majesty?'")
  time.sleep(4)
  r3 = input("What do you do? type a to have your guards attack them, type b to ignore.")
  if "a" in r3:
    import page5
  elif "b" in r3:
    print("You ignore the angry man. 'No, I wanted to explain myself to you.' You try to explain your situatuon, but all the citizens around you refuse to listen, because everything is the fault of your father, not theirs. They get violent, and attempt to kill you. Your guards stand no chance, and you flee back to the palace.")
    time.sleep(6)
    import page6
  else: 
    print("You didn't follow the rules. Start over.")
elif "b" in r2:
  print("You decide to ignore the unhappy people.")
  time.sleep(2)
  import page6
elif "c" in r2:
  print("You decide to shut up your people because you have bigger issues right now. Your foot soldiers kill a bunch of people, which shuts down the rebellion. ")
  time.sleep(4)
  print("Everyone hates you.")
  time.sleep(1)
  print("Your guards hate you. The staff hates you. Your advisors hate you.")
  time.sleep(2)
  r11 = ("Do you want to kill yourself? y // n")
  if "y" in r11:
    print("Okay. Game over. Nobody is sad.")
  elif "n" in r11:
    print("Alright. Make the right decisions this time around.")
    import main.py
  else: 
    print("you didn't follow the rules. start over.")
else: 
  print("You didn't follow the rules. Start over.")
  