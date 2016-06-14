import socket

#My laptop is name 'Guinsly-thinkpad-lenovo'
if 'guinsly' in socket.gethostname():
    from .development import *
    print('--dev--settings--')
else:
    try:
        from .production import *
    except:
        print("-"*18)
        print("\tPlease rename the file check this file")
        print("\tsettings/dispatch")
        print("\tfor guidance")
    #print('prod--settings')
#this file won't be load in git and in the
