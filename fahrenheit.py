# Question: 
# The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.
# You are given a variable Celsius representing a temperature in Celsius. Use the variable Fahrenheit
# already defined and assign it the Fahrenheit temperature equivalent to the given Celsius
# temperature. Use the algorithm mentioned above to help convert the Celsius temperature to
# Fahrenheit. 

temp_in_Celcius = float(input("Enter temperature to convert: "))

def convertToFahrenheit(temp_in_Celcius):

    Fahrenheit = (9 / 5 * temp_in_Celcius) + 32   #computation of the conversion
    
    print(Fahrenheit)

convertToFahrenheit(temp_in_Celcius)