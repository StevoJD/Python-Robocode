#! /usr/bin/python
#-*- coding: utf-8 -*-



from math import *
from robot import Robot #Import a base Robot


class Stevo(Robot): #Create a Robot
    
    def init(self):# NECESARY FOR THE GAME   To initialyse your robot
        
        
        #Set the bot color in RGB
        self.setColor(0, 000, 225)
        self.setGunColor(200, 000, 225)
        self.setRadarColor(000, 225, 000)
        self.setBulletsColor(0, 200, 225)
        
        #get the map size
        size = self.getMapSize() #get the map size
        self.radarVisible(True) # show the radarField

        
        self.lockRadar("gun") #remove this for independent scanner
        #self.setRadarField("thin")
    
    def run(self): #NECESARY FOR THE GAME  main loop to command the bot

       self.setRadarField("thin")
       #self.gunTurn(360)
       #movement sequence one is a circle

        #circle
       count=0;
       counts=0;
       while (counts < 4):
           self.gunTurn(90)
           counts = counts + 1
            
           
       while (count < 4):
           self.gunTurn(90)
           self.turn(90)
           self.move(100)
           count = count + 1


    
        

        
    def sensors(self):  #NECESARY FOR THE GAME
        """Tick each frame to have datas about the game"""
        
        pos = self.getPosition() #return the center of the bot
        x = pos.x() #get the x coordinate
        y = pos.y() #get the y coordinate
        
        angle = self.getGunHeading() #Returns the direction that the robot's gun is facing
        angle = self.getHeading() #Returns the direction that the robot is facing
        angle = self.getRadarHeading() #Returns the direction that the robot's radar is facing
        list = self.getEnemiesLeft() #return a list of the enemies alive in the battle
        for robot in list:
            id = robot["id"]
            name = robot["name"]
            # each element of the list is a dictionnary with the bot's id and the bot's name
        
    def onHitByRobot(self, robotId, robotName):
        self.rPrint("damn a bot collided me!")
    
        

        

    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event) 
        self.pause(100)
        self.move(-100)
        self.rPrint('ouch! a wall !')
        

        
    
    def onRobotHit(self, robotId, robotName): # when My bot hit another
        self.rPrint('collision with:' + str(robotName)) #Print information in the robotMenu (click on the righ panel to see it)

        self.move(100)
        
        


       
    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        """ When i'm hit by a bullet"""
        # self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event) 
        self.rPrint ("hit by " + str(bulletBotName) + "with power:" +str( bulletPower))

        
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a bot"""
        self.rPrint ("fire done on " +str( botId))
        

        
    def onBulletMiss(self, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        self.rPrint ("the bullet "+ str(bulletId) + " fail")
        self.rPrint(" rotating my gun")

        #If multiply bullets miss this could mean that the radar/gun is not aimed correctly
        #This allows the bot to retarget his opponent 
        self.gunTurn(90)

        #Used for other targetting system
        #self.radarTurn(360)
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")


    
    def onTargetSpotted(self, botId, botName, botPos):#NECESARY FOR THE GAME
        "when the bot see another one"

    #https://stackoverflow.com/questions/5228383/how-do-i-find-the-distance-between-two-points
        distance = sqrt( (botPos.x() - self.x())**2 + (botPos.y() - self.y())**2 ) #cals the distance between the robots
        self.rPrint("My postion is:"  + " on position: x:" + str(self.x()) + " , y:" + str(self.y()))    
        self.rPrint("I see the bot:" + str(botId) + "on position: x:" + str(botPos.x()) + " , y:" + str(botPos.y()))
        self.rPrint(" the distance is:" + str(distance)) 
        self.rPrint(" the gun angle:" + str(self.getGunHeading()))
        self.rPrint(" the radar angle:" + str(self.getRadarHeading()))

        #Targeting system. Scans target then moves gun to tank
        # compares the angle of the radar to the gun so can aim at the target
        #angle = self.getRadarHeading() - self.getGunHeading() 
        #self.gunTurn(angle) # moves the gun to the angle of the tank 
        
        
        
        
        # How powerful each shot will be. The closer the target the more powerful the shot

        if  distance < 100:   
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(10)
            self.pause(0)
            self.rPrint("Power of my shot is: 10") 
        
        elif 100 < distance <= 200:
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(8)
            self.pause(2)
            self.rPrint("Power of my shot is: 8")
            
        elif 200 < distance <= 300:   
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(6)
            self.pause(4)
            self.rPrint("Power of my shot is: 6")

        elif 300 < distance <= 400:
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(4)
            self.pause(6)
            self.rPrint("Power of my shot is: 4")           

        elif 400 < distance <= 500:
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(2)
            self.pause(8)
            self.rPrint("Power of my shot is: 2")             
            
        elif 500 < distance <= 700:
            self.gunTurn(0)
            self.radarTurn(0)
            self.fire(1)
            self.pause(10)
            self.rPrint("Power of my shot is: 1")             

        else:
            self.rPrint(" target too far away") 
            #Will not fire as target is too far away and will waste energy
    



