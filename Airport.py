class Airport: # creating airport class
   def __init__(self, code, city, country): # Initialized the instance variables _code, _city, and _country with a constructor
       self._code = code
       self._city = city
       self._country = country

   def __repr__(self): # This returns the representation of this class!
       return f"{self._code}({self._city}, {self._country})" # In appropriate format

   def getCode(self): # Getter that returns the Airport code
       return self._code

   def getCity(self): # Getter that returns the Airport city
       return self._city

   def getCountry(self): # Getter that returns the Airport country
       return self._country

   def setCity(self, city): # Setter that sets (updates) the Airport city
       self._city = city

   def setCountry(self, country): # Setter that sets (updates) the Airport country
       self._country = country

