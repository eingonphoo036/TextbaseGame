print('Welcome to PSB python game GP5 \n(N)new game\n(Q)quit')
# GameChar
import time
import random

Player_WarriorHealth = 100
Player_TankerHealth = 100
Enemy_WarriorHealth = 100
Enemy_TankerHealth = 100
Player_WarriorAttacker = random.randint(5, 20)
Player_TankerAttacker = random.randint(1, 10)
Enemy_WarriorAttacker = random.randint(5, 20)
Enemy_TankerAttacker = random.randint(1, 10)
Player_WarriorDef = random.randint(1, 10)
Player_TankerDef = random.randint(5, 15)
Enemy_WarriorDef = random.randint(1, 10)
Enemy_TankerDef = random.randint(5, 15)
Enemy_Name = []
randomRole = random.randint(0, 1)
name_list = []
role = ''

# input new game or exit

def main():
    global Player_WarriorHealth
    global Player_TankerHealth
    global Player_WarriorAttacker
    global Player_TankerAttacker
    global Player_WarriorDef
    global Player_TankerDef
    global name_list
    global Enemy_Name
    global randomRole
    global Enemy_WarriorHealth
    global Enemy_TankerHealth
    global Enemy_WarriorAttacker
    global Enemy_TankerAttacker
    global Enemy_TankerDef
    global Enemy_WarriorDef
    global role
    mainmenu = input('Choose option <ENTER> ==> ')
    if mainmenu == 'N':
        print('\nPlayer team,Setting...\n')
        for unit_name in range(1, 4):

            print(f'Enter Player name  #{unit_name}-> ', end='')

            name1 = input('')
            repeated = False
            while repeated:
                if name1 == "":
                    pass
            repeated = True

            if name1 in name_list:
                print('\nname cannot be same.\n')
                return main()
            if not name1.strip():
                print('\nname cannot be empty.\n')
                return main()
            else:
                name_list.append(name1)
                print(f'Select character #{unit_name}, type: (W)warrior, (T)tanker, ==> ', end='')

                role = input('')
                if role == 'W':
                    print('Ready to start!! ' + str(name_list))
                    time.sleep(2)
                    print(str(name1) + ' Health Is ' + str(Player_WarriorHealth))
                    print(str(name1) + ' Attack Point Is ' + str(Player_WarriorAttacker))
                    print(str(name1) + ' Defence Point Is ' + str(Player_WarriorDef))
                elif role == 'T':
                    print('Ready to start!! ' + str(name_list))
                    print(str(name1) + ' Health Is ' + str(Player_TankerHealth))
                    print(str(name1) + ' Attack Point Is ' + str(Player_TankerAttacker))
                    print(str(name1) + ' Defence Point Is ' + str(Player_TankerDef))
                elif role == '':
                    print("Invalid.......")



        else:
            Enemy_Name = []
        for unit_Enemy in range(1, 4):
            firstNum = random.randint(0, 9)
            secondNum = random.randint(0, 9)
            name = ("AI" + str(firstNum) + str(secondNum))

            if name in Enemy_Name:
                return main()
            if not name.strip():
                return main()

            else:
                Enemy_Name.append(name)
                randomRole = random.randint(0, 1)
                if randomRole == 0:
                    print('Enemy AI is ' + str(name))

                    print(str(name) + ' is Warrior.')
                    print(str(name) + ' Health Is ' + str(Enemy_WarriorHealth))
                    print(str(name) + ' Attack Point Is ' + str(Enemy_WarriorAttacker))
                    print(str(name) + ' Defence Point Is ' + str(Enemy_WarriorDef))

                elif randomRole == 1:
                    print('Enemy AI is ' + str(name))

                    print(str(name) + "is Tanker.")
                    print(str(name) + ' Health Is ' + str(Enemy_TankerHealth))
                    print(str(name) + ' Attack Point Is ' + str(Enemy_TankerAttacker))
                    print(str(name) + ' Defence Point Is ' + str(Enemy_TankerDef))

                while Player_WarriorHealth > 0 and Player_TankerHealth > 0 and Enemy_WarriorHealth > 0 and Enemy_TankerHealth > 0:

                    print("Choose Your Way To Fight 1 or 2 or 3")
                    attack = input("")
                    print("You uses attack " + str(attack))
                    if attack == 1 or attack == 2 or attack == 3:
                        print("")
                        if role == 'W' and randomRole == 0:
                            print("Your Warrior Attack To AI Warrior")
                            Damage = Player_WarriorAttacker - Enemy_WarriorDef + random.randint(5,10)
                            print("Your Warrior Gave " + str(Damage) + " Damage To AI Warrior")
                        Enemy_WarriorHealth = Enemy_WarriorHealth - Damage
                        if Enemy_WarriorHealth < 1:
                            Enemy_WarriorHealth = 0
                        print(" AI Warrior Have Only Left  " + str(Enemy_WarriorHealth))
                        if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                            print("You Won")
                            quit()
                        elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                            print("You Loose")
                            quit()


                    elif role == 'W' and randomRole == 1:
                        time.sleep(1)
                        print("Your Warrior Attack To AI Tanker")
                        Damage2 = Player_WarriorAttacker - Enemy_TankerDef + random.randint(5, 10)
                        print("Your Warrior Gave " + str(Damage2) + " Damage To AI Tanker")
                        Enemy_TankerHealth = Enemy_TankerHealth - Damage2
                        if Enemy_TankerHealth < 1:
                            Enemy_TankerHealth = 0
                        print("AI Tanker Have Only Left " + str(Enemy_TankerHealth))
                        if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                            print("You Won")
                            quit()
                        elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                            print("You Loose")
                            quit()


                    elif role == 'T' and randomRole == 0:
                        time.sleep(1)
                        print("Your Tanker Attack To AI Warrior")
                        Damage3 = Player_TankerAttacker - Enemy_WarriorDef + random.randint(5, 10)
                        print("Your Tanker Gave " + str(Damage3) + " Damage To AI Warrior")
                        Enemy_WarriorHealth = Enemy_WarriorHealth - Damage3
                        if Enemy_WarriorHealth < 1:
                            Enemy_WarriorHealth = 0
                        print(" AI Warrior Have Only Left  " + str(Enemy_WarriorHealth))
                        if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                            print("You Won")
                            quit()
                        elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                            print("You Loose")
                            quit()


                    elif role == 'T' and randomRole == 1:
                        time.sleep(1)
                        print("Your Tanker Attack To AI Warrior")
                        Damage4 = Player_TankerAttacker - Enemy_TankerDef + random.randint(5, 10)
                        print("Your Tanker Gave " + str(Damage4) + " Damage To AI Tanker")
                        Enemy_TankerHealth = Enemy_TankerHealth - Damage4
                        if Enemy_TankerHealth < 1:
                            Enemy_TankerHealth = 0
                        print(" AI Warrior Have Only Left  " + str(Enemy_TankerHealth))
                        if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                            print("You Won")
                            quit()
                        elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                            print("You Loose")
                            quit()


                    if Enemy_WarriorHealth > 0 and Enemy_TankerHealth > 0:
                        if randomRole == 0 and role == 'W':

                            print("AI Warrior Attack TO Your Warrior")
                    Damage5 = Enemy_WarriorAttacker - Player_WarriorDef + random.randint(5, 10)
                    print("AI Warrior Gave " + str(Damage5) + " Damage To your Warrior")
                    Player_WarriorHealth = Player_WarriorHealth - Damage5
                    if Enemy_TankerHealth < 1:
                            Enemy_TankerHealth = 0
                            print(" Your Warrior Health Is Only  " + str(Player_WarriorHealth) + " Left ")
                            if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                                    print("You Won")
                                    quit()
                            elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                                        print("You Loose")
                                        quit()


                    elif randomRole == 0 and role == 'T':
                            time.sleep(1)
                            print("AI Warrior Attack To Your Tanker")
                            Damage6 = Enemy_WarriorAttacker - Player_TankerDef + random.randint(5, 10)
                            print("AI Warrior Gave " + str(Damage6) + " Damage To your Tanker")
                            Player_TankerHealth = Player_TankerHealth - Damage6
                            if Player_WarriorHealth < 1:
                                Player_WarriorHealth = 0
                            print(" Your Tanker Health Is Only  " + str(Player_TankerHealth) + " Left ")
                            if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                                    print("You Won")
                                    quit()
                            elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                                        print("You Loose")
                                        quit()


                    elif randomRole == 1 and role == 'W':
                            time.sleep(1)
                            print("AI Tanker Attack To Your Worrior")
                            Damage7 = Enemy_TankerAttacker - Player_WarriorDef + random.randint(5, 10)
                            print("AI Tanker Gave " + str(Damage7) + " Damage To your Warrior")
                            Player_WarriorHealth = Player_WarriorHealth - Damage7
                            if Player_WarriorHealth < 1:
                                Player_WarriorHealth = 0
                            print(" Your Warrior Health Is Only  " + str(Player_WarriorHealth) + " Left ")
                            if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                                    print("You Won")
                                    quit()
                            elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                                        print("You Loose")
                                        quit()



                    elif randomRole == 1 and role == 'T':
                            time.sleep(1)
                            print("AI Tanker Attack To Your Tanker")
                            Damage8 =  Enemy_TankerAttacker - Player_TankerDef + random.randint(5, 10)
                            print("AI Tanker Gave " + str(Damage8) + " Damage To your Tanker")
                            Player_TankerHealth = Player_TankerHealth - Damage8
                            if Player_TankerHealth < 1:
                                Player_TankerHealth = 0
                            print(" Your Tanker Health Is Only  " + str(Player_TankerHealth) + " Left ")
                            if Enemy_WarriorHealth == 0 or Enemy_WarriorHealth == 0 or Enemy_TankerHealth == 0:
                                    print("You Won")
                                    quit()
                            elif Player_WarriorHealth == 0 or Player_TankerHealth == 0 or Player_TankerHealth == 0:
                                        print("You Loose")
                                        quit()


                    elif attack ==" ":
                        print("Invalid Please Only Choose 1 Or 2 Or 3....")
                        return main()









                else:

                        return str(randomRole())

    elif mainmenu == 'Q':
        print('Quit game...')
        pass
    elif mainmenu =='':
        print(" Invalid...")
        return main()

main()
def quit():
    i = input("")
    if i == "Y":
        print("Play Again")
        return main()
    elif i == "E":
        print("Thank You For Playing Game")
        pass