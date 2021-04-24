# Arkanoid
This program uses the arcade library to provide the graphics window and the run loop for the game.
There are 3 primary objects that comprise the game: the "MyGame" object, the ball, and the paddle. 
The run loop updates the objects in the game approximately 60 times a second, and each object contains logic for updating the objects state and determining how it is represented in the graphics window. The purpose of the game is to keep a bouncing ball from falling through the bottom of a graphics window by moving a paddle around the bottom of the window  to bounce the ball back up. 
Ball and paddle both have individual update and draw handlers.
Update handlers are responsible for dealing with any logic specific to the object and its motion
Draw handlers are responsible for drawing the object at its correct location.

The ball in this game has its own x and y-velocity 
Collisions- understanding when the ball has collided with the paddle or wall, because it needs to bounce (switch direction). 
Ball bounces on paddle - changes x-velocity: the closer to the middle of the paddle the ball is, the slower (lower x-velocity) it will go.

The paddle in this game responds to user input in the form of key presses, changing its x-position depending on which key you press (right arrow or left arrow).

"MyGame" is responsible for all the event handlers and interactions of the run loop. It handles the key presses and releases, and the collisions between the ball and the paddle mentioned earlier. This game uses a lot of conditional logic to determine legitimate collisions between the ball and the top of the paddle.   



 