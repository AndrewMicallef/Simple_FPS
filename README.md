#Simple_FPS 

This started off just as an exercise in the blender game engine.
There is no clear outcome, however there are a few things I would like to implement.

[ ] Mechanically realistic weapon, in the style of [Receiver](http://www.wolfire.com/receiver)

[ ] Artificial life simulation:
	Either,
	- Artificial Neural network controlled NPC
	- Genetically evolving NPCs
	- or both

[Blender Game Engine Documentation](https://www.blender.org/api/blender_python_api_current/)


Spawning objects
-----------------
Use the `addObject` method on the blender game engine scene to add objects
to the world. Each new object needs a reference object in the world to inherit
world propertiies from. 


`scene.addObject(object, reference, time=0)`
:    Adds an object to the scene like the Add Object Actuator would.
:    Parameters	
     : object (KX_GameObject or string)
		: The (name of the) object to add.
     : reference (KX_GameObject or string)
		: The (name of the) object 
 	 	which position, orientation, and scale to copy (optional), if 
 	 	the object to add is a light and there is not reference the 
 	 	light’s layer will be the same that the active layer in the 
 	 	blender scene.
     : time (integer)
		: The lifetime of the added object, in frames. 
 	 	A time of 0 means the object will last forever (optional).
 
     Returns
     :	The newly added object.
     :	Return type
      	:	KX_GameObject
