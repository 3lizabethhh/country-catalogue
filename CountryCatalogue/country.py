# Dongzheng (Elizabeth) Xu
# holds information about a single country
class Country:
    def __init__(self,name="",population=0,area=0,continent=""):
        self._name=name
        self._population = population
        self._area = area
        self._continent = continent

    def __repr__(self):
        return("{}(pop:{},area:{}) in {}".format(self.getName(),self.getPopulation(),self.getArea(),self.getContinent()))

    def getName (self):
        return self._name
    def getPopulation (self):
        return self._population
    def getArea (self):
        return self._area
    def getContinent(self):
        return self._continent

    def setPopulation(self,population):
        self._population = population
    def setArea(self,area):
        self._area = area
    def setContinent(self,continent):
        self._continent = continent

    def getPopDensity (self):
        #if self.getPopulation()!="Population":
         popDensity = round(float(self.getPopulation())/float(self.getArea()),2)
         return popDensity






