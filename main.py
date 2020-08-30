import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(400,400)
root.configure(bg='grey')


listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname

def rewindsong(event):
    pygame.mixer.music.rewind()
   
def vol_increase(event):
    if(pygame.mixer.music.get_volume()<1.0):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)

def vol_decrease(event):
    if(pygame.mixer.music.get_volume()>0.0):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)


label = Label(root,text='MY Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

Rewindbutton = Button(root,text = 'Rewind Song')
Rewindbutton.pack()

Volumeplus = Button(root,text = 'Volume +')
Volumeplus.pack()

Volumeminus = Button(root,text='Volume -')
Volumeminus.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
Rewindbutton.bind("<Button-1>",rewindsong)
Volumeplus.bind("<Button-1>",vol_increase)
Volumeminus.bind("<Button-1>",vol_decrease)

songlabel.pack()

root.mainloop()