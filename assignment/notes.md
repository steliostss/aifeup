# Notes for Box World2

This files holds notes for implementation of the game [BoxWorld2](http://hirudov.com/others/BoxWorld2.php)

## Objects

The objects available in the game are stated below:

| *Ascii character used* | *Representing character in game* |
|------------------------|----------------------------------|
| -                      | Empty space                      |
| B                      | Normal Box                       |
| F                      | Finish point                     |
| H                      | Hole                             |
| I                      | Ice Box                          |
| U                      | User position                    |
| W                      | Wall                             |

## User actions

The user can move:

| *Direction* | *Key pressed* |
|-------------|---------------|
| Up          | W             |
| Down        | S             |
| Left        | A             |
| Right       | D             |

The user can push boxes and move in their positions.
The user *cannot* go over holes or walls.

## Capabilities & Conditions

Below are be the capabilities of the game and the conditions that we should meet in order to perform the corresponding action.

### Moving User

To be able to move the user in a specific direction then you should check if the target position is wall or hole. If so the user cannot move there. 

If the target position is empty space then user moves there and the previous position becomes empty space.

If nothing else succeeds then the empty space is a box. Then check [Moving boxes](#moving-boxes).

### Moving boxes
#### Ice boxes
#### Normal boxes
### Finishing the game


## Input
