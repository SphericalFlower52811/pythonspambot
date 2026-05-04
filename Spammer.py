import pyautogui as pg
import time
def spammer(sec):
    repeats = int(input("How many times do you wanna spam? >>> "))
    spamchar = input("Choice of spam? >>> ")
    times = sec #change this for seconds.
    print("Waiting...\ngo into whatsapp now")
    print(f"You have {times} seconds.")
    for i in range(0, times):
        time.sleep(1)
        print(times - i)
    for i in range(0, repeats):
        pg.write(spamchar)
        pg.press('enter')
        print(i + 1)

if __name__ == '__main__':
    spammer(6)
