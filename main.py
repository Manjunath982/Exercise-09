import win32com.client
def pronounce_names(name_list):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in name_list:
        speaker.Speak(name)

names = ["manjunath", "nishant", "harry"]
pronounce_names(names)




