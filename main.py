import pyautogui, time, random
time.sleep(5)
x = 1
y = 1
mulChoi = ["A", "B", "C", "D"]
highLow = ["high", "low"]
locations = ["area51", "discord", "dresser"]
memeOptions = ["f", "r", "i", "c", "k"]
naughtyBois = ["Kelvin", "MT"]
while True:
    pyautogui.typewrite("pls trivia")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite(random.choice(mulChoi))
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls highlow")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite(random.choice(highLow))
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls search")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite(random.choice(locations))
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls postmeme")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite(random.choice(memeOptions))
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls hunt")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls fish")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls beg")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls use padlock")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls rob @" + random.choice(naughtyBois))
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.typewrite("pls dep all")
    pyautogui.press("enter")
    time.sleep(3)
#    pyautogui.typewrite('Spam Count: '+str(y))
#    pyautogui.press("enter")
    print(str(y))
    y = y+1
    time.sleep(3)