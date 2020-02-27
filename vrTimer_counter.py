'''
DISCLAIMER:
---------------------------------
In any case, all binaries, configuration code, templates and snippets of this solution are of "work in progress" character.
This also applies to GitHub "Release" versions.
Neither Simon Nagel, nor Autodesk represents that these samples are reliable, accurate, complete, or otherwise valid. 
Accordingly, those configuration samples are provided “as is” with no warranty of any kind and you use the applications at your own risk.
'''


#assign timer to a variable
timer = vrTimer()

#connect timer to a function
timer.connect("counterFunction()")

#starts the timer
timer.setActive(1)

#initialize counter and set to zero
counter = 0

#define the function that counts and print the result
def counterFunction():
    global counter
    counter+=1
    
    #print the integer
    print counter
    
    #print a readable sentence, int is converted to string
    print ("The result is: "+str(counter))
    
    #if the counter is 100, the timer is turned off
    if counter == 100:
        timer.setActive(0)
