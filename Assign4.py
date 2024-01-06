from Airport import *
from Flight import *
allAirports = [] # This will store all the Airport obj in list container
allFlights = {} # This will create flight obj in dic format!

def loadData(airportFile, flightFile): # Read in all the data from the airport file of the given name
    visited = [] # Will store "key(s)" for later use in the allFlights dic
    try:

        airFileContent = open(airportFile, "r")# Opens airportFile
        for line in airFileContent:
            airOrgnaizedLine = (line.replace("\n", "").replace("\t", "").replace("  ", "").replace(" ", "").split(",")) # Removes any whitespace from the outside of each portion of the line
            airportObj = Airport(airOrgnaizedLine[0], airOrgnaizedLine[2], airOrgnaizedLine[1]) # Extracts the information from each line and create an Airport object for each
            allAirports.append(airportObj)

        airFileContent.close() # Closes airFileContent (saves)

        flightFileContent = open(flightFile, "r") #Opens flightFile
        for line in flightFileContent:
            flightOrgnaizedLine = (line.replace("\n", "").replace("\t", "").replace("  ", "").replace(" ", "").split(",")) # Removes any whitespace from the outside of each portion of the line
            flightObj = Flight(flightOrgnaizedLine[0], getAirportByCode(flightOrgnaizedLine[1]), getAirportByCode(flightOrgnaizedLine[2]))  # Extracts the information from each line and create an Flight object for each
            if flightOrgnaizedLine[1] not in visited: # This Condtion is used to sort out the keys that we will use later which help us to add more [values] per that unique key!
                visited.append(flightOrgnaizedLine[1])
                allFlights[flightOrgnaizedLine[1]] = [flightObj] # Adding the key (origin code from flight obj) with its flight object as its [value]!
            else:
                allFlights[flightOrgnaizedLine[1]] += [flightObj] # If the key is already in the dic then we will add the additional flight obj (value) in that key

        flightFileContent.close() # Closes airFileContent(saves)

        return True

    except FileNotFoundError: # FileNotFoundError created in case the wrong file is provide for the method parameter!!!
        return False

def getAirportByCode(code): # Returns the Airport object that has the given code
    for airPortObj in allAirports:
        if code == airPortObj.getCode():
            return (airPortObj)
    return -1

def findAllCityFlights(city): # Returns a list that contains all Flight objects (given city)
    listFlightObj = [] # Here we will store the Flight objects
    for keys in allFlights:
        values = allFlights[keys] # The Value is the list of flight obj(s)
        for flightObj in values: # Each element/flight obj in flight obj list
            if flightObj.getOrigin().getCity() == city or flightObj.getDestination().getCity() == city: # All Flight objects that involve the given city either as the origin or the destination
                listFlightObj.append(flightObj)
    return listFlightObj

def findAllCountryFlights(country): # Returns a list that contains all Flight objects (given country)
    listFlightObj = [] # Here we will store the Flight objects
    for keys in allFlights:
        values = allFlights[keys] # The Value is the list of flight obj(s)
        for flightObj in values: # Each element/flight obj in flight obj list
            if flightObj.getOrigin().getCountry() == country or flightObj.getDestination().getCountry() == country: # All Flight objects that involve the given country either as the origin or the destination
                listFlightObj.append(flightObj)
    return listFlightObj

def findFlightBetween(origAirport, destAirport): # This function will check if there is a direct flight, single-hop connecting flight(s), or neither
    orig = origAirport.getCity() # This will determine the city associated with the origAirport
    des = destAirport.getCity() # This will determine the city associated with the destAirport
    desAndOrigin = [] # Will store destination and origin codes later used to determine duplicates(single-hop connecting flight(s))
    garbage = [] # Blank list for storing non-seeking destination and origin codes
    duplicates = [] # Important list storing duplicate destination and origin codes (you will see later that this list determines single-hop connecting flight)
    for flightObj in findAllCityFlights(orig):
        if flightObj.getOrigin().getCity() == orig and flightObj.getDestination().getCity() == des: # Checks if there is a direct flight from origAirport to destAirport.
            answer = f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
            return answer # Returns the seeked answer/info in the appropriated format
        elif flightObj.getOrigin().getCity() == orig: # Here we will also check if the flightObj (origin) city matches with the provided orig
            desAndOrigin.append(flightObj.getDestination().getCode()) # If so, we will store this for later use when trying to determine single-hop connecting flight

    for flightObj in findAllCityFlights(des):
        if flightObj.getDestination().getCity() == des: # Here we will also check if the flightObj (destination) city matches with the provided des
            desAndOrigin.append(flightObj.getOrigin().getCode())  # If so, we will store this for later use when trying to determine single-hop connecting flight

    for codes in desAndOrigin:
        if codes not in garbage:
            garbage.append(codes) # We store the non useful codes from our collected desAndOrigin in garbage list
        else:
            duplicates.append(codes) # And the duplicated codes will be stored in duplicates list (note that the duplicate code(s) indicate the possbile flight codes that are used for single-hop connecting flight)

    if len(duplicates) > 0: # If the duplicates list is greater than 0 (meaning there are single-hop connecting flight(s))
        return set(duplicates) # It will return a set of that list

    return -1 # If none of these conditions are met then this method will return -1 as an indication

def findReturnFlight(firstFlight): # This function will take the given Flight object and look for the Flight object representing the return flight from that given flight!
    for key in allFlights:
        value = allFlights.get(key) # Initializing the key values for the [value(s)] list
        for flightObj in value: # flightObj in [value(s)]
            if flightObj.getOrigin().getCode() == firstFlight.getDestination().getCode() and flightObj.getDestination().getCode() == firstFlight.getOrigin().getCode(): # This will check if there are any other Flight object (or flights) that goes in the opposite direction!
                return (flightObj) # Returns that flight obj (or flight).
    return -1 # If not, then it is indicated by -1


