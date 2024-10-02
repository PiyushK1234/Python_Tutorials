import pyautogui
import time

# Give the python file some time before continue
time.sleep(2)


#Mouse Functions
'''
print(pyautogui.size()) # Print the resolution of the screen

print(pyautogui.position()) #Print the current position of mouse

pyautogui.moveTo(100,100,3) #Move the mouse over time

pyautogui.moveRel(100,100,3)  #Move the mouse relative to its current postion

'''
#click
'''pyautogui.click();
pyautogui.doubleClick();
pyautogui.tripleClick();
pyautogui.leftClick();
pyautogui.rightClick();
'''
#scroll

'''
pyautogui.scroll(-500) #scroll down

pyautogui.scroll(500) #scroll up

'''

'''
time.sleep(2)
pyautogui.mouseDown(300,400, button="left")
pyautogui.moveTo(800,400,3)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400,3)

'''
'''
#Sprial drawing 
time.sleep(1)
distance = 300
while distance>5:
    pyautogui.dragRel(distance,0,1,button="left")
    distance= distance-20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance , 0,1, button="left")
    distance= distance-20
    pyautogui.dragRel(0,-distance,1,button="left")

'''


'''
#Keyboard Functions
pyautogui.write("Hello")
pyautogui.press("enter")
pyautogui.press("space")


'''
#Screenshot
pyautogui.screenshot("first.png")