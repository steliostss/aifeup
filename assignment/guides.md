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
| Argument  | Type             | Default Value |
|-----------|------------------|---------------|
| world     | <class 'World'>  | -             |
| direction | <class 'str'>    | -             |
| steps     | <class 'int'>    | 1             |

#### Return Value

| Return Value  | When                    | Example                  |
|---------------|-------------------------|--------------------------|
| True          | On succesful movement   | user + space interaction |
| False         | On failed movement      | user + wall interaction  |

##### Note:

The function also updates the world instance with the new values and positions of the object on a succesful movement.
Attributes updated:
1. map
2. userposition
3. path
4. available_movements

___

## Principles while moving in the grid

Each algorithm uses either a stack or a queue to keep track of available positions/nodes. 
In our implementation we add in this struct an instance of the world, before every movement. 
This way if we want to backtrack it is easier to find the alternative paths.
It might be memory-expensive but it is easier to implement.

Example of an implementation (pseudocode):

```python

while ( not finish_condition ):

    direction = random(world.available_movements) # choose a random direction from available movements
    world.available_movements.remove(direction) # remove that direction from available movements
    myqueue.add(world) # add the world to the queue

    result = move(world, direction) # and try to move

    if result:
        new_world = world.deepcopy() # CAREFUL ON DEEPCOPY, it should be done this way
    else:
        # if result == False then we backtrack
        new_world = myqueue.pop()
    
    temp = world
    world = new_world
    new_world = world

    # this way, everytime a new instance of the class is added to the queue.
    # and use the previous if we made a mistake
```