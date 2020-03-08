import time


while True:
    van_wijkstraat = 0
    t_end = time.time()
    seconds = 5
    while time.time() < t_end + seconds:
        van_wijkstraat += 1
        time.sleep(.5)
        print(van_wijkstraat)
        if time.time() == t_end + seconds:
            break
