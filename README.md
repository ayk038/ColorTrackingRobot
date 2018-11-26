# spis16-project-planning-robotics-Andrew-Anthony

For our final project, we had two ideas: one involved two robots playing pong with a ping pong ball, and the other project idea consisted of a robot that produced music using a keyboard. 

To elaborate on the first idea, we would take two robots that have only two primary directions: right or left. By restricting the overall motion to these two directions, we simulate an experience similar to that of the retro game. The simulation must occur on a frictionless surface as to promote fluidity of motion for the ping pong ball. Each robot would be controlled by a player for a 2 - player experience. 

To elaborate on the second idea, we would take a robot and a multi color sensor to sense different color strips and play certain musical notes when it senses the corresponding color. A speaker will be hooked up to the robot to play the music. We can hard program certain patterns to play specific songs.

#Stages (Idea 1)

Stage 1: Get the motor for each individual robot to move forward.

Stage 2: Get the motor for each individual robot to move forward and backward.

#Stages (Idea 2)

Stage 1: Get the sensor to indicate the difference between the colors

Stage 2: Get the robotic arm to point to each individual color

Stage 3: Get the sensor to indicate a relationship between the color and the note.

Stage 4: Get the robot to produce different sound notes.

Stage 5: Hard code individual patterns to produce simple songs.

#Actual Progress
For our final project, our goal is to program our raspberry pi to detect the sphereo and follow it by using sonar and camera video.
when the ball moves the sonar and the video camera should track the ball and follow it by turning and moving forward.

Completed so far: sonar is working as intended, motor is working as intended, sonar and motor work simultaneuously and as expected,
the camera works and is able to take pictures, the camera can also record videos, we have code that can trace circles and attempt to trrack the object.

Things to do: get the raspberry pi to recognize color, get the robot to turn when the ball gets out of the peripheral, make the circle drawing program more precise, additional actions depending on the color of the ball (such as doing tricks), make movement more precise
such as turning and stopping.
