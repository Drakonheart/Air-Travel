from Airport import *

class Flight(Airport): # (Airport) subclass!

    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):  # This how I check if these are objescts of Class Airport!
            # Initialized the instance variables _flightNo, _origin, and _destination:
            self.flightNo = flightNo
            self.origin = origin
            self.destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects") # If either or both are not Airport objects TypeError is raised!

    def __repr__(self):
        if self.isDomesticFlight() == True: # Using the domestic method I can tell if the flight from org to des is either domestic or international!

            flightType = "Domestic"
        else:
            flightType = "International"
        # The representation must be in the following format:
        return f"Flight: {self.getFlightNumber()} from {self.getOrigin().getCity()} to {self.getDestination().getCity()} " + "{%s}" %flightType

    def __eq__(self, other): # This method returns True if the origin and destination are the same for both Flights
        if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
            return True
        else:
            return False

    def isDomesticFlight(self): # Method that returns True if the flight is domestic, and returns False if the flight is international
        if self.getOrigin().getCountry() == self.getDestination().getCountry():
            return True # This is later used in in our __repr__ method
        else:
            return False # This is later used in in our  __repr__ method

    def getFlightNumber(self): # Getter that returns the Flight number code
        return self.flightNo

    def getOrigin(self): # Getter that returns the Flight origin
        return self.origin

    def getDestination(self): # Getter that returns the Flight destination
        return self.destination

    def setOrigin(self, origin): # Setter that sets (updates) the Flight origin
        self.origin = origin

    def setDestination(self, destination): # Setter that sets (updates) the Flight destination
        self.destination = destination





