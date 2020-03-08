from microbit import *
import time

vw_sens = sensorteller()
ls_sens = display.read_light_level()
ut_sens = display.read_light_level()
vs_sens = display.read_light_level()
aw_sens = display.read_light_level()
rb_sens = display.read_light_level()
rk_sens = display.read_light_level()
A28z_sens = display.read_light_level()
A28n_sens = display.read_light_level()
A1w_sens = display.read_light_level()
A1O_sens = display.read_light_level()

def sens(sensorlocal):
    while True:   
        t_end = time.time()
        seconds = 10
        afslag = 0 
        while time.time() < t_end + seconds:
            time.sleep(.1)
            if sensorlocal < 120:
                afslag += 1
            if time.time == t_end: 
                return afslag

van_wijkstraat = sens(vw_sens)
leusderweg = sens(ls_sens)
utrechtse_weg = sens(ut_sens)
vermeerstraat = sens(vs_sens)
arhnemseweg = sens(aw_sens)
ringwegranderbroek = sens(rb_sens)
ringwegkruiskamp = sens(rk_sens)
A28z = sens(A28z_sens)
A28n = sens(A28n_sens)
A1w = sens(A1w_sens)
A1O = sens(A1w_sens)


if van_wijkstraat > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()


if leusderweg > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()


if utrechtse_weg > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()


if vermeerstraat > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()


if arhnemseweg > 20:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)
else:
    display.scroll()


if ringwegkruiskamp > 20:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()


if ringwegranderbroek > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()

if A1O > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()

if A1w > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()

if A28n > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()

if A28z > 20:
    display.scroll()
else:
    bord = Image("05050:05050:05050:99999:09990")
    display.show(bord)()



