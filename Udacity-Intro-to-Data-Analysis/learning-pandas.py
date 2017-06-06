
'''
Write a function that takes in two series, life expectancy and GDP in 2007

Do life expectancy and GDP correlate.
i.e.When a country has a life expectancy above the mean, is the GDP also above? and vice versa.
'''

import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]


life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)


def function(life_expectancy, gdp):
  
  both_greater = (life_expectancy > life_expectancy.mean()) & (gdp > gdp.mean())
  both_lower = (life_expectancy < life_expectancy.mean()) & (gdp < gdp.mean())
  
  both_lower_OR_Greater = both_greater | both_lower
  count_both_same_direction = both_lower_OR_Greater.sum()
  print(count_both_same_direction)
  '''GDP and life expectancy either both above or both below the mean = 17'''
  
  count_different_directions = len(countries) - count_both_same_direction
  print(count_different_directions)
  '''=3'''
  
  '''GDP and life expectancy appears to correlate as in nearly all the cases
  , the country's GDP and life expectancy values were either both above or both below the mean'''
  
  
  
  
