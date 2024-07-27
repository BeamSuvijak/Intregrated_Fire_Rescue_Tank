
class PID:
    def __init__(self,KP,KI,KD):
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.error = 0
        self.laster = 0
        self.sum = 0

    def calc(self):
        return self.error*self.KP + self.sum*self.KI + self.laster*self.KD


class OBJ:
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.speed = 0
        self.pid = PID(0.5,0.2,0.1)

    # Function to move the ball right
    def move(self):
        control = {
            "L" : -self.speed ,
            "R" : self.speed
        }
        return control

    def updateerrorx(self,x_pid):
        error = self.x - x_pid
        self.pid.laster = self.pid.error
        self.pid.error = error
        self.pid.sum+=error
        self.speed = self.pid.calc()
        return self.move()
