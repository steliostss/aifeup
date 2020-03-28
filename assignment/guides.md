# Ηow to properly use existing code for Algorithms.py

Practically here will be given an API of World.py and Functions.py.


## Available Functions

### move

    ```python
    move(world, direction, steps=1)
    ```

    #### Purpose

    This function calculates if the user can move using the map and user_position attributes of the object world and the direction.

    #### Arguments

    This function has 3 arguments: 
    1. world : instance of class World
    2. direction : one of ( 'a' , 's' , 'd' , 'w')
    3. steps : by default 1 

    #### Return Value

    This function returns either: 
    - True : on succesful movement (e.g. user + space interaction)
    - False : on failed movement (e.g. user + wall interaction)

    ##### Note:

    The function also updates the world instance with the new values and positions of the object on a succesful movement.



