# Pixel's Set Maplist Generator

# This program allows you to easily and quickly make a maplist for any scrim or set you may be taking part in.

# To put it simply, this program chooses the most popular mapmodes first, while never repeating a map.
# If all of the possible maps for a given mode are used up, it will just make sure to use a mapmode that hasn't been used yet.
# Once everything gets used up, the loop resets and you will get repeat mapmodes.

# This means you shouldn't get many repeats too close to each other - but if this happens you can of course just run the program again.

import random

szList = [  # Define 10 popular Splat Zones maps, split in to 3 lists with varying popularity
    [("SZ", "Hagglefish Market"), ("SZ", "Mahi-Mahi Resort"), ("SZ", "MakoMart"), ("SZ", "Um'ami Ruins")],
    [("SZ", "Barnacle & Dime"), ("SZ", "Robo ROM-en"), ("SZ", "Shipshape Cargo Co.")],
    [("SZ", "Brinewater Springs"), ("SZ", "Manta Maria"), ("SZ", "Urchin Underpass")]
]
tcList = [  # Define 7 popular Tower Control maps, split in to 3 lists with varying popularity
    [("TC", "Hagglefish Market"), ("TC", "Inkblot Art Academy"), ("TC", "Shipshape Cargo Co.")],
    [("TC", "MakoMart"), ("TC", "Undertow Spillway")],
    [("TC", "Museum d'Alfonsino"), ("TC", "Manta Maria")]
]
rmList = [  # Define 7 popular Rainmaker maps, split in to 3 lists with varying popularity
    [("RM", "Scorch Gorge"),("RM", "Undertow Spillway"),("RM", "Humpback Pump Track")],
    [("RM", "Museum d'Alfonsino"),("RM", "Crableg Capital")],
    [("RM", "Manta Maria"),("RM", "Robo ROM-en")]
]
cbList = [  # Define 7 popular Clam Blitz maps, split in to 3 lists with varying popularity
    [("CB", "Scorch Gorge"),("CB", "Museum d'Alfonsino"),("CB", "Barnacle & Dime")],
    [("CB", "Um'ami Ruins"),("CB", "Inkblot Art Academy")],
    [("CB", "Crableg Capital"),("CB", "MakoMart")]
]

valid = False  # Create an infinite loop until user inputs correctly
while not valid:
    gameCount = int(input("How many games total? "))
    szCount = int(input("How many Splat Zones maps? "))
    tcCount = int(input("How many Tower Control maps? "))
    rmCount = int(input("How many Rainmaker maps? "))
    cbCount = int(input("How many Clam Blitz maps? "))

    if (szCount+tcCount+rmCount+cbCount) == gameCount:
        valid = True  # Move on if game count equals total of mode counts...
    else:
        print("Your mode counts do not equal the total game count. Please retry.")  # ...loop if not

def makeMapList(mapList, gameCounts, crntCounts): # If a mode is being played add its list and ready lists
    if szCount > 0:
        mapList.append(szList)
        gameCounts.append(szCount)
        crntCounts.append(0)
    if tcCount > 0:
        mapList.append(tcList)
        gameCounts.append(tcCount)
        crntCounts.append(0)
    if rmCount > 0:
        mapList.append(rmList)
        gameCounts.append(rmCount)
        crntCounts.append(0)
    if cbCount > 0:
        mapList.append(cbList)
        gameCounts.append(cbCount)
        crntCounts.append(0)
    return mapList, gameCounts, crntCounts

mode = 0  # Initialise lists and variables needed
mapList = []
gameCounts = []
crntCounts = []
makeMapList(mapList, gameCounts, crntCounts)
setMaps = []
usedMaps = []
usedMapModes = []

for i in range(gameCount):  # Loop for length of set
    activeList = mapList[mode]  # Select a list, rotating between available modes
    chosen = False
    attempts = 1
    sublist = 0  # Start on the first category of maps

    while not chosen:  # Start loop to find a valid map
        sel = random.choice(activeList[sublist])  # Choose randomly from current sublist
        if sel[1] not in usedMaps: # If the map hasn't been used, add it to all applicable lists
            setMaps.append(sel)
            usedMaps.append(sel[1])
            usedMapModes.append(sel)
            chosen = True  # Set chosen to True to break out of the loop and move on to the next mapmode
        else:  # If the map has been used, repeat to find an unused map
            attempts += 1

        if attempts >= 50:  # Technically it's possible that a given map never gets rolled, but that's a 0.000000002% chance. Increase this number to make the chance even lower.
            sublist += 1  # If an unused map isn't found, move on to the next sublist to start rolling from slightly less popular maps
            attempts = 1

        if sublist > 2:  # If all three categories are searched with no available map, move on
            sublist = 0  # Reset variables for the next loop
            attempts = 1
            while not chosen:  # This code is mainly the same, except it just doesn't care if the map has already been used.
                sel = random.choice(activeList[sublist])
                if sel not in usedMapModes:  # Instead only check if the mapmode is used
                    setMaps.append(sel)
                    usedMapModes.append(sel)
                    chosen = True
                else:
                    attempts += 1

                if attempts == 50:
                    sublist += 1
                    attempts = 1

                if sublist > 2:  # If every mapmode has been used, then reset the used lists and repeat loop
                    sublist = 0
                    usedMaps = []
                    usedMapModes = []

    crntCounts[mode] += 1  # Add 1 to the amount of times the selected mode has been played
    if crntCounts[mode] == gameCounts[mode]:
        mapList.pop(mode)  # Removes the mode from the options if all of its games have been played
        gameCounts.pop(mode)
        crntCounts.pop(mode)
    mode += 1  # Increment counter to allow mode to rotate
    if mode == len(mapList):  # Resets mode to 0 if it goes above the number of modes being played
        mode = 0

print("Your set maplist is below!\n")
print(f"Set MapList: Bo{gameCount}")  # This and below is just formatting for when it prints the maplist.
for i in range(1, gameCount+1):
    print(f"{i}. {setMaps[i-1][0]} {setMaps[i-1][1]}")