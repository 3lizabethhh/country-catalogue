# Dongzheng (Elizabeth) Xu
#Uses two files to build the data structures to hold the information about countries and continents.
import re
from dxu254_Assign4 import country

class CountryCatalogue:
    def __init__(self,data_file,continent_file):

        data = open(data_file, "r") #file with info of each country (data.txt)
        continent = open(continent_file, "r") #file with country and continent info (continent.txt)

        self._countryCat = [] #list store objects of type country
        self._cDictionary = {} #stores key as country and value is name of continent

        #fill Dictionary key=country name value=continent name
        next(continent) #skip header
        for line in continent:
            part = line.split(",") #[Country][Continent]      #[Country][Population][Area]'
            part[1] = part[1].rstrip("\n") #removes extra punctuation

            self._cDictionary [part[0]]= part [1] # key is country name,value is continent

        next(data) #skip header
        for line in data:
            part = line.split("|") #[Country][Population][Area]

            part[1]=re.sub(',','',part[1]) # deletes the commas
            part[2]=re.sub(',','',part[2]) # deletes the commas
            part[2] = part[2].rstrip("\n") #removes extra punctuation

            newCountry = country.Country(part[0],part[1],part[2],self._cDictionary[part[0]])
            self._countryCat.append(newCountry)

    #1 finds a given country in catalogue and returns country object
    def findCountry(self,givenCountryName):
        for country in self._countryCat: #for each country in list of Country objects (_countryCat)
            if country._name == givenCountryName: #if country name is the name being searched for
                return country
        return None

    #2 sets population to new population
    def setPopulationOfCountry(self,givenCountry,newPop):
        givenCountryObj = self.findCountry(givenCountry) #find given country object
        if (givenCountryObj==None):
            return False
        givenCountryObj._population = newPop
        return True
    #3 sets area to new area
    def setAreaOfCountry(self,givenCountry,newArea):
        givenCountryObj = self.findCountry(givenCountry) #find given country object
        if (givenCountryObj==None):
            return False
        givenCountryObj._area = newArea
        return True

    #5 add a new country to dictionary of countries and country catalogue
    def addCountry(self,givenCountry,givenPop,givenArea,givenConti):
       if givenCountry not in self._cDictionary: # checks if country in dictionary (means not in continents list either)
            newCountryObj = country.Country(givenCountry,givenPop,givenArea,givenConti) #creates country
            self._countryCat.append(newCountryObj) #add new country
            self._cDictionary[givenCountry]= givenConti #adds to dictionary
            return True
       return False
    #6
    def deleteCountry(self,givenCountry):
        if givenCountry in self._cDictionary:
            del self._cDictionary[givenCountry]
            countryObj = self.findCountry(givenCountry)
            self._countryCat.remove(countryObj)
    #7
    def printCountryCatalogue(self):
        print ("Dictionary:", self._cDictionary)
        print ("Catalogue:", self._countryCat)

    #8
    def getCountriesByContinent(self,givenConti):
        countryList = []

        for key in self._cDictionary: #for every pair of country and continent in dictionary
            if self._cDictionary[key] == givenConti: # if continent is given continent
                countryObj = self.findCountry(key)
                countryList.append(countryObj) # add the country to the country list

        return countryList
    #9
    def getCountriesByPopulation(self, givenConti = ""):
        countryPopList= []
        if givenConti == "":
          for country in self._countryCat: #create a tuple list of all countries (country,population)
                tuple = (country.getName(),int(country.getPopulation()))
                countryPopList.append(tuple)
        else:
            for country in self.getCountriesByContinent(givenConti):
                    tuple = (country.getName(),int(country.getPopulation()))
                    countryPopList.append(tuple)

        countryPopList.sort (key=self.takeSecond,reverse=True) #sorts from largest to smallest population
        return countryPopList

    def takeSecond(self,elem): #gets the second element of tuple, used .sort functions
        return elem[1]

    #10
    def getCountriesByArea(self,givenConti=""):
        countryAreaList= []
        if givenConti == "":
          for country in self._countryCat:
                tuple = (country.getName(),float(country.getArea()))
                countryAreaList.append(tuple)
        else:
            for country in self.getCountriesByContinent(givenConti):
                tuple = (country.getName(),float(country.getArea()))
                countryAreaList.append(tuple)

        countryAreaList.sort (key=self.takeSecond,reverse=True) #sorts from largest to smallest population
        return countryAreaList

    #11
    def findMostPopulousContinent(self):
        continentSet = set() #create a list of all continents (set() to avoid repetition)
        for country in self._countryCat:
            continentSet.add(self._cDictionary[country.getName()]) #add all continents to set (no reptition)

        continentList = list(continentSet) #make set into list for easy manipulation
        continentPopsDict ={} #dictionary with {(key=continent,value=total population)}

        for continent in continentList: #for each continent in all continents
            continentPop = 0 #variable to track current continent population
            contiCountryPopList= self.getCountriesByPopulation(continent) #get a list of tuples with country and pop in continent
            for element in contiCountryPopList: #for each country in current continent
                    continentPop = (continentPop+element[1])
            if (continentPop!=0): # gets rid of title Country,Population tuple
                continentPopsDict[continentPop]= continent#add key population value contient to dictionary ( so sort from largest to smallest population)

        sortedContiPopList=sorted(continentPopsDict,reverse=True) #list of conti pop largest to smallest
        largestPop=sortedContiPopList[0]#finds largest population and searches pop in dictionary to find conti and stores it in var
        largestPopConti=continentPopsDict[largestPop]

        return(largestPopConti,largestPop)

    def filterCountriesByPopDensity(self,lowerBound=0,upperBound=0):
        CountryDensities=[]#create list "CountryDensities" of all countries in tuples (countries,population density)
        for country in self._countryCat: # for every country in list add country to CountryDensities list if density in ranfe
                if int(country.getPopDensity())<=upperBound and int(country.getPopDensity())>=lowerBound:
                    tuple=(country.getName(),country.getPopDensity())
                    CountryDensities.append(tuple)
        CountryDensities.sort (key=self.takeSecond,reverse=True)
        return CountryDensities

    def saveCountryCatalogue (self,fileName):
        try:
            newFile = open(fileName,"w+") #create a new file with name fileNamestring
            linesWritten=0
            self._countryCat=sorted(self._countryCat,key=lambda country:country._name)
            for element in self._countryCat:
                linesWritten = linesWritten+1
                newFile.write("{}|{}|{}|{}|{}\n".format(element.getName(),element.getContinent(),element.getPopulation(),element.getArea(),element.getPopDensity()))
            return linesWritten
        except OSError:
            return -1














