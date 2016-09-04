5:12 PM 4/09/2016

The weapon will have a series of states, each being a partictular transform.
The key presses will shift between states, via bilinear spring dampened
interpolation [HARD PROBLEM].

Ultimatley each weapon will have it's own mechanics and so, require it's own
object and possibly key mapping.

The first weapon, ie the one we have now, is a bolt action rifle.

The rifle is composed of the following objects:

- Barrel
- Stock
- TriggerGuard
- Casing
- Frontgrip
- Fronsight
- Sight_rail

- sight_notch
- sight_rail
- trigger
- bolt

The trigger and the bolt are the only moveable parts. I will use a leading 
capital for parts which are stationary.

The movable parts have the following states:

- trigger
    + released
        - transform: rotation (0, 0, 0)
    + drawn
        - either: rot ( 22deg, 0, 0 )
        - or: translation(0, -0.004, 0)


- bolt
    + locked
        + unlocked:
            - rot: (0, 0, ~100 deg)
            + open
                - trans: (0, 0, 0.05)

    + bolt transitions:
        1. locked & closed -> 
            2. <- unlocked & closed ->
                3. <- unlocked & open ->
                    - ejects cartridge
                    - next bullet is pushed up slightly
                        4. <- locked & open ??
                        
            5. <- unlocked & closed ->
                - catches next bullet, feeds into chamber as bolt closes
                - firing now would release the hammer without garunteeing
                    striking the bullet. Could cause cartridge to blow out
                    the side, damaging the bolt mechanism.
        1. <- locked & closed
            - locks bullet in chamber, bringing striking hammer into range.
            

    all transitions could be boolean values.
    Or the might be floats between 0 and 1, the value of which is multiplied by 
    the transformation. Thus pressing the key would increment the value until it
    reaches 1 or 0. This would naturally encode the time course of the 
    animation.

