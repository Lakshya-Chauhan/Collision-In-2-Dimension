# Collision in 2-dimension

## Basic Working

When the program is run, it asks the user for entering two values,
- First being the value of the `mass` of the Blue Ball.
- Second being the value of the `mass` of the Green Ball.

After further execution, the **GUI** window opens and the main functionality begins to work.

<hr>

#### When is a collision detected?

Everytime, when the distance between the two balls becomes less than or equal to the sum of their radius the program declares it as a `collision`.

It then performs basic calculation by finding the vector component along x-axis and vector component along y-axis of the balls and change them.

> Footnote:
This program idea clicked in my mind, while thinking about how a **Carrom** game could be coded in **Python**. So, this one holds as a sub-part for the game.
