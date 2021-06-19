# xbox gamepad notes:
# Xbox A = PS X
# Xbox B = PS Circle
# Xbox X = PS Square
# Xbox Y = PS Triangle
# Xbox RB = PS R1
# Xbox RT = PS R2
# Xbox RS = PS R3
# Xbox LB = PS L1
# Xbox LT = PS L2
# Xbox LS = PS L3

# unsure if these are correct
# Xbox Select = PS Share
# Xbox Start = PS Options

import speech_recognition as sr # NOTE: this requires PyAudio because it uses the Microphone class
import vgamepad as vg
import time as zawurdo

def executeCommand(voiceClip):
    print('I heard you say {}'.format(voiceClip))
    if(voiceClip == "hello"):
        print("senpai notice me")      
        gamepad.press_button(button=vg.XUSB_BUTTON. XUSB_GAMEPAD_DPAD_DOWN)  # press the dpad down button
        gamepad.update()  # send the updated state to the computer
        zawurdo.sleep(0.017)
        
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        zawurdo.sleep(0.017)

        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)  # press the dpad left button
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)  # press the X button
        gamepad.update()  # send the updated state to the computer
        zawurdo.sleep(0.017)

        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()  # send the updated state to the computer

    if(voiceClip == "start"):
        gamepad.press_button(button=vg.XUSB_BUTTON. XUSB_GAMEPAD_START)
        gamepad.update()
        zawurdo.sleep(0.017)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        gamepad.update()


def voiceRecognition():
    while (True):
        print("Please say something")
        #gamepad.reset()
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
            try:
                print('You said: {}'.format(r.recognize_google(audio)))    # recognize speech using Google Speech Recognition
                voiceClip = r.recognize_google(audio)
                if (voiceClip == "exit"):
                    break
                executeCommand(voiceClip)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

gamepad = vg.VX360Gamepad()
voiceRecognition()

        
