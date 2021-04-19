import random

print('Character Thing v1')
print('')
print('')
Species = ''
Prof = ''
while True:
    if Species == '':
        Species = input('Choose your Species: Human, Elf, Dwarf, Orc, or Random: ')
        print('')
    if Species.lower() == 'human':
        print('You have chosen Human. Humans are skilled at many things, but masters of none given their short lifespans.')
        break
    elif Species.lower() == 'elf':
        print('You have chosen Elf. The elves are skilled in Magicks both arcane and natural. They live for thousands of years and often master many skills in that lifetime.')
        break
    elif Species.lower() == 'dwarf':
        print('You have chosen Dwarf. Dwarves are exceptionally skilled craftsmen and fierce warriors that guard their mountain homes from all manner of fearsome foes.')
        break
    elif Species.lower() == 'orc':
        print('You have chosen Orc. The Orcish people are nomadic and hardened by life on the plains of Ordania, their various clans are well known for producing strong warriors and some of the finest horses in the land.')
        break
    elif Species.lower() == 'random':
        Species = random.choice(['Human', 'Elf', 'Dwarf', 'Orc'])
        continue
    else:
        print(Species + '? Never heard of that before... Where did you say you were from again?')
        print('')

Species = Species.capitalize()

print('') #Line Break

print('Okay, so you are a ' + Species + ' but what do you do, like as your profession?')
print('')
while True:
    if Prof == '':
        Prof = input('Choose your profession: Fighter, Wizard, Thief, Priest, Craftsman, or Random: ')
        print('')
    if Prof.lower() == 'fighter':
        print("Oh ho! A fighter eh? I bet you're really strong! Can we arm wrestle later?")
        break
    elif Prof.lower() == 'wizard':
        print("Hmmm... A wizard huh? Can you turn that guy into a sheep? No? I bet you're too busy pondering the mysteries of the Arcane, aren't you? Oh well, maybe later...")
        break
    elif Prof.lower() == 'thief':
        print("Pretty brazen to just admit to anyone that you're a thief don't you think? I'm gonna guess you're plenty daring, but not too wise!")
        break
    elif Prof.lower() == 'priest':
        print("A Priest? Well, I'll be, this is a stroke of luck! My daughter wanted to get married tomorrow, could you do the ceremony for her?")
        break
    elif Prof.lower() == 'craftsman':
        print("Craftsman is a pretty generic term dont you think? Are you any good?")
        break
    elif Prof.lower() == 'random':
        Prof = random.choice(['fighter', 'wizard', 'thief', 'priest', 'craftsman'])
        continue
    else:
        print("Well that's a new one! What exactly does a " + Prof + " do anyway?")
        break

Prof = Prof.capitalize()

print('') #Line Break

#Generate Ability Scores
Strength = random.randrange(8, 19)
Dexterity = random.randrange(8, 19)
Constitution = random.randrange(8, 19)
Wisdom = random.randrange(8, 19)
Intelligence = random.randrange(8, 19)
Charisma = random.randrange(8, 19)
abScores = [Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma]
print("Let's check out your ability scores next. Here they are in order of Strength, Dexterity, Constitution, Wisdom, Intelligence, and Charisma:")
print('')
print(abScores)
print('')
print('Those look pretty good to me! Oh wait, we forgot to add these weird bonuses that for some reason come from being a certain species. Let me do that for you now, how does this look:')
if Species == 'Human':
    abScores = [x+1 for x in abScores]
elif Species == 'Elf':
    abScores[1] = Dexterity + 1
    abScores[4] = Intelligence + 2
elif Species == 'Dwarf':
    abScores[0] = Strength + 1
    abScores[2] = Constitution + 2
elif Species == 'Orc':
    abScores[0] = Strength + 2
    abScores[2] = Constitution + 1
else:
    print("Oh yeah you're one of those " + Species + " folks. I'm not really sure how to handle these weird score numbers for you, sorry friend.")

print('')

print(abScores)

print('')

print("Alright friend, I think the last thing we need to gather here is your name...")
print('')
charName = input('Give your name: ')
charName = charName.capitalize()
print('')
print('')
print(charName + "? That's a great name. Really suits you!")
print('')
print('')
print("Okay, here's how things are looking on my end, look correct to you? :")
print('')
print('--------------------------------------------------------------------------')
print('Name: ' + charName)
print('--------------------------------------------------------------------------')
print('Species: ' + Species)
print('--------------------------------------------------------------------------')
print('Profession: ' + Prof)
print('--------------------------------------------------------------------------')
print('Ability Scores')
print('Strength: ' + str(abScores[0]))
print('Dexterity: ' + str(abScores[1]))
print('Constitution: ' + str(abScores[2]))
print('Wisdom: ' + str(abScores[3]))
print('Intelligence: ' + str(abScores[4]))
print('Charisma: ' + str(abScores[5]))
print('--------------------------------------------------------------------------')
print('')
print('')
print('')
input('Press Enter to Exit...')