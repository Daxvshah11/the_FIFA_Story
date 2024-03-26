#  /**
#      * return an objects of structure:
#      * country : {
#      *    year : {              (year when the country participated in WC)
#      *      player   : #scores  (score of player)
#      *      "_total" : #socres  (total scores of the country in this year)
#      *    }
#      *    "_img" : image source
#      * }
#      */

import pandas as pd
data = pd.read_csv('WorldCupMatches.csv')


