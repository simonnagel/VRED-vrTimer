'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided ?as is? with no warranty of any kind and you use the applications at your own risk.
'''

box = findNode("Box")
sphere = findNode("Sphere")

timer = vrTimer()
timer.connect("syncZPositionToSphere()")
timer.setActive(1)

def syncZPositionToSphere():
    global box
    global spehere
    positionBox = box.getWorldTranslation()
    
    boxX = positionBox[0]
    boxY = positionBox[1]
    boxZ = positionBox[2]
    
    positionSphere = sphere.getWorldTranslation()
    
    sphereX = positionSphere[0]
    sphereY = positionSphere[1]
    sphereZ = positionSphere[2]
    
    sphere.setWorldTranslation(positionSphere[0],positionSphere[1],positionBox[2])
