# MP3 Player

# ---------------------------------------------------
# Packages
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import pygame
import time


# ---------------------------------------------------
# Functions
# Add Many Songs
from sqlalchemy import column


def addMany():
    songs = filedialog.askopenfilenames(initialdir='songs/', title='Choose a Song',
                                      filetypes=(('mp3 Files', "*.mp3"),))
    for song in songs:
        song = song.replace('/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/', '')
        songBox.insert(END, song)


# Add One Song
def addOne():
    song = filedialog.askopenfilename(initialdir='songs/', title='Choose a Song',
                                      filetypes=(('mp3 Files', "*.mp3"), ))
    song = song.replace('/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/', '')
    songBox.insert(END, song)


# Previous Song
def back():
    # Reset slider and Status Bar
    statusBar.config(text='')
    mySlider.config(value=0)
    # Get the current song tuple number
    next_song = songBox.curselection()
    # Add one to the current song number
    next_song = next_song[0] - 1
    # Grad song title from playlist
    song = songBox.get(next_song)
    # Add directory structure and mp3 to song title
    song = f'/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/{song}'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar in playlist listbox
    songBox.selection_clear(0, END)
    # Activate new song bar
    songBox.activate(next_song)
    # Set active bar to next song
    songBox.select_set(next_song, last=None)


# Delete All Songs
def deleteAll():
    stop()
    songBox.delete(0, END)
    pygame.mixer.music.stop()


# Delete One Song
def deleteOne():
    stop()
    songBox.delete(ANCHOR)
    pygame.mixer.music.stop()


# Forward Songs
def forward():
    # Reset slider and Status Bar
    statusBar.config(text='')
    mySlider.config(value=0)
    # Get the current song tuple number
    next_song = songBox.curselection()
    # Add one to the current song number
    next_song = next_song[0] + 1
    # Grad song title from playlist
    song = songBox.get(next_song)
    # Add directory structure and mp3 to song title
    song = f'/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/{song}'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar in playlist listbox
    songBox.selection_clear(0, END)
    # Activate new song bar
    songBox.activate(next_song)
    # Set active bar to next song
    songBox.select_set(next_song, last=None)


# Pause
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# Play
def play():
    # Set stopped variable to false so song can play
    global stopped
    stopped = False
    # Get the song
    song = songBox.get(ACTIVE)
    # Search the song on directory
    song = f'/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/{song}'
    # Load and Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Call Time Function
    songTime()


# Slider
def slide(x):
    # Get the song
    song = songBox.get(ACTIVE)
    # Search the song on directory
    song = f'/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/{song}'
    # Load and Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(mySlider.get()))


# Time info
def songTime():
    # Check for double time
    if stopped:
        return
    # Grab current song elapsed time
    currentTime = pygame.mixer.music.get_pos()/1000
    # Get currently playing song
    current_song = songBox.curselection()
    song = songBox.get(current_song)
    song = f'/home/matheus/PycharmProjects/Tkinter/Programas/MP3Player/songs/{song}'
    # Get song length with mutagen
    songMut = MP3(song)
    global songLength
    songLength = songMut.info.length
    # Converted to time format
    convertedLength = time.strftime("%M:%S", time.gmtime(songLength))
    if int(mySlider.get()) == int(songLength):
        # Output time to status bar
        statusBar.config(text=convertedLength)
    elif paused:
        pass
    elif int(mySlider.get()) == int(currentTime+1):
        # Update slider
        sliderPosition = int(songLength)
        mySlider.config(to=sliderPosition, value=currentTime + 1)
    else:
        sliderPosition = int(songLength)
        mySlider.config(to=sliderPosition, value=mySlider.get())
        # Converted to time format
        convertedTime = time.strftime("%M:%S", time.gmtime(int(mySlider.get())))
        # Output time to status bar
        statusBar.config(text=convertedTime + '/' + convertedLength)
        # Move this thing along by one second
        nextTime = int(mySlider.get()) + 1
        mySlider.config(value=nextTime)
    # Update time
    statusBar.after(1000, songTime)


# Stop
def stop():
    # Reset slider and Status Bar
    statusBar.config(text='')
    mySlider.config(value=0)
    # Stop song
    pygame.mixer.music.stop()
    songBox.selection_clear(ACTIVE)
    # Clear statusBar
    statusBar.config(text="")
    # Set stop variable to true
    global stopped
    stopped = True


def volume(x):
    pygame.mixer.music.set_volume(volumeSlider.get())


# ---------------------------------------------------
# GUI
root = Tk()
root.title('Music Tkinter Player')
root.geometry('600x370')
root.resizable(False, False)


# ---------------------------------------------------
# Variables
global paused
paused = False
global stopped
stopped = False
pygame.mixer.init()


# ---------------------------------------------------
# Frames
masterFrame = Frame(root)
controlsFrame = Frame(masterFrame)
volumeFrame = LabelFrame(masterFrame, text="Volume")
# Song Box
songBox = Listbox(masterFrame, background="black", fg="pink", width=60, selectbackground="pink",
                  selectforeground="black")
# Images
backImg = ImageTk.PhotoImage(Image.open('images/back.png'))
forwardImg = ImageTk.PhotoImage(Image.open('images/forward.png'))
playImg = ImageTk.PhotoImage(Image.open('images/play.png'))
pauseImg = ImageTk.PhotoImage(Image.open('images/pause.png'))
stopImg = ImageTk.PhotoImage(Image.open('images/stop.png'))
# Buttons
backButton = Button(controlsFrame, image=backImg, borderwidth=0, command=back)
forwardButton = Button(controlsFrame, image=forwardImg, borderwidth=0, command=forward)
playButton = Button(controlsFrame, image=playImg, borderwidth=0, command=play)
pauseButton = Button(controlsFrame, image=pauseImg, borderwidth=0, command=lambda: pause(paused))
stopButton = Button(controlsFrame, image=stopImg, borderwidth=0, command=stop)
# Menu
myMenu = Menu(root)
root.config(menu=myMenu)
# Add Songs
addSong = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Add Songs", menu=addSong)
addSong.add_command(label="Add One Song", command=addOne)
addSong.add_command(label="Add Many Song", command=addMany)
# Delete Songs
removeSong = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Remove Songs", menu=removeSong)
removeSong.add_command(label="Delete One Song", command=deleteOne)
removeSong.add_command(label="Delete All Song", command=deleteAll)
# Status Bar
statusBar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
# Sliders
mySlider = ttk.Scale(masterFrame, from_=0, to=100, orient=HORIZONTAL, value=0, length=360, command=slide)
volumeSlider = ttk.Scale(volumeFrame, from_=0, to=1, orient=VERTICAL, value=1, length=140, command=volume)


# ---------------------------------------------------
# Layouts
masterFrame.pack(pady=20)
songBox.grid(row=0, column=0)
volumeFrame.grid(row=0, column=1, padx=20)
controlsFrame.grid(row=1, column=0, pady=20)
backButton.grid(row=0, column=0, padx=7)
forwardButton.grid(row=0, column=1, padx=7)
playButton.grid(row=0, column=2, padx=7)
pauseButton.grid(row=0, column=3, padx=7)
stopButton.grid(row=0, column=4, padx=7)
statusBar.pack(fill=X, side=BOTTOM, ipady=2)
mySlider.grid(row=2, column=0, pady=10)
volumeSlider.pack(pady=10)


# ---------------------------------------------------
# MainLoop
root.mainloop()