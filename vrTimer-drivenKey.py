'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
'''

import math

timer = vrTimer()
timer.connect("drivenKey()")
timer.setActive(1)

car = findNode("Car")
tireFront = findNode("Tire_Front")
tireRear = findNode("Tire_Rear")

def drivenKey():
    tireDiameter = 300
    carPos = car.getTranslation()
    tireRot = carPos[0]*(tireDiameter*math.pi)/1000

    tireFront.setRotation(0,tireRot,0)
    tireRear.setRotation(0,tireRot,0)
    
 
