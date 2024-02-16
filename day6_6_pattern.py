#pattern for mh12aa1111
#ejepm8291n
# using reguler expresion
# chck reguler expresion table screenshot
# a-h for range , and ae it for just ae only
# ^ for start $ for ens pattern

import re # for reguler expresion

p_code = input("enter product code : ")
patternn = "[A-Z]{2}[0-9]{3}"
if re.match(patternn,p_code):
    print("valid code")

else:
    print("not valid code")

