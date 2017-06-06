countries = ['england', 'ireland', 'scotland', 'wales', 'france', 'spain', 'andorra', 'gibralta']
employmentRate = [92, 10, 63, 87, 94, 10, 28, 98]

'''get the country with the maximum employment rate!'''

'''First using regular Python'''

max_country = None
max_employment_rate = 0

for i in range(len(countries)):
    country = countries[i]
    employment = employmentRate[i]
    
    if employmentRate[i] > max_employment_rate:
        max_employment_rate = employment
        max_country = country

print(max_employment_rate, max_country)

--output: 98, 'gibralta'

'''now using numpy'''

import numpy as py

countries = py.array(['england', 'ireland', 'scotland', 'wales', 'france', 'spain', 'andorra', 'gibralta'])
employment = py.array([92, 10, 63, 87, 94, 10, 28, 98])

def maxEmployment(countries, employmentRate):
    position = employment.argmax()
    return countries[position]

maxEmployment(countries, employment)

--output: 'gibralta'


'''get the mean employment rate across the countries using numPy'''

employment.mean()

--output: 60.25

'''standardize each country's employment rate (calculate the number of standard deviations away from the mean for each)'''

def standardizingAll(employment):
    standardized_value = (employment - employment.mean())/employment.std()
    return standardized_value
    
standardizingAll(employment)

--output: array([ 0.88120107, -1.39465682,  0.0763245 ,  0.74242925,  0.9367098 ,
       -1.39465682, -0.89507826,  1.04772726])

