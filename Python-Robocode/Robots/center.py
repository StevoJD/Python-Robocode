#! /usr/bin/python
#-*- coding: utf-8 -*-

from math import *
from robot import Robot #Import a base Robot


class Center(Robot): #Create a Robot
    
    def init(self):    #To initialyse your robot
        
        
        #Set the bot color in RGB
        self.setColor(250, 10, 20)
        self.setGunColor(0, 0, 0)
        self.setRadarColor(200, 100, 0)
        self.setBulletsColor(100, 150, 250)
        
        self.radarVisible(True) # if True the radar field is visible
        
        #get the map size
        size = self.getMapSize()
        
        self.lockRadar("gun")
        self.setRadarField("thin")
        self.inTheCorner = False
        

    
    def run(self): #main loop to command the bot


        self.rPrint('heading direction1:' + str(self.getHeading()))
        self.turn(180)
        self.rPrint('heading direction1:' + str(self.getHeading()))
        
        pos = self.getPosition()
        deltaX = 400 - pos.x()
        deltaY = 400 - pos.y()
        self.rPrint('pos' +str(pos))
        
        rad = atan2(deltaY, deltaX)

        deg = rad * (180 / pi)

        distance = sqrt( (400 - pos.x())**2 + (400 - pos.y())**2 )

        self.rPrint('distance: ' + str(distance) + 'delta x: ' + str(deltaX) + 'delta y: ' + str(deltaY) + 'rad: ' + str(rad) + 'deg: ' + str(deg) + 'heading: ' + str(self.getHeading()))

        if (deg < 0):
            deg = deg + deg
            self.turn(deg)
            self.move(int(distance))
            
        else:
            self.rPrint('deg was above 0')
            self.turn(deg)
            self.move(int(distance))
        
        

        #self.move(int(distance))
        self.pause(10000)

       


        
        


    def onHitWall(self):
        pass

    def sensors(self): 
        pass
        
    def onRobotHit(self, robotId, robotName): # when My bot hit another
        pass
        
    def onHitByRobot(self, robotId, robotName):
        pass

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        pass
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        pass
        
    def onBulletMiss(self, bulletId):
        pass
        
    def onRobotDeath(self):
        pass
        
    def onTargetSpotted(self, botId, botName, botPos):#NECESARY FOR THE GAME
        if self.inTheCorner:
            self.fire(2)
            self.gunTurn(2)
            self.stop()
            self.fire(2)
            self.gunTurn(-4)
            self.stop()
            self.fire(2)
            self.gunTurn(2)
           
