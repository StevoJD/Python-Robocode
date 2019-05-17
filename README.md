![alt text](https://github.com/turkishviking/Python-Robocode/blob/master/Python-Robocode/robotImages/robotTitre.png?raw=true "Python-Robocode")
===============
 


### A Fork of Robocode for python programming


### Installation
* [Python 2.7 Windows 64bit](https://www.python.org/ftp/python/2.7.16/python2716.chm)
* [Pyqt4.exe](https://netcologne.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe)
 

### Bots
 - StevoJDbot (Main)
 - Center
 - Wall
 - Aim


### StevoJDbot
 - The movement is circle motion.
 - Head on targeting system that has system that can control power of shot and firerate. (Line 146 onwards)
 
 - How to improve
 1. Implement a strafing stragety to dodge more bullets this would be espically effective in 1v1 [Strafing](http://mark.random-article.com/weber/java/robocode/lesson5.html)
 2. More complex [movements](http://www.robowiki.net/wiki/Anti-Gravity_Tutorial)
 - Could not implement as python inf is a float and the self move requires an int 
 3. Game awarness. e.g 1v1 
 
### Bugs
- When bot miss shots it should scan again and aim at target. As the radar will be on target but the bullets miss. However bulletmiss event launches too slow or not at all and the bot kills it self by wasting energy
 
 
 
 
### Center
 - This bot is designed to move to the center of the arena.
 - Calculates the distance and the angle and moves the bot.
 
Unfortunately the bot does not work as it won't turn the tank in the correct direction. So this was not implemented in my main bot.

- [Distance](https://stackoverflow.com/questions/5228383/how-do-i-find-the-distance-between-two-points)
- [Angle](https://stackoverflow.com/questions/21483999/using-atan2-to-find-angle-between-two-vectors#21484228)

 

### Wall
 - Bot that detects walls 
 There is no speed/velocity. 
 
 I did try *-1 of the direction this did work but then the main loop would start again and make the bot move forward when it should have gone backwards to avoid that wall.
 This solution was created to be alternative strategy for the Center bot.  
 
### Aim bot
 - Radar moves independently then gun moves to the target
 
 Decided to remove from StevoJD bot as the gun takes to long to move to target and always rotates clockwise when the other direction would be quicker. Had to update robot.py Line 404
- [Targetting](http://robowiki.net/wiki/Head-On_Targeting)

### Whats Next?

- [Machine Learning](http://www.dinbedstemedarbejder.dk/Dat3.pdf) in Python robocode.
