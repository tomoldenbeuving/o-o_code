from microbit import *
import time

A1w_sens = display.read_light_level()
# voor het voorbeeld zijn de volgende inputs uitgeschakeld
#vw_sens = sensorteller()
#ls_sens = display.read_light_level()
#ut_sens = display.read_light_level()
#vs_sens = display.read_light_level()
#aw_sens = display.read_light_level()
#rb_sens = display.read_light_level()
#rk_sens = display.read_light_level()
#A28z_sens = display.read_light_level()
#A28n_sens = display.read_light_level()
#A1O_sens = display.read_light_level()

def sens(sensorlocal): #dit is de teller die 1 optelt bij een variable als het te donker wordt(als er dus een atuo voor langs rijdt)
    while True:   
        t_end = time.time()
        seconds = 10
        afslag = 0 
        while time.time() < t_end + seconds: #dit is de klok waardoor die maar voor 1 minuut autos telt
            time.sleep(.1)
            if sensorlocal < 120:
                afslag += 1
            if time.time == t_end: 
                return afslag #aan het eind van de loop stuurt de functie (da's altijd een 'def') de variable afslag terug naar de code

A1w = sens(A1w_sens)
#van_wijkstraat = sens(vw_sens)
#leusderweg = sens(ls_sens)
#utrechtse_weg = sens(ut_sens)
#vermeerstraat = sens(vs_sens)
#arhnemseweg = sens(aw_sens)
#ringwegranderbroek = sens(rb_sens)
#ringwegkruiskamp = sens(rk_sens)
#A28z = sens(A28z_sens)
#A28n = sens(A28n_sens)
#A1O = sens(A10_sens)


#hier wordt de 'afslag vergeleken met een getal om te bepalen waar de automobilist heen moet
if A1w > 20: 
    display.scroll("via Energieweg, Amersfoortse Straat")
elif A1w > 5 : 
   display.scroll("via Outputweg, Rondweg Ost, Bergpas") 
else:
   display.scroll("via Hogweg, A28") 

if A28n > 20:
    display.scroll("via Energieweg, Amersfoortsestraat, A1")
elif A28n > 5 : 
   display.scroll("via Hogeweg") 
else:
   display.scroll("via Hogeweg") 

if A28z > 20:
    display.scroll("via Leusderweg, Kersebaan of N227")
elif A28z > 5 : 
   display.scroll("via Leusderweg") 
else:
   display.scroll("via Hogeweg") 