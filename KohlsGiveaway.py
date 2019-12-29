from tkinter import* #Source for button with image GUI: http://www.pythonlake.com/tkinterbuttongrid
from tkinter import ttk
import tkinter as tk
import time
'''
Code Citations:
Entry box in line 434: https://www.youtube.com/watch?v=hst3AWjxF5o
Tkinter grid system. It's used in the buttons, labels, and the entry box. http://www.pythonlake.com/tkinterbuttongrid
How to include pictures in buttons and labels and how to edit the widgets. https://www.youtube.com/watch?v=a1Y5e-aGPQ4
Picture citations are in the code.
'''

createList = [] #Empty list to be filled with the items the user adds to their outfit.
namesList = []  #Includes the name of the outfit that the user creates. This list also includes "Example1" and "Example2".
votesList = []  #Empty list to be filled with votes corresponding to outfits in namesList
votesList2 = [] #Copy of votesList that will be reordered in ascending order to determine the winners.
priceTracker = 0 #Tracks the total cost of the outfit.
global winnerScore 
winnerScore = []
global winnerName
winnerName = []

def submittedPage(): #A new window that pops up when the user clicks "submit". This will show their submission and examples of other submissions.
    mytext = myEntry.get() #Gets the name of the user's outfit.
    Example1 = "Example 1"
    Example2 = "Example 2"
    namesList.append(mytext) #Adds the name of the user's outfit to a list.
    namesList.append(Example1)
    namesList.append(Example2)
    print("Submitted Outfits:",namesList)
    print("\n")
    print("Thanks for submitting", mytext +".")
    print("\n")
    HatIndex = len(createList) - 5 #References the first item (hat) the user chose at the top of the window.
    SunglassesIndex = len(createList) - 4 #References the second item (sunglasses) the user chose.
    ShirtIndex = len(createList) - 3 #References the third item (shirt) the user chose.
    PantsIndex = len(createList) - 2 #References the fourth item (pants) the user chose.
    ShoeIndex = len(createList) - 1  #References the fifth item (shoes) the user chose. The picture will be at the bottom.
    master.destroy() #Closes out the previous GUI.
    popup = tk.Tk() 
    popup.configure(background="#c9ddff")
    popup.wm_title("Your Submission and Examples")

    labelTitlePageTwo=Label(popup, text="Your Submission and Other Submissions", bg="#c9ddff", font="Times 32 underline bold", borderwidth=0)
    labelTitlePageTwo.grid(row=1, column=1, columnspan=3)

    labelOnePageTwo=Label(popup, text=mytext, fg= "red", bg="#c9ddff", font="Times 24 bold", borderwidth=0) #Displays the hat selected by the user.
    labelOnePageTwo.grid(row=2,column=1, sticky=N+E+S+W)
    UserHatSelection = PhotoImage(file=createList[HatIndex])
    ss1 = UserHatSelection.subsample(4,4)
    labelOnePageTwo.config(image=ss1,compound=BOTTOM)
    
    labelTwoPageTwo=Label(popup, bg="#c9ddff", borderwidth=0) #Displays sunglasses.
    labelTwoPageTwo.grid(row=3, column=1, sticky=N+E+S+W)
    UserSunglassesSelection = PhotoImage(file=createList[SunglassesIndex])
    ss2 = UserSunglassesSelection.subsample(4,4)
    labelTwoPageTwo.config(image=ss2,compound=BOTTOM)

    labelThreePageTwo=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shirt.
    labelThreePageTwo.grid(row=4, column=1, sticky=N+E+S+W)
    UserShirtSelection = PhotoImage(file=createList[ShirtIndex])
    ss3 = UserShirtSelection.subsample(4,4)
    labelThreePageTwo.config(image=ss3,compound=BOTTOM)

    labelFourPageTwo=Label(popup,bg="#c9ddff", borderwidth=0) #Displays pants.
    labelFourPageTwo.grid(row=5, column=1, sticky=N+E+S+W)
    UserPantsSelection = PhotoImage(file=createList[PantsIndex])
    ss4 = UserPantsSelection.subsample(4,4)
    labelFourPageTwo.config(image=ss4,compound=BOTTOM)

    labelFivePageTwo=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shoes.
    labelFivePageTwo.grid(row=6, column=2, sticky=N+E+S+W)
    UserShoeSelection = PhotoImage(file="images/converse.gif") #Image: https://image.dhgate.com/albu_269291508_00/1.0x0.jpg
    ss5 = UserShoeSelection.subsample(4,4)
    #labelFi/images/
    priceListTotal = priceTracker
    labelSixPageTwo=Label(popup, text= str("Total cost: $") + str(priceListTotal), bg="#c9ddff", fg="green", font="Times 16 bold", borderwidth=0)
    labelSixPageTwo.grid(row=7, column=1, sticky=N+E+S+W)

    

    Example1Label1=Label(popup, text="Example 1", fg= "red", bg="#c9ddff", font="Times 24 bold", borderwidth=0) #Example one's hat.
    Example1Label1.grid(row=2,column=2, sticky=N+E+S+W)
    E1HatSelection = PhotoImage(file="images/underarmour.gif") #Image: https://www.ddtexasoutfitters.com/shop/under-armour-mens-fish-hook-cap-82950)
    ss6 = E1HatSelection.subsample(4,4)
    Example1Label1.config(image=ss6,compound=BOTTOM)
    
    Example1Label2=Label(popup, bg="#c9ddff", borderwidth=0) #Displays sunglasses.
    Example1Label2.grid(row=3, column=2, sticky=N+E+S+W)
    E1SunglassesSelection = PhotoImage(file="images/mendota.gif") #Image: https://www.mendotaeyewear.com/shop/isthmus
    ss7 = E1SunglassesSelection.subsample(4,4)
    Example1Label2.config(image=ss7,compound=BOTTOM)

    Example1Label3=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shirt.
    Example1Label3.grid(row=4, column=2, sticky=N+E+S+W)
    E1ShirtSelection = PhotoImage(file="images/dri.gif") #Image: https://www.forrunnersbyrunners.com/nike-dri-fit-knit-ss-top.html)
    ss8 = E1ShirtSelection.subsample(4,4)
    Example1Label3.config(image=ss8,compound=BOTTOM)

    Example1Label4=Label(popup,bg="#c9ddff", borderwidth=0) #Displays pants.
    Example1Label4.grid(row=5, column=2, sticky=N+E+S+W)
    E1PantsSelection = PhotoImage(file="images/blackshorts.gif") #Image: https://www.shirtstop.us/armani-martillo-dress-shorts-603s.html
    ss9 = E1PantsSelection .subsample(4,4)
    Example1Label4.config(image=ss9,compound=BOTTOM)

    Example1Label5=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shoes.
    Example1Label5.grid(row=6, column=1, sticky=N+E+S+W)
    E1ShoeSelection = PhotoImage(file="images/converse.gif") #Image: https://image.dhgate.com/albu_269291508_00/1.0x0.jpg
    ss10 = E1ShoeSelection.subsample(4,4)
    Example1Label5.config(image=ss10,compound=BOTTOM)

    Example1Price=Label(popup, text= str("Total cost: $150"), bg="#c9ddff", fg="green", font="Times 16 bold", borderwidth=0)#Displays the cost for this outfit.
    Example1Price.grid(row=7, column=2, sticky=N+E+S+W)


    Example2Label1=Label(popup, text="Example 2", fg= "red", bg="#c9ddff", font="Times 24 bold", borderwidth=0) #Example two's hat.
    Example2Label1.grid(row=2,column=3, sticky=N+E+S+W)
    E2HatSelection = PhotoImage(file="images/suess.gif") #Image: http://partycity5.scene7.com/is/image/PartyCity/732768?wid=400
    ss11 = E2HatSelection.subsample(4,4)
    Example2Label1.config(image=ss11,compound=BOTTOM)
    
    Example2Label2=Label(popup, bg="#c9ddff", borderwidth=0) #Displays sunglasses.
    Example2Label2.grid(row=3, column=3, sticky=N+E+S+W)
    E2SunglassesSelection = PhotoImage(file="images/beach.gif") #Image: http://makamaka.es/product/sunglasses/
    ss12 = E2SunglassesSelection.subsample(4,4)
    Example2Label2.config(image=ss12,compound=BOTTOM)

    Example2Label3=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shirt.
    Example2Label3.grid(row=4, column=3, sticky=N+E+S+W)
    E2ShirtSelection = PhotoImage(file="images/dressshirt.gif") #Image: https://www.jcpenney.com/p/stafford-travel-performance-super-shirt/1cca9b9?pTmplType=regular
    ss13 = E2ShirtSelection.subsample(4,4)
    Example2Label3.config(image=ss13,compound=BOTTOM)

    Example2Label4=Label(popup,bg="#c9ddff", borderwidth=0) #Displays pants.
    Example2Label4.grid(row=5, column=3, sticky=N+E+S+W)
    E2PantsSelection = PhotoImage(file="images/dresspants.gif") #Image: https://bonobos.com/shop/pants-and-bottoms/dress-pants
    ss14 = E2PantsSelection.subsample(4,4)
    Example2Label4.config(image=ss14,compound=BOTTOM)

    Example2Label5=Label(popup,bg="#c9ddff", borderwidth=0) #Displays shoes.
    Example2Label5.grid(row=6, column=3, sticky=N+E+S+W)
    E2ShoeSelection = PhotoImage(file="images/option4.gif") #Image: https://scene7.josbank.com/is/image/JosBank/40TZ_18_JOSEPH_A_BANK_MAPLE_MAIN?$browse_thumbnail$?$browse_thumbnail$
    ss15 = E2ShoeSelection.subsample(4,4)
    Example2Label5.config(image=ss15,compound=BOTTOM)

    Example2Price=Label(popup, text= str("Total cost: $225"), bg="#c9ddff", fg="green", font="Times 16 bold", borderwidth=0)#Displays the cost for this outfit.
    Example2Price.grid(row=7, column=3, sticky=N+E+S+W)


    popup.mainloop()

def CalculateandPublishResults(winnerNumber): #Calculates the winners and prints the winners.  
    votesList2.sort(key=int)
    winnerIndex = len(votesList2) - winnerNumber
    winnerScore.append(votesList2[winnerIndex])
    winnerCorrespondingIndex = votesList.index(winnerScore[winnerNumber-1]) #Based on the rearranged list
    winnerName.append(namesList[winnerCorrespondingIndex]) #Name of the outfit that won based on the index number.

    if winnerNumber == 1:
        print("The grand prize winner is", winnerName[0] , "with a total of", winnerScore[0], "votes. The submitter has earned $100 to spend at our store! If you would like to buy this outfit, it costs $",priceTracker)
    elif winnerNumber == 2:
        print("The second place winner is", winnerName[1] , "with a total of", winnerScore[1], "votes. The submitter has earned $90 to spend at our store!")
    else:
        print("The third place winner is", winnerName[2] , "with a total of", winnerScore[2], "votes. The submitter has earned $80 to spend at our store!")
        
def add(item): #Adds the item to the outfit's list, adds an integer to the price tracker, and defines the price tracker as a string.
    global priceTracker
    if item == 1:
        MiDirectory = "images/None.gif" #Image: http://gallery.mobile9.com/asf/aCTH0IXRFPsm/none/
        createList.append(MiDirectory)
        priceTracker += 0
        CurrentTotalValue = str(priceTracker)
        
    elif item == 2:
        Mi2Directory = "images/GrayHat.gif" #Image: https://www.tilley.com/us_en/men/hats/snap-up-brim.html
        createList.append(Mi2Directory)
        priceTracker += 35
        CurrentTotalValue = str(priceTracker)   

    elif item == 3:
        Mi3Directory = "images/underarmour.gif" #Image: https://www.ddtexasoutfitters.com/shop/under-armour-mens-fish-hook-cap-82950
        createList.append(Mi3Directory)
        priceTracker += 20
        CurrentTotalValue = str(priceTracker)

    elif item == 4:
        Mi4Directory = "images/suess.gif" #Image: http://partycity5.scene7.com/is/image/PartyCity/732768?wid=400
        createList.append(Mi4Directory)
        priceTracker += 15
        CurrentTotalValue = str(priceTracker)

    if item == 5: 
        Mi5Directory = "images/None.gif" #Image: http://gallery.mobile9.com/asf/aCTH0IXRFPsm/none/
        createList.append(Mi5Directory)
        priceTracker += 0
        CurrentTotalValue = str(priceTracker)
        
    elif item == 6:
        Mi6Directory = "images/purdy.gif" #Image: https://roypurdy-glasses.com/product/glasses/
        createList.append(Mi6Directory)
        priceTracker += 15
        CurrentTotalValue = str(priceTracker)

    elif item == 7:
        Mi7Directory = "images/mendota.gif" #Image: https://www.mendotaeyewear.com/shop/isthmus
        createList.append(Mi7Directory)
        priceTracker += 40
        CurrentTotalValue = str(priceTracker)

    elif item == 8:
        Mi8Directory = "images/beach.gif" #Image: http://makamaka.es/product/sunglasses/
        createList.append(Mi8Directory)
        priceTracker += 30
        CurrentTotalValue = str(priceTracker)

    if item == 9:
        Mi9Directory = "/images/dri.gif" #Image: https://www.forrunnersbyrunners.com/nike-dri-fit-knit-ss-top.html
        createList.append(Mi9Directory)
        priceTracker += 50
        CurrentTotalValue = str(priceTracker)

    elif item == 10:
        Mi10Directory = "images/Tux.gif" #Image: https://www.etsy.com/listing/111416407/boys-tuxedo-shirt-kids-tux-tee-kids-size
        createList.append(Mi10Directory)
        priceTracker += 12
        CurrentTotalValue = str(priceTracker)

    elif item == 11:
        Mi11Directory = "images/gold.gif" #Image: https://browze.com/2017-camisa-masculina-men-39-s-elastic-shirts-slim-fit-fashion-stylish-shiny-shirt-mens-shirts-long-sleeve-homme-clothing-18655
        createList.append(Mi11Directory)
        priceTracker += 75
        CurrentTotalValue = str(priceTracker)

    elif item == 12:
        Mi12Directory = "images/dressshirt.gif" #Image: https://www.jcpenney.com/p/stafford-travel-performance-super-shirt/1cca9b9?pTmplType=regular
        createList.append(Mi12Directory)
        priceTracker += 80
        CurrentTotalValue = str(priceTracker)

    if item == 13:
        Mi13Directory = "images/northface.gif" #Image: https://www.thenorthface.com/shop/mens-pants-shorts-shorts/mens-straight-paramount-30-short-ch6a?variationId=NXJ#hero=0
        createList.append(Mi13Directory)
        priceTracker += 35
        CurrentTotalValue = str(priceTracker)

    elif item == 14:
        Mi14Directory = "images/blackshorts.gif" #Image: https://www.shirtstop.us/armani-martillo-dress-shorts-603s.html
        createList.append(Mi14Directory)
        priceTracker += 20
        CurrentTotalValue = str(priceTracker)

    elif item == 15:
        Mi15Directory = "images/dresspants.gif" #Image: https://bonobos.com/shop/pants-and-bottoms/dress-pants
        createList.append(Mi15Directory)
        priceTracker += 60
        CurrentTotalValue = str(priceTracker)
        
    elif item == 16:
        Mi16Directory = "images/joggers.gif" #Image: https://uniqlo.scene7.com/is/image/UNIQLO/goods_03_183508?$detail$
        createList.append(Mi16Directory)
        priceTracker += 20
        CurrentTotalValue = str(priceTracker)

    if item == 17:
        Mi17Directory = "images/converse.gif" #Image: https://image.dhgate.com/albu_269291508_00/1.0x0.jpg
        createList.append(Mi17Directory)
        priceTracker += 30
        CurrentTotalValue = str(priceTracker)

    elif item == 18:
        Mi18Directory = "images/dressshoes.gif" #Image: https://www.belk.com/shoes/mens-shoes/dress-shoes/
        createList.append(Mi18Directory)
        priceTracker += 50
        CurrentTotalValue = str(priceTracker)

    elif item == 19:
        Mi19Directory = "images/option4.gif" #Image: https://scene7.josbank.com/is/image/JosBank/40TZ_18_JOSEPH_A_BANK_MAPLE_MAIN?$browse_thumbnail$?$browse_thumbnail$
        createList.append(Mi19Directory)
        priceTracker += 30
        CurrentTotalValue = str(priceTracker)
        
    elif item == 20:
        Mi20Directory = "images/ugh boots.gif" #Image: https://www.larizia.com/shoes-c248/classic-short-ii-chestnut-twinface-boot-p87661
        createList.append(Mi20Directory)
        priceTracker += 80
        CurrentTotalValue = str(priceTracker)

    text = str("Current Total: $") 
    print(text + CurrentTotalValue) #Prints the total cost of the outfit as the user is selecting their outfit.
    print("\n") #Prints a line with no text.

def DesignContest(): #Algorithm for Creating outfits, submitting, voting, calculating the winners, and viewing them.
    start.destroy() #Exits start menu GUI that is found at the bottom of this file.
    print("Welcome to the Contest!") #Prints after the user clicks on the "Enter" button.
    print("\n") 
    season = True #The event continues to run until the season is over. The host can end the event.
    SubmitOutfitPhase = True #Used to indicate that the submitting phase of the event is still going on.
    while season == True: #This while loop will continue to run until the event or season ends.
        choice = input("Would you like to create and submit your outfit or vote on an existing one? Please type either 'create' or 'vote':")
        print("\n")
        if choice == "create": #A GUI with all of the items will pop up if the user types "create".
            global master        
            master = Tk()
            master.title("Create your own outfit!")
            master.configure(background="#c9ddff")
            master.geometry("550x700")
        
            mi = PhotoImage(file="images/GrayHat.gif") #A button that can be clicked to add a hat.
            button1 = Button(master,text="Add #2", fg= "black", bg= "#c9ddff", font="Times 16 bold", command = lambda: add(2))
            button1.grid(row=1,column=2, sticky=N+E+S+W)
            tmi = mi.subsample(4,4) #Shrinks the image.
            button1.config(image=tmi,compound=TOP) #The picture will go on top of the text.

            button2 = Button(master, text="No hat add #1", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda : add(1))
            button2.grid(row=1,column=1,sticky=N+E+S+W)
            mi2 = PhotoImage(file="images/None.gif")
            tmi2 = mi2.subsample(4,4)
            button2.config(image=tmi2,compound=TOP)

            button3 = Button(master,text="Add #3", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(3))
            button3.grid(row=1,column=3, sticky=N+E+S+W)
            mi3 = PhotoImage(file="images/underarmour.gif")
            tmi3 = mi3.subsample(4,4)
            button3.config(image=tmi3,compound=TOP)

            button4 = Button(master,text="Add #4", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(4))
            button4.grid(row=1,column=4, sticky=N+E+S+W)
            mi4 = PhotoImage(file="images/suess.gif")
            tmi4 = mi4.subsample(4,4)
            button4.config(image=tmi4,compound=TOP)

            button5 = Button(master,text="Add #20", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(20))
            button5.grid(row=5,column=4, sticky=N+E+S+W)
            mi5 = PhotoImage(file="images/ugh boots.gif")
            tmi5=mi5.subsample(4,4)
            button5.config(image=tmi5,compound=TOP)
            
            button6 = Button(master,text="Add #11", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(10))
            button6.grid(row=3,column=3, sticky=N+E+S+W)
            mi6 = PhotoImage(file="images/Tux.gif")
            tmi6 = mi6.subsample(4,4)
            button6.config(image=tmi6,compound=TOP)

            button7 = Button(master,text="Add #6", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(6))
            button7.grid(row=2,column=2, sticky=N+E+S+W)
            mi7 = PhotoImage(file="images/purdy.gif")
            tmi7 = mi7.subsample(4,4)
            button7.config(image=tmi7,compound=TOP)

            button8 = Button(master,text="Add #7", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(7))
            button8.grid(row=2,column=3, sticky=N+E+S+W)
            mi8 = PhotoImage(file="images/mendota.gif")
            tmi8 = mi8.subsample(4,4)
            button8.config(image=tmi8,compound=TOP)

            button9 = Button(master,text="Add #8", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(8))
            button9.grid(row=2,column=4, sticky=N+E+S+W)
            mi9 = PhotoImage(file="images/beach.gif")
            tmi9 = mi9.subsample(4,4)
            button9.config(image=tmi9,compound=TOP)

            button10 = Button(master,text="Add #18", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(18))
            button10.grid(row=5,column=2, sticky=N+E+S+W)
            mi10 = PhotoImage(file="images/dressshoes.gif")
            tmi10 = mi10.subsample(4,4)
            button10.config(image=tmi10,compound=TOP)

            button11 = Button(master,text="No sunglasses add #5", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(5))
            button11.grid(row=2,column=1, sticky=N+E+S+W)
            mi11 = PhotoImage(file="images/None.gif")
            tmi11 = mi11.subsample(4,4)
            button11.config(image=tmi11,compound=TOP)

            button12 = Button(master,text="Add #10", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(11))
            button12.grid(row=3,column=2, sticky=N+E+S+W)
            mi12 = PhotoImage(file="images/gold.gif")
            tmi12 = mi12.subsample(4,4)
            button12.config(image=tmi12,compound=TOP)

            button13 = Button(master,text="Add #9", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(9))
            button13.grid(row=3,column=1, sticky=N+E+S+W)
            mi13 = PhotoImage(file="images/dri.gif")
            tmi13 = mi13.subsample(4,4)
            button13.config(image=tmi13,compound=TOP)

            button14 = Button(master,text="Add #12", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(12))
            button14.grid(row=3,column=4, sticky=N+E+S+W)
            mi14 = PhotoImage(file="images/dressshirt.gif")
            tmi14 = mi14.subsample(4,4)
            button14.config(image=tmi14,compound=TOP)

            button15 = Button(master,text="Add #19",fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(19))
            button15.grid(row=5,column=3, sticky=N+E+S+W)
            mi15 = PhotoImage(file="images/option4.gif")
            tmi15 = mi15.subsample(4,4)
            button15.config(image=tmi15,compound=TOP)

            button16 = Button(master,text="Add #13", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(13))
            button16.grid(row=4,column=1, sticky=N+E+S+W)
            mi16 = PhotoImage(file="images/northface.gif")
            tmi16 = mi16.subsample(4,4)
            button16.config(image=tmi16,compound=TOP)

            button17 = Button(master,text="Add #14", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(14))
            button17.grid(row=4,column=2, sticky=N+E+S+W)
            mi17 = PhotoImage(file="images/blackshorts.gif")
            tmi17 = mi17.subsample(4,4)
            button17.config(image=tmi17,compound=TOP)

            button18 = Button(master,text="Add #15", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(15))
            button18.grid(row=4,column=3, sticky=N+E+S+W)
            mi18 = PhotoImage(file="images/dresspants.gif")
            tmi18 = mi18.subsample(4,4)
            button18.config(image=tmi18,compound=TOP)

            button19 = Button(master,text="Add #16", fg='black', bg="#c9ddff", font="Times 16 bold", command = lambda: add(16))
            button19.grid(row=4,column=4, sticky=N+E+S+W)
            mi19 = PhotoImage(file="images/joggers.gif")
            tmi19 = mi19.subsample(4,4)
            button19.config(image=tmi19,compound=TOP)

            button20 = Button(master,text="Add #17", fg="black", bg="#c9ddff", font="Times 16 bold", command = lambda: add(17))
            button20.grid(row=5,column=1, sticky=N+E+S+W)
            mi20 = PhotoImage(file="images/converse.gif")
            tmi20 = mi20.subsample(4,4)
            button20.config(image=tmi20,compound=TOP)

            labelSubmitGUI = Label(master, text="Outfit name:",fg="black", bg="#c9ddff", font="Times 20 bold", borderwidth=0)
            labelSubmitGUI.grid(row=6,column=1, sticky=N+E+S+W)
            
            global myEntry
            myEntry = StringVar()
            entryButton21 = Entry(master,textvariable=myEntry) #Gets the outfit's name.
            entryButton21.grid(row=6, column=2, columnspan=2, sticky=E+W)
            
            button22 = Button(master,text="Submit",fg="black", bg="#c9ddff", font="Times 16 bold", command = submittedPage) #Redirects user to the submitted page.
            button22.grid(row=6,column=4, sticky=N+E+S+W)

            master.mainloop()
            
        elif choice == "vote": #Transitions into the voting phase.
            if SubmitOutfitPhase == True:
                SubmitOutfitPhase = False
                for number in namesList: #Adds as many zeros to the votes list depending on the number of outfits submitted. 
                    votesList.append(0)
                    votesList2.append(0)
            if len(namesList) == 0:
                print("No outfits have been submitted yet. Please try again later.")
                print("\n")
            else:
                vote = input("What is the name of the outfit you would like to vote for?:")
                print("\n")
                if vote in namesList: #If outfit has truly been submitted.
                    voteIndex = namesList.index(vote) #Take index of outfit name.
                    votesList[voteIndex] += 1 #Add 1 vote to outfit.
                    votesList2[voteIndex] += 1 #Copy of votesList that will be in ascending order.
                    print ("Thanks for voting in our contest!")
                    print("\n")
                
        
                elif vote == "super secret event code":  #If someone (the host) types "super secret event code" and enters the correct password, the event will end and the results will be printed.  
                    eventPassword = input("What is the super secret event code?")
                    print("\n")
                    if eventPassword == "password":
                        season = False
                        print("The season has ended and the results will be calculated and released.")
                        print("\n")
                        CalculateandPublishResults(1)
                        time.sleep(1)
                        CalculateandPublishResults(2)
                        time.sleep(1)
                        CalculateandPublishResults(3)
                        time.sleep(1)
                    else:
                        print("Wrong super secret event code. Sorry :(")
                        print("\n")
                else:
                    print("That outfit does not exist in our database. Please try again or submit a new outfit.") 
                    print("\n")               

        else:
            print("Type either 'create' or 'vote'. Please try again.")
            print("\n")
        
start = Tk()
start.title("Contest Start Button")
start.config(background="#c9ddff")
start.geometry("348x125")
startButton= Button(start, text="Enter", fg="#f73333", bg="#c9ddff", font="Times 24 bold", command=DesignContest)
startButton.configure(relief=RAISED)
startButton.grid(row=3, column=1, sticky=N+E+S+W)
startButtonlabel = Label(start, text="The top three outfits will recieve prizes!",fg="black", bg="#c9ddff", font="Times 16 bold", borderwidth=0)
startButtonlabel.grid(row=2, column=1, sticky=N+E+S+W)
startButtonTitle = Label(start, text="Seasonal Design Contest",fg="black", bg="#c9ddff", font="Times 20 underline bold", borderwidth=0)
startButtonTitle.grid(row=1, column=1, sticky=N+E+S+W)