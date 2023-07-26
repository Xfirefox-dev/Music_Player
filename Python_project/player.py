import tkinter as tk
from tkinter import filedialog
import easygui
import os
import pygame
import customtkinter as ctk
from PIL import Image, ImageTk
from threading import *
import time
import math
from mutagen.mp3 import MP3

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=ctk.CTk()
root.title('Zapp Music Player')
root.geometry('400x480')

#images
play_img=ctk.CTkImage(Image.open("icons/play.png"),size=(50,50))
pause_img=ctk.CTkImage(Image.open("icons/pause.png"),size=(50,50))
skip_img=ctk.CTkImage(Image.open("icons/forward.png"),size=(50,50))
prev_img=ctk.CTkImage(Image.open("icons/previous.png"),size=(50,50))
player_bg=ctk.CTkImage(Image.open("icons/zapp player.png"),size=(230,230))
icon1=Image.open("icons/add_song.png")
ad_song=ImageTk.PhotoImage(icon1)
icon2=Image.open("icons/add_songs.png")
ad_songs=ImageTk.PhotoImage(icon2)




def get_path():
    filename=easygui.fileopenbox()
    new_path=filename.replace(os.sep,'/')
    return new_path
directory_list=[]   
def add_song():
    songs=filedialog.askopenfilenames(title="Select Music Folder:",filetypes=(('mp3 files','*.mp3'),))
    for song in songs:
        song_name =os.path.basename(song)
        directory_path=song.replace(song_name,"")
        directory_list.append({'path':directory_path,'song':song_name})
        songs_list.insert('end',song_name)
    songs_list.select_set('0')    
        
    
   



def threading():
    t1=Thread(master=progress)
    t1.start()




def play_music():
    pygame.init()
    progress['value']=0
    time_elapsed_label['text']="00:00"
    song_name=songs_list.get('active')
    directory_path=None
    for dictio in directory_list:
        if dictio['song']== song_name:
            directory_path=dictio['path']
    song_with_path=f'{directory_path}/{song_name}'
    music_data= MP3(song_with_path)
    music_length=int(music_data.info.length)
    music_duration['text']= time.strftime('%M:%S',time.gmtime(music_length))
    
    
    progress.set= music_length
    play_btn.configure(image=pause_img)
    pygame.mixer.music.load(song_with_path)
    pygame.mixer.music.play()
    scale_update()
    
def scale_update():
    if progress('value')< music_duration:
        progress["value"]+=1
        
        time_elapsed_label["text"]=time.strftime('%M:%S',time.gmtime(progress.get()))
        updater = root.after(1000,scale_update())
        
    
def pause_music():
    #play_btn = ctk.CTkButton(master=root,image=play_img,text='',command=play_music,width=3,corner_radius=25,fg_color="transparent",hover="true")
    #play_btn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
    pass
def skip_music():
    pass   
def prev_music():
    pass
def volume(value):
    pygame.init()
    pygame.mixer.music.set_volume(value)





#buttons
song_photo=ctk.CTkLabel(master=root,text="",image=player_bg)
song_photo.place(relx=0.5, rely=0.4,anchor=tk.CENTER)
play_btn = ctk.CTkButton(master=root,image=play_img,text='',command=play_music,width=3,corner_radius=25,fg_color="transparent",hover="false")
play_btn.place(relx=0.5,rely=0.8, anchor=tk.CENTER)
skip_btn = ctk.CTkButton(master=root,image=skip_img,text="",command=skip_music,width=3,fg_color="transparent",hover="false")
skip_btn.place(relx=0.65,rely=0.8, anchor=tk.CENTER)
prev_btn = ctk.CTkButton(master=root,image=prev_img,text="",command=prev_music,width=3,fg_color="transparent",hover="false")
prev_btn.place(relx=0.35,rely=0.8,anchor=tk.CENTER)
volume_slider= ctk.CTkSlider(master=root,from_=0,to=1,command=volume,width=10,height=60,button_color="#1DB954",button_hover_color="#1DB954",orientation="vertical")
volume_slider.place(relx=0.75,rely=0.8,anchor=tk.CENTER)
time_elapsed_label=ctk.CTkLabel(master=root,text="00:00",fg_color="transparent",padx=5)
time_elapsed_label.place(relx=0.2,rely=0.66)
music_duration=ctk.CTkLabel(master=root,text="00:00",fg_color="transparent",padx=5)
music_duration.place(relx=0.7,rely=0.66)
progress=ctk.CTkSlider(master=root,button_color="#1DB954",button_hover_color="#1DB954",width=240,progress_color="#1DB954",)
progress.place(relx=0.5,rely=0.72,anchor=tk.CENTER)
progress.configure()
menu_bar=tk.Menu(root,activebackground="black")
root.configure(menu=menu_bar)
m1=tk.Menu(master=menu_bar,background="white",tearoff=False,bd=0,activebackground="green")
menu_bar.add_cascade(label="Actions",menu=m1,background="black")
m1.add_command(label="Add Song",image=ad_song,compound="left",command=add_song)
m1.add_command(label="Add Multiple Songs",command="get_path()",image=ad_songs,compound="left")
songs_list=tk.Listbox(master=root,width=30,height=18,background="black",fg="blue",relief="flat")
songs_list.place(relx=0.85,rely=0.15)
root.mainloop()

