Kp,Ki,Kd = 1, 1, 0
time = 0
integral = 0
time_prev = -1e-6
e_prev = 0
def change_settings(p,i,d):
    global Kp,Ki,Kd
    Kp,Ki,Kd = p,i,d


def PID(setpoint, measurement):
    global time, integral, time_prev, e_prev

    # Value of offset - when the error is equal zero
    offset = 320

    # PID calculations
    e = setpoint - measurement

    P = Kp * e
    integral = integral + Ki * e * (time - time_prev)
    D = Kd * (e - e_prev) / (time - time_prev)

    # calculate manipulated variable - MV
    MV = offset + P + integral + D

    # update stored data for next iteration
    e_prev = e
    time_prev = time
    return MV

def start_PID(object_x,object_y,SCREEN_WIDTH,SCREEN_HEIGHT):
    while object_x - (SCREEN_WIDTH / 2) <= 1e-2 and object_y - (SCREEN_HEIGHT / 2) <= 1e-2:
        print("KUY")
