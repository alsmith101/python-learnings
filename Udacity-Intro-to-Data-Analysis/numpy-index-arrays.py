'''Write a function that takes in time_spent and days_to_cancel and returns the mean of time_spent
only for students that didn't cancel in the first 6 days'''

import numpy as np

time_spent = np.array([
       12.89697233,    0.        ,   64.55043217,    0.        ,
       24.2315615 ,   39.991625  ,    0.        ,    0.        ,
      147.20683783,    0.        ,    0.        ,    0.        ,
       45.18261617,  157.60454283,  133.2434615 ,   52.85000767,
        0.        ,   54.9204785 ,   26.78142417,    0.
])

days_to_cancel = np.array([
      4,   5,  37,   3,  12,   4,  35,  38,   5,  37,   3,   3,  68,
     38,  98,   2, 249,   2, 127,  35
])

def function mean_time_for_paying_students(time_spent, days_to_cancel)

  days_to_cancel_bool = days_to_cancel >= 7

  mean_time_spent = time_spent[days_to_cancel_bool].mean()

  return mean_time_spent
