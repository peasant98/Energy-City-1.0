# Matthew Strong
# The Energy Program, Volume 1.0
# Computer Science Student in University of Colorado Boulder
# Project for brief Python practice over the break



# This program relates to one of my passions, energy,
# The goal is to bring to light the importance of clean and green communities in society
# As it is, fossil fuels such as coal are going down in usage across the world.
# Many countries are transitioning to more green environments, and my simulation,
# As one can call it, is supposed to give regular users a hands-on experience
# With these ideas. Here we go.

from random import *

# importing the ability to randomly generate numbers.


class City:
    def __init__(self):
        # creating a pretty design for the beginning and intro to the title of the program.
        print("========================================//////////////================================")
        print("")
        print("---------------------------------------PYCITY-----------------------------------------")
        print("")
        print("=====================================/////////////====================================")
        print("")
        print("")
        print("Created by Matthew Strong, Version 1.0, January 9th, 2018.")
        print("")
        print("")
        print("")
        print("")
        print("The goal of the game is simple - double your population. Buy sources to generate electricity.")
        print("If you don't take care of your city, people will die. And you will never win.")
        print("Good luck!")
        print("")
        print("")
        print("")
        print("")
        # initializing all of the members of the class, including all of the qualities of the city.

        self.win = False
        self.population = randint(100, 50000)
        self.ogpop = self.population
        self.pollution = 0
        self.radiation = 0
        self.typecity = randint(1, 3)
        self.requiredenergy = self.population * 1000
        self.topographics = randint(0, 4000)
        self.money = self.population * 100 * (4 - self.typecity)
        self.rivers = randint(0, 10)
        self.openland = randint(100, 1000)
        self.coal = randint(100, 10000)
        self.natgas = randint(100, 10000)
        self.clouds = randint(0, 100)
        self.disasters = randint(0, 10)
        self.newtech = 0
        self.powerplants = 0
        self.advancedpowerplants = 0
        self.coalplants = 0
        self.advancedcoalplants = 0
        self.solarpanels = 0
        self.windturbines =0
        self.natgasplants = 0
        self.advancednatgasplants = 0
        self.dams = 0
        self.name = ""
        # many members are initialized, and they will all be used
        print("A new city has been created!")
        print("The qualities of this city are random, so do the best with what you've got.")
        print("")

    # displays the stats of the city; this is also an option under the menu when the program is running.

    def displaycity(self):
        pop = str(self.population)
        rad = str(self.radiation)
        poll = str(self.pollution)
        type = str(self.typecity)
        topo = str(self.topographics)
        mon = str(self.money)
        riv = str(self.rivers)
        openl = str(self.openland)
        coal = str(self.coal)
        nat = str(self.natgas)
        clo = str(self.clouds)
        dis = str(self.disasters)
        reqe = str(self.requiredenergy)
        # converting all of the integers to strings to display to the user that is easy to read
        print("Hello user, we will now display the statistics of your city.")
        print("Note that this city is randomly generated, so sometimes")
        print("You might be unlucky with your situation, other times not so much.")
        print("We will now display the stats of your city so that you can know what to expect:")
        # displaying the important parts of the city, such as the people, pollution, money, radiation, and basic
        # stats about the city. Very important
        print(self.name + " has:")
        print(pop + " people")
        print(poll + " pollution")
        print(rad + " radiation")
        print(type + " is the level of the city, where 3 indicates the least developed and one is the most developed.")
        print(topo + " topographical rating")
        print(mon + " dollars")

        if riv == "1":
            print(riv + "river")

        else:
            print(riv + " rivers")

        print(openl + "  square kilometers of open land")
        print(coal + " tons of coal")
        print(nat + " tons of natural gas")
        print(clo + " cloud rating")
        print(dis + " disaster rating.")
        print("Lastly, there is " + reqe + " watts of required energy for the city.")
        print("----------------------------------------")
        name = input("Press any key and ENTER to continue.")
        self.Menu()


    # allows the user to set a name to their city
    def namer(self):
        name = input("What do you want the name of your city to be? ")
        self.name = name
        print("Name successfully changed to " + self.name + "!")




    # the exit method, which can be found througb the menu, it returns 0 and also tells the
    # user if they have won the game, there is no reward except the joy of winning the game

    def exit(self):
        print("Exit successful.")
        if self.win == True:
            print("We are sorry to see that you are leaving")
            print("But, you did well, and you were good enough to win.")
            print("Good job, see you later.")


        else:
            print("See you, looks like you did not win yet, but come and play again.")
            print("None of your progress will be saved.")



    # this method is automatically applied at the end of the disaster wheel (to be explained later in the code)
    # determines if there are still people alive in the city.

    def alldead(self):

        if self.population <= 0:
            print("Everyone is dead. Game over.")

            # code for quitting the whole program when everyone is dead

            quit()

        else:
            stralive = str(self.population)
            print("You have " + stralive + " people alive in your city.")




    # the most complex of the methods in this program


    def disasterwheel(self):
        self.distarray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.alldisasters = ["Tornado strikes!", "Hurricane ravages your city!", "Big city fire!", "Volcanic eruption!", "Explosion of gas station!", "Flash floods!"]
        # this for loop ensures that if the disaster rating is higher, than the distarray will have
        # more 1's
        # this way, if a random index in the distarray is a 1, then there will be a disaster,
        # so chances are that having a higher disaster rating will lead to a more likely disaster
        for i in range(0, self.disasters):
            self.distarray[i] = 1
        rando = randint(0, 30)
        reso = self.distarray[rando]

        if reso == 1:
            print("Disaster strikes!")
            print("")
            print("")
            print("DISASTER!!!!!")
            print("")
            print("")
            print("ALERT!!!")
            print("")
            print("")

            # selects a random disaster from all of the disasters to occur, like a tornado

            # based on the index of the random value of newdisaster, prints out the disaster
            # and selects a random amount of people to die based on the severity of the diaster

            # ex: Hurricanes can be more ravaging and destructive than tornadoes

            newdisaster = randint(0, 5)
            if newdisaster == 0:
                print(self.alldisasters[newdisaster])
                deaths = randint(10, 100)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                # checks to see if everyone is dead in the city
                self.alldead()

            elif newdisaster == 1:
                print(self.alldisasters[newdisaster])
                deaths = randint(20, 2500)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                self.alldead()

            elif newdisaster == 2:
                print(self.alldisasters[newdisaster])
                deaths = randint(100, 1000)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                self.alldead()

            elif newdisaster == 3:
                print(self.alldisasters[newdisaster])
                deaths = randint(1000, 4000)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                self.alldead()

            elif newdisaster == 4:
                print(self.alldisasters[newdisaster])
                deaths = randint(3, 100)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                self.alldead()

            elif newdisaster == 5:
                print(self.alldisasters[newdisaster])
                deaths = randint(10, 1000)
                printdeaths = str(deaths)
                self.population = self.population - deaths
                print("Sadly, " + printdeaths + " people died in this disaster.")
                self.alldead()


        else:
            # happens if the random value is not 1, so it's 0, so no disaster
            print("No disaster this time.")

    # updates the user with all of the important information to win the game, such as the
    # the pollution, rivers left for dams, radiation, technology, required energy, coal, natural gas
    # total plants and methods for electrical generation

    def current(self):
        moneys = str(self.money)
        required = str(self.requiredenergy)
        natgasleft = str(self.natgas)
        coalleft = str(self.coal)
        pol = str(self.pollution)
        rad = str(self.radiation)
        popu = str(self.population)
        lander = str(self.openland)
        riversleft = str(self.rivers)
        # deal with all of this in terms of strings
        powerplants = str(self.powerplants)
        adpowerplants = str(self.advancedpowerplants)
        coalplants = str(self.coalplants)
        adcoalplants = str(self.advancedcoalplants)
        solarpanels = str(self.solarpanels)
        windturbines = str(self.windturbines)
        ngplants = str(self.natgasplants)
        adgpl = str(self.advancednatgasplants)
        dams = str(self.dams)
        techs = str(self.newtech)

        # asks if the user wants to see the current state of the city
        valid = False
        while valid == False:
            answer = input("Would you like to see the current state of your city? ")
            if answer == "yes" or answer == "Yes" or answer == "y" or answer == "ye":
                print("Here is your current city:")
                print(self.name + " is the CITY!")
                print("--------------------------")
                print("People: " + popu + ", Required energy: " + required + " watts.")
                print("Money: " + moneys + " dollars and " + lander + " square kilometers of open land.")
                print("Rivers Left: " + riversleft)
                print(coalleft + " tons of coal left and " + natgasleft + " tons of natural gas left.")
                print("-----------------ENERGY PRODUCTION--------------")
                print(powerplants + " powerplants ------- " + adpowerplants + " advanced power plants")
                print(coalplants + " coal plants --------- " + adcoalplants + " advanced coal plants")
                print(ngplants + " natural gas plants --------- " + adgpl + " advanced natural gas plants")
                print(solarpanels + " solar panels")
                print(windturbines + " wind turbine sets")
                print(dams + " hydroelectric dams")
                print("-----------ENVIRONMENTAL STATS---------")
                print(pol + " tons of greenhouse gas emissions")
                print(rad + " tons of radiation nuclear emissions")
                print("---------------TECHNOLOGY--------------")
                print(techs + " items of greenhouse gas emission technologies")


                valid = True
            elif answer == "no":
                print("Nothing has happened.")
                valid = True
            else:
                print("Try again. Type a valid answer in.")
        print("----------------------------------------")
        name = input("Press any key and ENTER to continue.")
        # goes back the menu
        self.Menu()

    # buys a nuclear plant

    def buynucplant(self):
        # spins the wheel of disasters to see if disaster strikes!

        self.disasterwheel()

        print("A nuclear power plant costs 10,000 dollars")
        if self.money <10000 or self.openland < 10:
            # if the money is too low, or there is no land, nothing will happen.
            print("Not enough money/land, you have less than 10,000 dollars.")
            print("Try to do something else.")
        else:
            # if the user can afford it and there is enough land, it is bought
            self.powerplants = self.powerplants + 1

            print("Purchase successful!")
            if self.money < 5000:
                # low money
                print("Looks like you do not have much money left, be careful.")

            # reduces land, money, required energy and increases radiation
            self.openland = self.openland - 10
            self.money = self.money - 10000
            self.radiation = self.radiation + 100
            self.requiredenergy = self.requiredenergy - 100000
            if self.requiredenergy <= 0:
                # a lot of energy leads to population, money, but greater demand for money
                print("You have more energy than enough to sustain your population.")
                print("The population will grow.")
                print("")
                print("Every time you buy a plant, the population will grow, but will increase required energy.")
                print("In fact, the population will go up by 50, and the required energy increases by 50000.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (5000 * (4 - self.typecity))
                print("However, the amount of money received depends slightly on the level of your city.")
                self.population = self.population + 50
                self.requiredenergy = self.requiredenergy + 50000
            if self.openland < 40:
                # little land left
                print("You don't have a lot of land left.")
            if self.radiation >= 4000:
                # too much radiation, kills 500 people, checks to see if the city is still alive
                print("The radiation is rather high, and people will die from this radiation.")
                print("YOU WERE WARNED.")
                self.population = self.population - 500
                self.alldead()
                print("Every time you buy something, more people will die.")
                print("You can shut down the plant, with no refund, though.")
                valid = False
                while valid == False:
                    answer = input("If you want to type yes or no: ")
                    if answer == "yes":
                        print("Power plant shut down.")
                        # if user wants to delete power plant, the radiation goes down
                        # but the required energy goes up
                        # no refunds on money or land, it's not like, in the real world,
                        # they can get back the money out of thin air
                        self.powerplants = self.powerplants - 1
                        self.radiation = self.radiation - 100
                        self.requiredenergy = self.requiredenergy + 100000
                        valid = True
                    elif answer == "no":
                        print("Nothing has happened, more people will die.")
                        valid = True
                    else:
                        print("Try again. Type a valid answer in.")
            if self.newtech > 0:
                print("Looks like you have advancements in technology to reduce your radiation")
                print("On nuclear power plants. Would you like to use one?")
                good = False
                while good == False:
                    answer = input("Type in yes or no: ")
                    if answer == "yes":

                        self.newtech = self.newtech - 1
                        # decreases new technology by one and power plants by one as well
                        # but also increases the amount of advanced power plants by one
                        # decreases radiation by 505
                        self.powerplants = self.powerplants -1
                        self.advancedpowerplants = self.advancedpowerplants + 1
                        self.radiation = self.radiation - 75

                        print("Now this coal plant is advanced and only produces 25 rating for radiation!")
                        good = True
                    elif answer == "no":
                        print("Alright, sounds good. OK.")
                        good = True
                    else:
                        print("Try again. Type a valid answer in.")
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        # will enable the user to see their progress
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        # back to menu

        self.Menu()



    # buys a coal plant
    def buycoalplant(self):
        self.disasterwheel()
        # diasters
        print("A coal power plant costs 5,000 dollars.")
        if self.money < 5000 or self.openland < 8 or self.coal < 50:
            print("Not enough money/land/coal yet. Sorry.")
            # sees if user can buy this
        else:
            self.coalplants = self.coalplants + 1
            print("Purchase successful!")
            # depletes amount of coal by 50, it is a non-renewable resource, after all
            self.coal = self.coal - 50

            self.openland = self.openland - 8
            self.money = self.money - 5000
            self.pollution = self.pollution + 100
            self.requiredenergy = self.requiredenergy - 30000
            if self.money <= 2500:
                print("You have very little money left, be careful.")
            if self.requiredenergy <= 0:
                # if there is more than enough energy, the population will grow to meet it and exceed the needs
                # also more money is given with more people having jobs
                # but higher level city will lead to more money
                print("You have more than enough energy for your population.")
                print("So every time you buy a plant, the population could grow.")
                print("")
                print("Every time you buy a plant, the population will grow, but will increase required energy.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (1500 * (4 - self.typecity))

                print("In fact, the population will go up by 15, and the required energy increases by 515000.")
                self.population = self.population + 15
                self.requiredenergy = self.requiredenergy + 15000
            if self.openland < 40:
                print("You don't have a lot of land left.")
            if self.pollution >= 20000 and self.pollution <= 22000:
                print("You are in big trouble. The pollution is getting high, and the people are sick.")
                print("Because of this, the city has to invest money in treatment for these people.")
                self.money = self.money - 2500
                # loses money, not people, gives user option to shut down plant with no refunds on
                # money or land
                print("You lost 2500 dollars.")
                valid = False
                while valid == False:
                    answer = input("If you want shut down a coal plant to type yes or no: ")
                    if answer == "yes":
                        print("Coal plant shut down.")
                        self.coalplants = self.coalplants - 1
                        self.pollution = self.pollution - 100
                        self.requiredenergy = self.requiredenergy + 30000
                        valid = True
                    elif answer == "no":
                        print("Nothing has happened, things could go bad.")
                        valid = True
                    else:
                        print("Try again. Type a valid answer in.")

            if self.pollution > 22000:
                print("Oh no. Now the pollution is too high, people will die.")
                self.population = self.population - 250
                # people die if the pollution is too high
                self.alldead()
                good = False
                while good == False:
                    answer = input("If you want shut down a coal plant to type yes or no: ")
                    if answer == "yes":
                        print("Coal plant shut down.")
                        self.coalplants = self.coalplants - 1
                        self.pollution = self.pollution - 100
                        self.requiredenergy = self.requiredenergy + 30000
                        good = True
                    elif answer == "no":
                        print("Nothing has happened, things could go bad.")
                        good = True
                    else:
                        print("Try again. Type a valid answer in.")
            if self.newtech > 0:
                # gives users option to advance technology in one coal power plant and cut pollution
                # in half
                print("Looks like you have advancements in technology to reduce your pollution")
                print("On coal plants. Would you like to use one?")
                right = False
                while right == False:
                    answer = input("Type in yes or no: ")
                    if answer == "yes":
                        self.coalplants = self.coalplants -1
                        self.advancedcoalplants = self.advancedcoalplants + 1
                        self.newtech = self.newtech - 1
                        self.pollution = self.pollution - 75
                        print("Now this coal plant is advanced and only produces 25 rating for pollution!")
                        right = True
                    elif answer == "no":
                        print("Alright, sounds good. OK.")
                        right = True
                    else:
                        print("Try again. Type a valid answer in.")
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        self.Menu()


    # buys a natural gas plant

    def buynatgasplant(self):
        self.disasterwheel()
        print("A natural gas plant costs 8,000 dollars.")
        if self.money < 8000 or self.openland < 10 or self.natgas < 100:
            # sees if user meets all requirements to buy natural gas plant
            print("Not enough money/land/natural gas yet. Sorry.")
        else:
            self.natgasplants = self.natgasplants + 1
            print("Purchase successful!")
            # increases pollution, lowers required energy, lowers open land, natural gas resources, money when
            # the plant is bought
            self.natgas = self.natgas - 100

            self.openland = self.openland - 10
            self.money = self.money - 8000
            self.pollution = self.pollution + 50
            self.requiredenergy = self.requiredenergy - 30000
            if self.money <= 2500:
                print("You have very little money left, be careful.")
            if self.requiredenergy <= 0:

                # if there is more than enough energy, the population will grow to meet it and exceed the needs
                # also more money is given with more people having jobs
                # but higher level city will lead to more money
                print("You have more than enough energy for your population.")
                print("So every time you buy a plant, the population could grow.")
                print("")
                print("Every time you buy a plant, the population will grow, but will increase required energy.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (1500 * (4 - self.typecity))
                print("In fact, the population will go up by 15, and the required energy increases by 15000.")
                self.population = self.population + 15
                self.requiredenergy = self.requiredenergy + 15000
            if self.openland < 40:
                print("You don't have a lot of land left.")
            if self.pollution >= 20000 and self.pollution <= 22000:
                # if the pollution is dangerously high, but not fatally high
                print("You are in big trouble. The pollution is getting high, and the people are sick.")
                print("Because of this, the city has to invest money in treatment for these people.")
                # loses money
                self.money = self.money - 2500
                print("You lost 2500 dollars.")
                valid = False
                while valid == False:
                    answer = input("If you want shut down a natural gas plant to type yes or no: ")
                    if answer == "yes":
                        print("Natural gas plant shut down.")
                        # allows user to reduce all of the pollution from that plant but with no refund in terms of
                        # land or money
                        self.natgasplants = self.natgasplants - 1
                        self.pollution = self.pollution - 100
                        self.requiredenergy = self.requiredenergy + 30000
                        valid = True
                    elif answer == "no":
                        print("Nothing has happened, things could go bad.")
                        valid = True
                    else:
                        print("Try again. Type a valid answer in.")

            if self.pollution > 22000:
                # when the pollutions is too high, population goes down
                print("Oh no. Now the pollution is too high, people will die.")
                self.population = self.population - 250
                self.alldead()
                good = False
                while good == False:
                    answer = input("If you want shut down a natural gas plant to type yes or no: ")
                    if answer == "yes":
                        print("Natural gas plant shut down.")
                        self.natgasplants = self.natgasplants - 1
                        self.pollution = self.pollution - 100
                        self.requiredenergy = self.requiredenergy + 30000
                        good = True
                    elif answer == "no":
                        print("Nothing has happened, things could go bad.")
                        good = True
                    else:
                        print("Try again. Type a valid answer in.")
            if self.newtech > 0:
                # new tech for user, similar to coal plant
                print("Looks like you have advancements in technology to reduce your pollution")
                print("On natural gas plants. Would you like to use one?")
                right = False
                while right == False:
                    answer = input("Type in yes or no: ")
                    if answer == "yes":
                        self.natgasplants = self.natgasplants - 1
                        self.advancednatgasplants = self.advancednatgasplants + 1
                        self.newtech = self.newtech - 1
                        self.pollution = self.pollution - 47.5
                        print("Now this natural gas plant is advanced and only produces 47.5 rating for pollution!")
                        right = True
                    elif answer == "no":
                        print("Alright, sounds good. OK.")
                        right = True
                    else:
                        print("Try again. Type a valid answer in.")
                        # user must enter in a valid answer
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        # back to menu

        self.Menu()



    # buys solar panels

    def buysolarpanels(self):
        self.disasterwheel()
        print("A set of solar panels costs 4,000 dollars")
        print("Based on the topographical rating and cloud rating, this affects the energy generation.")
        if self.money < 4000 or self.openland <5:
            # if conditions are not met, panels will not be bought
            print("Not enough money/land")
        else:
            self.solarpanels = self.solarpanels + 1

            print("Purchase successful!")
            self.openland = self.openland - 5
            self.money = self.money - 4000
            if self.money <= 2500:
                print("You have very little money left, be careful.")
            # amount of energy received from solar energy is based on the topographical rating (higher is better)
            # and clouds covering the sun
            solaris = 20000 + self.topographics - self.clouds
            print("No refunds!")
            self.requiredenergy - self.requiredenergy - solaris

            if self.requiredenergy <= 0:
                # if there is more than enough energy, the population will grow to meet it and exceed the needs
                # also more money is given with more people having jobs
                # but higher level city will lead to more money

                print("You have more than enough energy for your population.")
                print("So every time you buy solar panels, the population could grow.")
                print("")
                print("Every time you buy solar panels, the population will grow, but will increase required energy.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (1300 * (4 - self.typecity))
                print("In fact, the population will go up by 13, and the required energy increases by 13000.")
                self.population = self.population + 13
                self.requiredenergy = self.requiredenergy + 13000
            if self.openland < 40:
                print("You don't have a lot of land left.")
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        # back to menu

        self.Menu()





    # buys wind turbines

    def buywindturbines(self):
        self.disasterwheel()
        print("A large wind turbine costs 6000 dollars.")

        if self.money < 6000 or self.openland < 10:
            print("Not enough money/land")
        else:
            self.windturbines = self.windturbines + 1

            print("Purchase successful!")
            self.openland = self.openland - 10
            self.money = self.money - 6000
            if self.money <= 2500:
                print("You have very little money left, be careful.")
            # higher topographical rating leads to more electrical generation from wind turbines
            windaris = 40000 + self.topographics
            print("No refunds!")
            self.requiredenergy - self.requiredenergy - windaris
            if self.requiredenergy <= 0:
                # if there is more than enough energy, the population will grow to meet it and exceed the needs
                # also more money is given with more people having jobs
                # but higher level city will lead to more money

                print("You have more than enough energy for your population.")
                print("So every time you buy wind turbines, the population could grow.")
                print("")
                print("Every time you buy wind turbines, the population will grow, but will increase required energy.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (2500 * (4 - self.typecity))
                print("In fact, the population will go up by 25, and the required energy increases by 25000.")
                self.population = self.population + 25
                self.requiredenergy = self.requiredenergy + 25000
            if self.openland < 40:
                print("You don't have a lot of land left.")
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        # back to menu

        self.Menu()





    # buys a hydroelectric dam

    def buydam(self):
        self.disasterwheel()

        print("A hydroelectric dam costs 30,000 dollars")
        print("If you do not have any rivers, though, no dams for you. ")
        if self.rivers == 0 or self.money <30000:
            print("You cannot build a dam, not enough money/not enough rivers left.")
        else:
            self.dams = self.dams + 1
            print("Purchase successful!")
            self.rivers = self.rivers - 1
            # one dam per river, so no rivers means no dams
            self.money = self.money - 30000
            print("No refunds!")
            self.requiredenergy = self.requiredenergy - 200000
            # lots of money but lots of energy given in return
            if self.requiredenergy <= 0:
                print("You have more than enough energy for your population.")
                print("So every time you buy dams, the population could grow.")
                print("")
                print("Every time you buy dams, the population will grow, but will increase required energy.")
                print("Since you have more people, the amount of money will also go up")
                self.money = self.money + (10000 * (4 - self.typecity))
                print("In fact, the population will go up by 100, and the required energy increases by 100000.")
                self.population = self.population + 100
                self.requiredenergy = self.requiredenergy + 100000
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        self.Menu()

        # back to menu



    # buys new technologies for fossil fuels

    def buytech(self):
        # if user has enough money, they can buy new tech and apply it to a coal or natural gas plant to
        # reduce the amount of pollution in the city
        print("Time to buy tech!")
        print("One piece of new technology costs 5,000 dollars.")
        if self.money < 5000:
            print("Looks like you cannot buy the technology. Sorry.")
        else:
            print("Nice, you can buy the new technology! This is good for your fossil fuel plants!")
            print("New tech successfully bought!")
            self.money = self.money - 5000
            self.newtech = self.newtech + 1
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")
        self.current()
        print("--------------------------")
        name = input("Press any key and ENTER to continue.")

        self.Menu()

        # back to the menu


    # is the menu

    def Menu(self):
        if self.population >= (2 * self.ogpop):
            self.win = True
            # checks to see if the user successfully doubled their population
            # if they did, then the user wins if they exit
        # gives all of the options in the program
        print("Here is the main menu screen for the energy city game. Here are the options:")
        print("Exit - 1")
        print("Buy Nuclear Power Plant (10,000 dollars) - 2")
        print("Buy Coal Power Plant (5,000 dollars) - 3")
        print("Buy Natural Gas Area (8,000 dollars) - 4")
        print("Buy Solar Panels (4,000 dollars) - 5")
        print("Buy Wind Turbines (6,000 dollars) - 6")
        print("Buy Hydroelectric Dam (30,000 dollars) - 7")
        print("Display Current City Stats - 8")
        print("Display BRIEF City Stats - 9")
        print("Buy New Technologies for Fossil Fuels (5,000 dollars) - 10")
        print("--------------------------")
        valid = False
        # the user must enter in a valid option
        while valid == False:

            # baed on the choice the user puts in, there are directed to a different method of the program
            # such as buying a nuclear power plant

            entry = input("Enter a choice between 1 and 10: ")
            if entry == "1":
                print("Exit, selected, good bye. No progress will be saved because this is a hardcore game.")
                self.exit()
                quit()

            elif entry == "2":
                print("A nuclear power plant will be bought.")
                self.buynucplant()
                valid = True

            elif entry == "3":
                print("A coal power plant will be bought.")
                self.buycoalplant()
                valid = True

            elif entry == "4":
                print("A natural gas area will be bought.")
                self.buynatgasplant()
                valid = True

            elif entry == "5":
                print("Solar panels will be bought.")
                self.buysolarpanels()
                valid = True

            elif entry == "6":
                print("Wind turbines will be bought.")
                self.buywindturbines()
                valid = True

            elif entry == "7":
                print("A hydroelectric dam will be bought, one per river.")
                self.buydam()
                valid = True

            elif entry == "8":
                print("We will now display the current status (full stats) of your randomly generated city.")
                self.displaycity()
                valid = True

            elif entry == "9":
                print("We will now display the stats, neatly ")
                self.current()
                valid = True

            elif entry == "10":
                print("Now to see if you can buy revolutionary new tech from the BAC!")
                self.buytech()
                valid = True

            else:
                print("Invalid choice selected, try again.")
            # the only way to leave the program is option 1, which is to exit






# money amounts for each object


def main():
    # is the main so that the game can be plaed

    Broomfield = City()
    Broomfield.namer()
    Broomfield.Menu()


if __name__ == '__main__':
    # ensures that the main will run
    main()
