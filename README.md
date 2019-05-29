# country-catalogue
## Description
A catalog that allows users to search up demographics about countries such as population,density etc.. using classes, data structures and text files
## Country.py
This class holds the information about a single country; name the file
country.py.
Instance Variables
1) name: The name of the country (string)
2) population: The population in the country (integer)
3) area: The area of the country (float)
4) continent: The name of the continent to which the country belongs (string)
### Methods
1) Constructor, __init__(self, name, pop, area, continent)  
2) Getter Methods: getName, getPopulation, getArea, getContinent,  
3) Setter Methods: setPopulation, setArea, setContinent
4) getPopDensity: This calculates and returns the population density for the country. Population
density is the population divided by the area rounded to 2 decimal places.
5) def __repr__(self): generates a string representation for class objects.  
Example of output from __repr__
Name (pop: population value, size: area value) in Continent
e.g Nigeria (pop: 11723456, size: 324935) in Africa
Test all your classes and methods before moving to the next section. Feel free to
create other helper methods if necessary.  

## Catalogue.py 
Implements a class called CountryCatalogue.This class will use two files to build the data structures to hold the information about countries and continents. The file data.txt contains information about a number of countries and the file
continent.txt contains information about countries and
This class has the following two instance variables:
*countryCat:* This is a collection of countries, i.e., each member is an object of the class Country.  
The collection could be a set, dictionary or list. It is important that the collection store objects of
type Country.
*cDictionary:* This is a dictionary where the key is the country name and the value is the name of
the continent.

### Methods
*1. Constructor: The constructor method will take as parameters two files:  
- the first file parameter is the name of the file that contains the information about each country.
- the second file parameter is the name of the file that contains the country and continent
information.
The constructor will use the data in the files to construct the two data structures countryCat  and
cDictionary.  It does this as follows:
- Fill the Dictionary:  Using the second file, fill cDictionary; the key is the country name, while the
name of the continent is the value.
- Fill the Catalogue: Using the first file, read each line of the file and from that create a country
and add it to countryCat. (Note: you will also need to use the data in cDictionary to determine
the continent for each country)  

## Sample data files
continent.txt and data.txt
Notes: a) Both files have headers and b) these files are meant for you to test your program; they
may NOT be the same used to evaluate your solution.

*2. findCountry: This method allows a user to look up information on countries.  

*3. setPopulationOfCountry: This method will take as parameters a country name and new population
and then set the population of the country (if it is in the catalogue) to the value. 

*4. setAreaOfCountry: This method will take as parameters a country name and a new area and then
set the area of the country (if it is in the catalogue) to the value.  
*5. addCountry: This method provides a way to add a new country to the dictionary of countries and
country catalogue. 
  
*6. deleteCountry: This method will take as parameter a country name and then if this country exists
then it should be deleted from the catalogue and from cDictionary.  
*7. printCountryCatalogue: This method displays the whole catalogue to the screen, using the default
string representation for the Country objects.
*8. getCountriesByContinent: This method will return a list of countries on a specific continent.  
*9. getCountriesByPopulation: This method will return a list of pairs (tuples) where a pair is a country
name and its population.  
*10. getCountriesByArea: This method will return a list of pairs (tuples) where each pair is a
country name and their area (just the value, no units).  The list is in descending order by
area from the largest to the smallest.
*12. filterCountriesByPopDensity: This method will take as parameters as a lower bound and
upper bound for a population density range and then return a list of countries that have a
population density that falls within the range (inclusive of the endpoints). 

*13. saveCountryCatalogue:  This method will enable all the country information in the catalogue
to be saved to a file. The method takes as a parameter the name of the file.  All the countries
should be sorted alphabetically by name (A – Z) prior to saving.  The file should appear in the
following format:
Format:  
Name|Continent|Population|AreaSize|PopulationDensity
For example: Canada|North America|34207999|9976200.00|3.43
Note: no spaces between attributes, 2 decimal places for the area and the population density. If
the operation is successful, the method should return the number of items written, otherwise it
should return a value of ‐1.  
