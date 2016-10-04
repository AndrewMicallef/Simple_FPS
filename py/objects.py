'''
#(https://www.blender.org/api/blender_python_api_current/bge.types.KX_GameObject.html)
import bge

class CustomGameObject(bge.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" can just be ignored. At this point, "self" is
        # already the object in the scene, and "old_owner" has been
        # destroyed.

        # New attributes can be defined - but we could also use a game
        # property, like "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # switch direction
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Called first
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # After calling the constructor above, references to the old object
    # should not be used.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Called later - note we are now working with the mutated object.
def update(cont):
    cont.owner.update()
    
scene = bge.logic.getCurrentScene()
Cube = scene.objects['Cube']

Cube = CustomGameObject(Cube)
Cube.update()
'''

class brain ():

    '''The simplest possible neural network of this form is composed of a
    connection matrix and the operation:
    
    $output = w \times input$
    
    where w is the connection matrix and input the vector of nueral activity
    
    Example trivial network
    -----------------------
    
    digraph network {
        A -> C;
        A -> B;
        B -> C;
        C -> C;
        D -> C;
    }
    
    for the network above a connection matrix of inputs and outputs can be
    constructed as follows:
    ```
        INPUTS
      +---------------+  O
    A | 0   0   0   0 |  U
      |               |  T
    B | 1   0   0   0 |  P
      |               |  U
    C | 1   1   1   1 |  T
      |               |  S
    D | 0   0   0   0 |
      +---------------+
       A    B   C   D
    ```
    
    In this situation each row is the input vector of the coresponding neuron
    while each colum represents the output of it's neuron.
    
    TODO: How to make this controlled by genes?
            - gene for input out put of each nuron
            - gene for connection matrix?
    
    '''
    
    def __init__(self, sensors, actuators):
        pass
    
    def generateLayer(self, _input):
        '''create a connection matrix of all neurons'''
        
        synapse_weights = np.zeros((_input.size, _input.size))



class creature(bge.types.KX_GameObject):
    ''' Instantiates a creature in the game world as a subclass of a blender
    game object.
    
    The creature has a simple neural network. In the first instance I will
    implement a three layered structure. The first layer will be composed of
    sensory neurons which will feed forward to a processing layer which in turn
    is connected to output actuators.
    
    ----------------------------------------------------------------------
    Sensor              genes
    ------------------  --------------------------------------------------
    *EXTERNAL*
    
    collision detector  - physical location
                        - sensitivity
                        - number of sensors
                        
    eye (rayCast)       - physical location
                        - orientation
                        - sensitivity
                            - max distance
                            - property reported
                              :     can be one of, distance, material, object
                              
    *INTERNAL*
    
    pace maker         - frequency
    
    hunger             - range
                         :  that is sets the offset between max firing and
                            maximum hunger. 
    
    fatigue            - range
                         :   offset between percieved and actual fatigue
                             levels. When actual fatigue reaches maximum
                             the creature is unable to move. Fatigue 
                             replenishes if the hunger is non-zero. 
                             Otherwise the creature will die.
    
    ----------------------------------------------------------------------
    
    Table: Sensory layers
    
    '''
    def __init__(self, old_object, genome = None):
        pass

    def update(self):
        pass

    def eye(self, 
                target_of_eye, #[x, y, z] 
                position_of_eye, #[x, y, z]
                max_look_distance, #float
                **kwargs):
                
        '''wraps rayCast with semantics of an eye'''
        
        # grab ray and then unpack
        ray = self.rayCast(
                        objto = target_of_eye,
                        objfrom = position_of_eye,
                        dist = max_look_distance,
                        poly = 2, #forces expected 5 tuple output 
                        **kwargs,
                        )
                     
        _object, hitpoint, hitnormal, polygon, hituv = ray  
        
        '''returning the color of the object will give error if polygon 
        returns `None`'''
        #rgb = polygon.material.diffuseColor
        pass

    def hunger (self):
        pass
    
    def fatigue (self):
        pass
            
    def heartbeat (self):
        '''the pace maker'''
        pass

