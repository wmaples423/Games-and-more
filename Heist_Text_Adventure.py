while True:
    print("\nYou and your posse sit at the top of the canyon as the four car Feng Hu express train comes into view. Your right hand man, Armadillo Jones looks at you and asks 'you ready boss?' ")
    answer = input("\nBegin the heist? (yes / no)  ")
    if answer.lower().strip() == "yes":
        approach = input("\nFrom which direction do you assault the train? (front / back / side)  ").lower().strip()

 #approach from the front
        if approach == "front":
            #shoot conductor
            front = input("\nThe train is barrellling towards you. The conductor begins blowing the engine. What do you do? (shoot conductor / board train / derail)  ")
            if front == "shoot conductor":
                print("\nBulls eye! The conductor lifelessly falls forward onto the acceleration lever. The train begins gaining speed and races off too fast to board. It crashes into the depot in Feng Hu. Game over.\n")

            #board train
            elif front == "board train":
                board = input("\nYou grab onto the ladder on the train engine. You hear the door to the engine room bolt closed. A siren begins to sound out. What do you do? (enter engine / enter car)  ")
                if board =="enter engine":
                    print("\nYou attempt to pry the door open, but it is bolted shut. Moments later, lawmen appear behind you with guns drawn. Game over.\n")
                else:
                    showdown = input("\nYou open a door to a passenger car with lawmen rushing through to you. What do you do?  (shoot / run)  ")
                    if showdown =="shoot":
                        print("\nThere is a hail of gunfire. All parties fall to the ground. Game over.\n")
                    else:
                        print("\nYou are cornered as the lawmen approach, forcing you to surrender. Game over.\n")

            #destroy rail
            else:
                print("\nYou light a stick of dynamite and drop it onto the rails. An explosion rings out behind you. The train derails, falling to one side and sliding several hundred feet before coming to a stop.\n")
                derail = input("Passengers begin filing out of the train, some of them being lawmen. What do you do?  (threaten / fire)  ")
                if derail =="threaten":
                    print("\nThe passengers lay on the ground. The lawmen drop their weapons. The train is yours!\n")
                    derail2 = input("You locate the the boxes of gold on the second to last car. They are too heavy to carry entirely. What do you do?  (small bag / large bag / box)  ")
                    if derail2 == "small bag":
                        print("\nYou manage to escape successfully with only a fraction of the loot. Minor success!\n")
                    elif derail2 =="large bag":
                        print("\nYou load up half of the haul into heavy bags. You ride off to the mountains but the slower travel gives the law time to catch up to you.\n")
                        large = input("Your camp has been surrounded by lawmen. What do you do?  (surrender / fire / escape)  ")
                        if large =="surrender":
                            print("\nYou are taken into custody and summarily hung in Feng Hu for the crime of train robbery. Game over.\n")
                        elif large =="fire":
                            print("\nYou go down in a hail of gunfire. Locals tell stories of your posse for years to come. Historical success.\n")
                        else:
                            print("\nYou abandon your posse in the standoff and live the rest of yours days on the lamb. Questionable success.\n")
                    else:
                        print("\nYou attempt to drag the boxes to your hideout with rope. Your hubris gets the better of you and you perish from exposure in the heat. Game over.\n")
                elif derail =="fire":
                    print("\nYou alone fire on the civilians. Your crews looks on at you in horror for the crime you have committed.\n")
                    fire = input("They ask you why you did something so heartless. How do you defend your action?  (witnesses / reactionary / fun)  ")
                    print("\nYour crew looks at you in disgust and leaves you to take in the gravity of what you have just done. Game over.\n")

#approach from the back
        elif approach == "back":
            back = input("\nYou approach the train from behind without being spotted and leap onto the caboose. The back door is locked. What do you do?  (shoot lock / climb on top / climb around)  ")
            if back =="shoot lock":
                print("\nUnbenounst to you, the storage car is full of tanks of barreled oil. The back of the train explodes, atomizing you and your posse. Game over.\n")
            elif back =="climb on top":
                climb = input("\nYou reach the top of the train car. You see a skylight on top of each car. Which car do you enter?  (caboose / third car / second car / engine)  ")
                if climb =="caboose":
                    print("\nThe caboose is full of barrels of oil and one lawmen. When you drop in, he panics, fires his weapon, and blows you all sky high. Game over.\n")
                elif climb =="third car":
                    third = input("\nYou land in a car of lawmen sitting on boxes of gold. They are caught off guard. What do you do?  (fire / threaten / surrender)  ")
                    if third =="fire":
                        print("\nhe lawmen fall to the ground. The gold is yours. You disconnect the car and escape with your spoils. Congratulations, you win!\n")
                        break
                    elif third =="threaten":
                        print("\nThey are not intimidated. They pull their guns, and the car erupts in gunfire. Game over.\n")
                    else:
                        print("\nConfused, they arrest you and you are put on trial for gross stupidity. Game over.\n")
                else:
                    print("\nWhile crossing the third car, lawmen hear you. They ascend after you and fire on you from behind before you can react. Game over.\n")

            else:
                print("\nou attempt to shimmy around the side of the train car, lose your grip, and plummet into the dust at 30 mph. Game over.\n")
            

#approach from the side
        else:
            print("\nAn emergency siren begins blaring as you approach, a massive cloud of dust growing behind you. You begin to hear the cracks of rifle shots.\n")
            side = input("Your posse is being picked off one by one as you get closer to the middle car of the train. What do you do? (proceed / flee)  ")
            if side =="proceed":
                print("\nYou and Armadillo Jones reach the train and leap onto the coupling between cars. The rest of your posse has perished.\n")
                side = input("There is a car in front of you and behind. Which do you enter? (front / behind)  ")
                if side =="front":
                    front = input("\nYou enter a car full of civilians. What do you do? (take hostage / rob civilians / cross the car)  ") 
                    if front =="take hostage":
                        hostage = input("\nYou grab a woman as a hostage moments before lawmen enter from the car behind. What do you do? (surrender / ransom / attack)  ")
                        if hostage =="surrender":
                            print("\nYou are taken into custody to stand trial. Game over.\n")
                        elif hostage =="ransom":
                            print("\nYou demand a ransom. You hold your hostage until reaching Feng Hu where authorities promptly arrest you. Game over.\n")
                        else:
                            print("\nYou fire your gun, forcing the lawmen to fire as well. Bullets fly and moments later your body falls to the floor. Game over.\n")
                    elif front == "rob civilians":
                        print("\nWhile your back is turned, you feel a gun press against your neck. Game over.\n")
                    else:
                        print("\nYou are tackled by the men in the car when your back is turned. Game over.\n")
                else:
                    back = input("\nSix lawmen have their guns trained on the door as you enter. One of them tells you to drop your weapons. What do you do? (draw / drop)  ")
                    if back == "draw":
                        print("\nYou and Jones are riddled with bullets by the lawmen. Game over.\n")
                    else:
                        
                        print("\nYou are taken into custody and taken to stand trial for attempted train robbery.\n")
            else:
                print("\nYou return to camp. The survivors cast you out of the group for your poor leadership.\n")

    else:
        print("\nYour crew stares at you for what seems like an eternity before silentyly returning to camp. The train safely arrives at Feng Hu station, its cargo intact.\n")
        break
