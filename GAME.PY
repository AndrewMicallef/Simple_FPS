from bge import logic
from bge import events
import numpy as np
import math


def length(vector):
    return np.linalg.norm(vector)

def normalise(vector):
    if length(vector) != 0:
        return np.array(vector) / length(vector)
    else:
        return np.array((0,0,0))

scene = logic.getCurrentScene()
text = scene.objects['Text']

def Camera():
    obj = scene.objects['Camera']

    
    def Init():
        logic.mouse.position = 0.5, 0.5
        if not 'init' in obj:
            obj['init'] = 1

    def mouselook():
        ###############
        # Looking
        ###############

        #The mouse input:
        # centre of screen = 0,0?
        #X = (logic.mouse.position[0] - 0.5)
        X, Y = logic.mouse.position
        Y = Y - 0.5
        
        x,y,z = obj.localOrientation.to_euler()
        #the X movement is applied to the rotation of the character itself
        obj.localOrientation= (x-Y, y, z)

        #and then the cursor is set back to the center of the screen.
        logic.mouse.position = 0.5, 0.5

    
    Init()
    mouselook()



def Player():
    obj = scene.objects['Player']
    player = obj

    key = logic.keyboard.events
    kbleft = key[events.AKEY] > 0
    kbright = key[events.DKEY] > 0
    kbup = key[events.WKEY] > 0
    kbdown = key[events.SKEY] > 0
   
    def Init():
        logic.mouse.position = 0.5, 0.5
        if not 'init' in obj:
            obj['init'] = 1
   
   
    def mouselook():
        ###############
        # Looking
        ###############

        #The mouse input:
        # centre of screen = 0.5,0.5?
        X, Y = logic.mouse.position
    
        X = X - 0.5
        #the X movement is applied to the rotation of the character itself
        obj.applyRotation([0, 0, -X])

        #and then the cursor is set back to the center of the screen.
        logic.mouse.position = 0.5, 0.5
    
   
    def Update():
   
        x,y,z = player.position
        ax, ay, az = player.localOrientation.to_euler()
        
        spd = 0.1
        
        direction = normalise((kbright - kbleft, kbup - kbdown, 0))
        
        if length(direction) > 0:
            dx, dy, dz = direction
            
            print(az)
            print (dx, dy, dz)
            if dx == 0:
                if dy > 0:
                    theta = np.pi/2 
                else:
                    theta = -np.pi/2 
            elif dy == 0:
                if dx > 0:
                    theta = 0
                else:
                    theta = np.pi
            else:
                theta = np.arctan(dy/dx) 
                
            theta += az
            
            player.position =  (x + (spd*np.cos(theta)), y + (spd*np.sin(theta)), z)
            print(np.cos(theta))
        
        
        
    Init()
    mouselook()
    Update()

if __name__ == '__main__':
    
    bullets = 5
    logic.mouse.position = 0.5, 0.5
    Player()
    
    if logic.mouse.events[events.LEFTMOUSE] > 0:
        text['Text'] = 'Bang!'
    else:
        text['Text'] = '%d bullets' %bullets
    Camera()