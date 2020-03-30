# Notes for Box World2

This file has notes for implementation of the game [BoxWorld2](http://hirudov.com/others/BoxWorld2.php)

## Objects

The objects available in the game are stated below:

| Ascii character used | Representing character in game |
|----------------------|--------------------------------|
| -                    | Empty space                    |
| B                    | Normal Box                     |
| F                    | Finish point                   |
| H                    | Hole                           |
| I                    | Ice Box                        |
| U                    | User position                  |
| W                    | Wall                           |

## User actions

The user can move:

| Direction | Key pressed |
|-----------|-------------|
| Up        | W           |
| Down      | S           |
| Left      | A           |
| Right     | D           |

The user can push boxes and move in their positions.
The user *cannot* go over holes or walls.

## Capabilities & Conditions

Below are be the capabilities of the game and the conditions that we should meet in order to perform the corresponding action.

### Moving User

To be able to move the user in a specific direction then we should make some checks. It's important to mention that **the user can only move one step at a time**.

If the target position is:

1. wall or hole, the user cannot move there.
2. empty space then user moves there and the previous position becomes empty space.
3. a box, then check [Moving boxes](#moving-boxes).

### Moving boxes

In order for the user to move a box we should check what is in the position next to the box, towards the direction that the user moves.

If the target position is:

1. wall or box, then we can't move the box, so the user doesn't move.
2. hole, then the box **[fills](#filling-holes)** the hole and and the user occupies the box's previous position.
3. empty space, then the user occupies the box's previous position and we should also check the box's type. It can be either:
    1. [normal box](#normal-boxes)
    2. [ice box](#ice-boxes)

#### Normal boxes

Normal boxes just move to the target position giving their spot to the user. The user gives his spot to empty space.

#### Ice boxes

If the box that the user meets is an ice box then an **extra check** should be made. Ice boxes move in the same direction until they hit a wall, another box or a hole. So we should check the row or column that the box moves and find the next item. The ice box will move next to it or in it, if it is a hole. The original position will be overtaken by the user and the user's position by empty space.

#### Filling holes

Holes can be filled by boxes of any type. They have a capacity of 1 box. If a box moves and fells into a hole, then the hole is transformed into empty space. 

### Finishing the level

If the user reached the end ( 'F' ) then the next level is presented to him to continue playing, until the last level.

### Restarting Level

The user can restart the game if he gets stuck by pressing 'R'.