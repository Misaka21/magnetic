# projectile.py

"""
Provides a simple class for modeling the flight of projectiles.
"""
   
from math import sin, cos, radians

class ProjectileNew:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        
        #20210219追加 进入磁场半径覆盖范围
        if abs(self.xpos - 100) <= 30 and abs(self.ypos - 100) <= 30:      
            self.xpos = self.xpos + time * self.xvel
            yvel1 = self.yvel - 19.8 * time
            self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
            self.yvel = yvel1
        #20210219追加 不在磁场覆盖范围
        else:
            self.xpos = self.xpos + time * self.xvel
            self.ypos = self.ypos + time * self.yvel
          




    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos
