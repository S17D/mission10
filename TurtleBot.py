import turtle as t
from XYRobot import XYRobot 
from math import pi,sin,cos

class TurtleBot:
    def __init__(self,nom,x=0,y=0) :
        # nom du robot
        self.__nom = nom
        # position du robot
        self.__x = x               # position x du robot
        self.__y = y               # position y du robot
        # angle en degres radius représentant la direction du robot
        self.__angle = 0           
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve dans le coin supérieur gauche
        self.__win = t.Turtle()
        self.__history = []
    
    def history(self):
        return self.__history

    def __str__(self) :
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(self.nom()) + "@(" + str(round(self.x())) + "," + \
               str(round(self.y())) +") angle: "+str(self.angle())

    def nom(self) :
        return self.__nom

    def x(self) :
        return self.__x
    
    def y(self) :
        return self.__y
    
    def angle_rad(self) :
        "retourne l'angle en degres radius représentant la direction du robot"    
        return self.__angle

    def angle(self) :
        "retourne l'angle en degres représentant la direction du robot"    
        return ( self.angle_rad() * 180 / pi ) % 360
        
    def __set_x(self,x) :
        self.__x = x
        
    def __set_y(self,y) :
        self.__y = y

    def __set_angle_rad(self,angle) :
        self.__angle = angle

    def position(self) :
        return (self.x(),self.y())

    def __draw_from(self,old_x,old_y) :
        """
        méthode auxiliaire pour tracer une ligne de l'ancienne position
        (old_x,old_y) du robot à sa position (x,y) actuelle
        """        
        
        self.__win.goto(old_x,old_y)
        
    def __move(self,distance,sense) :
        """ méthode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  fait avancer le robot de distance pixels
            si sense = -1 fait reculer le robot de distance pixels
        """
        old_x = self.x()
        old_y = self.y()
        orientation_x = cos(self.angle_rad())
        orientation_y = sin(self.angle_rad())
        self.__set_x(old_x + orientation_x * distance * sense)
        self.__set_y(old_y + orientation_y * distance * sense)
        self.__draw_from(old_x,old_y)

    def move_forward(self,distance) :
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance,1)
        self.__history.append(("forward",distance))
        

    def move_backward(self,distance) :
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """
        self.__move(distance,-1)
        self.__history.append(("backward",distance))


    def __turn(self,direction) :
        """ méthode auxiliaire pour les méthodes turn_right() et turn_left()
            si direction = 1 change l'angle du robot de 90 degrés vers la droite
                             (dans le sens des aiguilles d'une montre)
            si direction = -1 change l'angle du robot de 90 degrés vers la gauche
                             (dans le sens contraire des aiguilles d'une montre)
        """
        self.__set_angle_rad(self.angle_rad() + direction * pi/2)
        
        
    def turn_right(self) :
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.__turn(-1)
        self.__win.right(90)
        self.__history.append(("right",90))


    def turn_left(self) :
        """ fait tourner le robot de 90 degrés vers la gauche
            (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(1)
        self.__win.left(90)
        self.__history.append(("left",90))

    def unplay(self):
        for move in self.__history[::-1]:
            if move[0] == "backward":
                self.move_forward(move[1])
            
            elif move[0] == "forward":
                self.move_backward(move[1])

            elif move[0] == "left":
                self.turn_right()

            else:
                self.turn_left()
        self.__history = []                

        

test = TurtleBot("hi",100,100)
test.move_forward(500)
test.turn_left()
test.move_backward(350)
print(test.history())
test.unplay()
print(test.history())

