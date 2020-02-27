'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided ?as is? with no warranty of any kind and you use the applications at your own risk.
'''

import math

timer = vrTimer()
timer.connect("actionBasedOnDistance()")
timer.setActive(1)

sphere = findNode("Sphere")
goal = findNode("Goal")

def actionBasedOnDistance():
    spherePos = sphere.getTranslation()
    goalPos = goal.getTranslation()
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(spherePos, goalPos)]))
    #print distance
    if distance >500:
        selectVariantSet("Green")
    elif distance <500 and distance>250:
        selectVariantSet("Yellow")
    else:
        selectVariantSet("Red")
 
