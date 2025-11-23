from tkinter import *
from tkinter import Tk
from tkinter import ttk, filedialog,messagebox
from pygame import mixer
import pygame
import os
from PIL import Image, ImageTk


#Creating the root window 
root=Tk()
root.title('The Vimsical ')
root.geometry("980x600+80+20")
root.configure(bg= "black")
root.resizable(False, False)


var1=StringVar(value='K-Pop')
var_search=IntVar(value=1)
search_nm=StringVar(value='')
# artist=StringVar()
pause_status=0
q_status=0
mixer.init()
qlist=[]
night_songs=[]
Nimages={}
Fimages={}
Dimages={}
Eimages={}
Kimages={}
Dance={'2step.mp3': 'Ed Sheeran', 'Audio.mp3': 'LSD', 
       'Back to You.mp3': 'Louis Tomlinson', 
       'Bon Appétit.mp3': 'Katy Perry · Migos', 'Break My Heart.mp3': 'Dua Lipa', 
       'Chained To The Rhythm.mp3': 'Katy Perry · Skip Marley', 
       'Cheap Thrills.mp3': 'Sia · Sean Paul', 'Dancing With A Stranger.mp3': 
        'Sam Smith · Normani', 'Dynamite.mp3': 'BTS', 
        'Havana.mp3': 'Camila Cabello · Young Thug', 
        'Holiday.mp3': 'Now United', 'Let Me Move You.mp3': 'Sabrina Carpenter', 
        'Levitating .mp3': 'Dua Lipa', 'Make It Right.mp3': 'BTS',
        'One Love.mp3': 'One Love (Official Music Video)', 
        'Permission to Dance.mp3': 'BTS', 'Reggaetón Lento .mp3': 'CNCO · Little Mix', 
        'Swalla.mp3': 'Jason Derulo · Nicki Minaj · Ty Dolla $ign', 
        'Taki Taki.mp3': 'DJ Snake · Selena Gomez · Ozuna · Cardi B',
        'The Way I Are.mp3': 'Bebe Rexha', 'Tip Toe.mp3': 'Jason Derulo · French Montana'}

Night={'All of Me.mp3': 'John Legend', 'Alone Pt II.mp3': 'Ava Max', 
       'Angel Baby.mp3': 'Troye Sivan', 'At My Worst.mp3': 'Pink Sweat$', 
       'Back To You.mp3': 'Selena Gomez', 'Backwards.mp3': 'Alexander Stewart', 
       'Beauty and the Beast.mp3': 'Ariana Grande · John Legend', 
       'bury a friend.mp3': 'Billie Eilish', 'cardigan.mp3': 'Taylor Swift', 
       'Cashmere.mp3': 'RITA ORA', 'Dancing With A Stranger.mp3': 'Sam Smith · Normani', 
       'Diamonds.mp3': 'Sam Smith', 'Dusk Till Dawn.mp3': 'ZAYN · Sia', 
       'Eastside.mp3': 'benny blanco · Halsey · Khalid', 'Faded.mp3': 'Alan Walker', 
       'Feel Me.mp3': 'Selena Gomez', 'Fetish.mp3': 'Selena Gomez · Gucci Mane', 
       'Ghost.mp3': 'Justin Bieber', 'Good For You.mp3': 'Selena Gomez', 
       'Him and I.mp3': 'G-Eazy · Halsey', 'Hurts So Good.mp3': 'Astrid S', 
       'I Do not Wanna Live Forever.mp3': 'ZAYN · Taylor Swift', 
       'i hate u i love u .mp3': "gnash · Olivia O'brien", 
       'Infinity.mp3': 'Jaymes Young', 'It Aint Me.mp3': 'Kygo · Selena Gomez', 
       'It is Ok If You Forget Me.mp3': 'Astrid S', 'Let Me Down Slowly.mp3': 'Alec Benjamin', 
       'Like I am Gonna Lose You.mp3': 'Meghan Trainor · John Legend', 'Living Hell.mp3': 'Bella Poarch',
       'Love Me Harder.mp3': 'Ariana Grande · The Weeknd', 'lovely.mp3': 'Billie Eilish · Khalid',
       'MIDDLE OF THE NIGHT.mp3': 'Sam Roman', 'Mon Soleil.mp3': 'Ashley Park', 
       'Never Forget You.mp3': 'Zara Larsson · MNEK', 'no tears left to cry.mp3': 'Ariana Grande',
       'On My Way.mp3': 'Fredrik Borch Olsen', 'One Call Away.mp3': 'Charlie Puth', 
       'One Last Time.mp3': 'Ariana Grande', 'Our Song.mp3': 'Anne-Marie Nicholson',
       'People You Know.mp3': 'Selena Gomez', 'Perfect.mp3': 'Ed Sheeran',
       'Photograph.mp3': 'Ed Sheeran', 'pov.mp3': 'Ariana Grande', 
       'Scared to Be Lonely.mp3': 'Martin Garrix · Dua Lipa', 
       'Scars To Your Beautiful.mp3': 'Alessia Cara', 'See You Again .mp3': 'Wiz Khalifa · Charlie Puth', 
       'So Am I.mp3': 'Ava Max', 'Speechless.mp3': 'Alan Menken', 
       'Stuck with U.mp3': 'Ariana Grande · Justin Bieber', 'Takeaway.mp3': 'The Chainsmokers · Illenium · Lennon Stella', 
       'Thinking out Loud.mp3': 'Ed Sheeran', 'Trampoline.mp3': 'SHAED', 
       'We Dont Talk Anymore.mp3': 'Charlie Puth · Selena Gomez', 
       'willow.mp3': 'Taylor Swift', 'Without Me.mp3': 'Halsey', 'Wolves.mp3': 'Selena Gomez · Marshmello', 
       'Wow.mp3': 'Zara Larsson', 'You Belong With Me.mp3': 'Taylor Swift'}

Energize={'34+35.mp3': 'Ariana Grande', 'Anywhere.mp3': 'RITA ORA', 
          'Audio.mp3': 'LSD', 'Baby.mp3': 'Justin Bieber · Ludacris', 
          'Bad Blood.mp3': 'Taylor Swift', 'Bad Guy.mp3': 'Billie Eilish', 
          'Bad Habits.mp3': 'Ed Sheeran', 'Believer.mp3': 'Imagine Dragons', 
          'Bon Appétit.mp3': 'Katy Perry · Migos', 'Bones.mp3': 'Imagine Dragons',
          'Capital Letters.mp3': 'Hailee Steinfeld · BloodPop®', 
          'Chained To The Rhythm.mp3': 'Katy Perry · Skip Marley', 
          'Cheap Thrills.mp3': 'Sia · Sean Paul', 'Dance Monkey.mp3': 'Tones And I', 
          "Don't Start Now.mp3": 'Dua Lipa', 'Flowers.mp3': 'Miley Cyrus', 
          'For You.mp3': 'Liam Payne · Rita Ora', 'Genius.mp3': 'Thomas Wesley Pentz', 
          'Heaven.mp3': 'Julia Michaels', 'Hey Mama.mp3': 'David Guetta · Afrojack · Bebe Rexha · Nicki Minaj', 
          'Holiday.mp3': 'Now United', 'I Knew You Were Trouble.mp3': 'Taylor Swift', 
          'Let Me Move You.mp3': 'Sabrina Carpenter', 'Let You Love Me.mp3': 'RITA ORA', 
          'Lonely Together.mp3': 'Avicii', 'Love You Like A Love Song.mp3': 'Selena Gomez & The Scene', 
          'Me Too.mp3': 'Meghan Trainor', 'Meant to Be.mp3': 'Bebe Rexha · Florida Georgia Line', 
          'Natural.mp3': 'Imagine Dragons', 'One Kiss.mp3': 'Calvin Harris · Dua Lipa',
          'Personal.mp3': 'HRVY', 'positions.mp3': 'Ariana Grande', 'Say My Name.mp3': 'Bebe Rexha',
          'Shake It Off.mp3': 'Taylor Swift', 'Side To Side.mp3': 'Ariana Grande · Nicki Minaj', 
          'Sorry.mp3': 'Justin Bieber', 'South of the Border.mp3': 'Ed Sheeran · Camila Cabello · Cardi B',
          'STAY.mp3': 'The Kid LAROI · Justin Bieber', 'Strip That Down.mp3': 'Liam Payne · Quavo', 
          'Style.mp3': 'Taylor Swift', 'Sucker.mp3': 'Jonas Brothers', 
          'Swalla.mp3': 'Jason Derulo · Nicki Minaj · Ty Dolla $ign',
          'Taki Taki.mp3': 'DJ Snake · Selena Gomez · Ozuna · Cardi B', 
          'The Middle.mp3': 'Zedd · Maren Morris · Grey', 
          "There's Nothing Holdin' Me Back.mp3": 'Shawn Mendes', 
          'Thumbs.mp3': 'Sabrina Carpenter', 'Thunderclouds.mp3': 'LSD ',
          'Toxic.mp3': 'Britney Spears', 'Watermelon Sugar.mp3': 'Harry Styles',
          'We Are Never Ever Getting Back Together.mp3': 'Taylor Swift', 
          'Why.mp3': 'Sabrina Carpenter', 'Worth It.mp3': 'Fifth Harmony · Kid Ink',
          'Your Song.mp3': 'Anne'}

Favourites={'Alone Pt II.mp3': 'Alan Walker/Ava Max', 
            'BabyBaby .mp3': 'CHOI SANG YEOP · Jo Eun Ae',
            'Bad Guy.mp3': 'Billie Eilish', 'Believer.mp3': 'Imagine Dragons', 
            'Cheap Thrills.mp3': 'Sia · Sean Paul', 'Dont Start Now.mp3': 'Dua Lipa',
            'Kill Em With Kindness.mp3': 'Selena Gomez', 'Lost In Japan.mp3': 'Shawn Mendes', 
            'Love You Like A Love Song.mp3': 'Love You Like A Love Song', 
            'My Universe.mp3': 'Coldplay · BTS', 'No tears left to cry.mp3': 'Ariana Grande', 
            'One Love.mp3': 'Now United/R3HAB', 'Permission to Dance.mp3': 'BTS ', 
            'Safari.mp3': 'Serena', 'Slow Down.mp3': 'Selena Gomez', 'Souvenir.mp3': 'Selena Gomez', 
            'Taki Taki.mp3': 'DJ Snake · Selena Gomez · Ozuna · Cardi B', 'Wasabi.mp3': 'Little Mix', 
            'Whatever It Takes.mp3': 'Imagine Dragons'}

Kpop = {'Opening Sequence': 'TOMORROW X TOGETHER',
    'Good Boy Gone Bad': 'TOMORROW X TOGETHER',
    '_WORLD': 'SEVENTEEN',  'OMG': 'NewJeans','Still Monster':'ENHYPEN',
    'Back for More': 'TOMORROW X TOGETHER','Save ME':'BTS',
    'Cat & Dog': 'TOMORROW X TOGETHER','DNA':'BTS',
    'Sweet Venom': 'ENHYPEN',  'Happily Ever After': 'TOMORROW X TOGETHER',
    '락 (樂) LALALALA': 'Stray Kids', 'Still With You': 'Jung Kook',
    'Still Life': 'RM', '9 and Three Quarters': 'TOMORROW X TOGETHER',
    'One In A Billion': 'ENHYPEN', 'Bite Me': 'ENHYPEN',
    'I AM': 'IVE', 'Boy with Luv': 'BTS', 'Deja Vu':'ATEEZ',
    'Who U Are': 'KANG DANIEL', 'MOONLIGHT SUNRISE': 'TWICE',
    'Polaroid Love': 'ENHYPEN', 'Stay Alive': 'Jungkook',
    '다라리 (DARARI)': 'TREASURE', 'Not For Sale': 'ENHYPEN',
    'Given-Taken': 'ENHYPEN', 'No Manners': 'SuperM',
    '죽겠다 (KILLING ME)': 'iKON', 'Butterfly': 'BTS',
    'FANCY': 'TWICE', 'VIBE': 'TAEYANG','HOME':'BTS',
    'Love, Maybe': 'SECRET NUMBER',"Can't You See Me" : 'TOMORROW X TOGETHER',
    'CROWN': 'TOMORROW X TOGETHER', 'Magic': 'TOMORROW X TOGETHER',
    'I NEED U': 'BTS', 'We Lost The Summer': 'TOMORROW X TOGETHER',
    'Ready to Love': 'SEVENTEEN', 'Blood Sweat & Tears': 'BTS',
    'Any song (아무노래)': 'ZICO', 'Devil by the Window': 'TOMORROW X TOGETHER',
    'I CAN\'T STOP ME': 'TWICE', '음악의 신': 'SEVENTEEN',
    'Darl+ing': 'SEVENTEEN', 'FOR YOU': 'BTS','Love Talk':'WayV',
    '전야 前夜 The Eve': 'EXO',  '특 S-Class': 'Stray Kids','House Of Cards':'BTS',
    'Airplane pt. 2': 'BTS', 'Stay Gold': 'BTS','For Us':'V', 'TRUE':'Yaori',
    'The Truth Untold (feat. Steve Aoki)': 'BTS', 'Black Swan': 'BTS',
    '꽃(FLOWER)': 'JISOO', 'Anti-Romantic': 'TOMORROW X TOGETHER',
    'My You': 'Jung Kook',  'Pied Piper': 'BTS', 'Slow Dancing':'V',
    'So What': 'BTS',  'Dance The Night Away': 'TWICE','Rainy Days':'V',
    'Love Shot': 'EXO', 'GO HARD': 'TWICE',  'Filter': 'BTS',
    '손오공': 'SEVENTEEN', '0X1=LOVESONG (I Know I Love You) ': 'TOMORROW X TOGETHER',
    'FAKE LOVE': 'BTS',  'Drunk-Dazed': 'ENHYPEN','Euphoria':'BTS',
    'Take Two': 'BTS',  'LO$ER=LO♡ER': 'TOMORROW X TOGETHER'}

def Add_Music():
    Playlist.delete(0,END)
    if var1.get() == 'Favourites':
        add_files('Favourites')
    elif var1.get() == 'Night':
        add_files('Night')
    elif var1.get() == 'Energize':
        add_files('Energize')
    elif var1.get() == 'Dance':
        add_files('Dance')
    elif var1.get() == 'K-Pop':
        add_files('K-Pop')
    else:
        print("Please choose an option")

def add_files(word):
    path = "C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/{}".format(word)
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song[:-4])    
                night_songs.append(song[:-4])
    

shm=PhotoImage(file=r"C:\Users\aggar\Music\#PythonJourney\The Vimsical\Assets\m_search3.png").subsample(1)
sbi=PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/search_button.png").subsample(2)
def search_music():
    tp=Toplevel(bg='black')
    tp.geometry("285x330+445+120")
    tp.title("Search for Music")        
    tp.grab_set()
    sh=Label(tp,image=shm,background='black').pack(side='top',pady=10)
    arts=Radiobutton(tp,variable=var_search,value=1,text='By Artist',font=('Georgia',16), bg='black', fg='blue').pack(anchor='w',pady=3,padx=40)
    mn=Radiobutton(tp,value=2,variable=var_search,text= 'By Song Name',font=('Georgia',16), bg='black', fg='blue').pack(anchor='w',padx=40)
    se=Entry(tp,textvariable=search_nm,font=('Georgia',14),width=20).place(x=30-10,y=200)
    sb=Button(tp,image=sbi,bg='black',command=search_engine, border=0).place(x=90,y=305-50)

def search_engine():
    sv=var_search.get()
    nm=search_nm.get()
    if nm!='':
        Playlist.delete(0,END)
        if sv==1:
            a=[key for key,value in Kpop.items() if nm.lower() in value.lower()]
            b=[key[:-4] for key,value in Favourites.items() if nm.lower() in value.lower()]
            c=[key[:-4] for key,value in Night.items() if nm.lower() in value.lower()]
            d=[key[:-4] for key,value in Dance.items() if nm.lower() in value.lower()]
            e=[key[:-4] for key,value in Energize.items() if nm.lower() in value.lower()]
            final_list=a+b+c+d+e
            for i in final_list:
                Playlist.insert(END, i)    
        elif sv==2:
            a=[key for key,value in Kpop.items() if nm.lower() in key.lower()]
            b=[key[:-4] for key,value in Favourites.items() if  nm.lower() in key.lower()]
            c=[key[:-4] for key,value in Night.items() if  nm.lower() in key.lower()]
            d=[key[:-4] for key,value in Dance.items() if  nm.lower() in key.lower()]
            e=[key[:-4] for key,value in Energize.items() if  nm.lower() in key.lower()]
            final_list=a+b+c+d+e
            for i in final_list:
                Playlist.insert(END, i)    
    else:
        messagebox.showerror("Error", "Please enter an input for the Artist  or Song name.")  
                
            
        
                
for word in ['Night','Dance','Energize','Favourites']:
    path = "C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/{}".format(word)
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                song=song[:-4]
                im=ImageTk.PhotoImage(Image.open(f'C:/Users/aggar/Music/#PythonJourney/The Vimsical/Images/{word}/{song}.jpg').resize((180,180)))
                if word=='Night':
                    Nimages[song]=im
                elif word=='Dance':
                    Dimages[song]=im
                elif word=='Energize':
                    Eimages[song]=im
                elif word=='Favourites':
                    Fimages[song]=im
                
path = "C:/Users/aggar/Music/#PythonJourney/The Vimsical/Images/K-Pop"
if path:
    os.chdir(path)
    songs = os.listdir(path)
    for song in songs:
        song=song[:-4]
        im=ImageTk.PhotoImage(Image.open(f'C:/Users/aggar/Music/#PythonJourney/The Vimsical/Images/K-Pop/{song}.jpg').resize((180,180)))
        Kimages[song]=im
            

def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    var.set(Music_Name)
    print(Music_Name)
    if Music_Name in Nimages.keys():
        label1['image']=list(Nimages.values())[list(Nimages.keys()).index(Music_Name)]
        artist.set('~' + Night[Music_Name+'.mp3'])        
        mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Night/'+Music_Name+'.mp3')
    elif Music_Name in Eimages.keys():
        label1['image']=list(Eimages.values())[list(Eimages.keys()).index(Music_Name)]
        artist.set('~' + Energize[Music_Name+'.mp3'])
        mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Energize/'+Music_Name+'.mp3')
    elif Music_Name in Fimages.keys():
        label1['image']=list(Fimages.values())[list(Fimages.keys()).index(Music_Name)]
        artist.set('~' + Favourites[Music_Name+'.mp3'])
        mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Favourites/'+Music_Name+'.mp3')
    elif Music_Name in Dimages.keys():
        label1['image']=list(Dimages.values())[list(Dimages.keys()).index(Music_Name)]
        artist.set('~' + Dance[Music_Name+'.mp3'])
        mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Dance/'+Music_Name+'.mp3')
    elif Music_Name in Kpop.keys():
        label1['image']=list(Kimages.values())[list(Kimages.keys()).index(Kpop[Music_Name])]
        artist.set('~' + Kpop[Music_Name])
        mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/K-pop/'+Music_Name+'.mp3')
    mixer.music.play()

    
def Play_Next():
    Music= Playlist.get(ACTIVE)
    album=str(var1.get())
    qlist.insert(0,album+':'+Music)
    
def Add_to_Queue():
    Music= Playlist.get(ACTIVE)
    album=str(var1.get())
    qlist.append(album+':'+Music)

def music_pause():
    global pause_status
    mixer.music.pause()
    pause_status=1

def music_unpause():
    global pause_status
    mixer.music.unpause()
    pause_status=0
    
def check_music_status():
    global pause_status
    if (not pygame.mixer.music.get_busy()) :
        if pause_status==0 and qlist!=[]:
            M=(qlist.pop(0)).split(':')
            var.set(M[1])
            Music_Name=M[1]
            if Music_Name in Nimages.keys():
                label1['image']=list(Nimages.values())[list(Nimages.keys()).index(Music_Name)]
                artist.set('~' + Night[Music_Name+'.mp3'])        
                mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Night/'+Music_Name+'.mp3')
            elif Music_Name in Eimages.keys():
                label1['image']=list(Eimages.values())[list(Eimages.keys()).index(Music_Name)]
                artist.set('~' + Energize[Music_Name+'.mp3'])
                mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Energize/'+Music_Name+'.mp3')
            elif Music_Name in Fimages.keys():
                label1['image']=list(Fimages.values())[list(Fimages.keys()).index(Music_Name)]
                artist.set('~' + Favourites[Music_Name+'.mp3'])
                mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Favourites/'+Music_Name+'.mp3')
            elif Music_Name in Dimages.keys():
                label1['image']=list(Dimages.values())[list(Dimages.keys()).index(Music_Name)]
                artist.set('~' + Dance[Music_Name+'.mp3'])
                mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/Dance/'+Music_Name+'.mp3')
            elif Music_Name in Kpop.keys():
                label1['image']=list(Kimages.values())[list(Kimages.keys()).index(Kpop[Music_Name])]
                artist.set('~' + Kpop[Music_Name])
                mixer.music.load('C:/Users/aggar/Music/#PythonJourney/The Vimsical/Musics/K-pop/'+Music_Name+'.mp3')
            mixer.music.play()
    root.after(400,  check_music_status)
    
def q_remove():
    m=Queuelist.get(ACTIVE)
    Queuelist.delete(ACTIVE)
    for s in qlist:
        if m in s:
            qlist.remove(s)
    

qh=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/queue_head.png').subsample(4,4)
rm=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/remove.png').subsample(4,4)
def Queue():
    global Queuelist
    tp=Toplevel(bg='black')
    tp.geometry("250x400+440+60")
    tp.title("Queue")        
    tp.grab_set()
    
    qhl=Label(tp,image=qh,background='black').pack(side='top')
    
    Q_Frame = Frame(tp, bd=2, bg='black')
    Q_Frame.place(x=20, y=75, width=220-4, height=260)
    Scroll = Scrollbar(Q_Frame)
    Queuelist = Listbox(Q_Frame, width=28,highlightcolor='purple', highlightthickness=2,borderwidth=0,activestyle='none',font=("Georgia",12), bg="Black", fg="blue", selectbackground="purple", cursor="hand2",  yscrollcommand=Scroll)
    Scroll.config(command=Queuelist.yview)
    Scroll.pack(side=RIGHT, fill=Y)
    Queuelist.pack(side=LEFT, fill=BOTH)
    
    rb=Button(tp,image=rm,bg='black',command=q_remove, border=0).place(x=80,y=345)
    
    for s in qlist:
        song=s.split(':')[1]
        Queuelist.insert('end',song)
        Scroll.update_idletasks()
                

#icon
image_icon = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/icon.png") 
root.iconphoto(False,image_icon)


#Frames
frame1=Frame(root,bg='black').pack()
canvas=Canvas(root,width=0, height=600)
canvas.place(x=360,y=0)
frame3=Frame(root,bg='black',padx=50).pack()
canvas1=Canvas(root,width=0, height=600,bg='darkblue')
canvas1.place(x=650,y=0)
frame5=Frame(root,bg='black').pack(side='left')


#Music Controls

path1='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/frame.png'
image1 = Image.open(path1).resize((300-5,300+10))
img1 = ImageTk.PhotoImage(image1)
label0 = Label(image=img1,bg='black')
label0.place(x=40-10,y=80-15)

path2='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Artists/default.png'
image = Image.open(path2).resize((180,180))
img = ImageTk.PhotoImage(image)
label1 = Label(image=img,bg='black')
label1.place(x=90,y=140-10)

head=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/Head.png').subsample(3,3)
l1=Label(frame1,image=head, bg='black').place(x=0,y=10)

var=StringVar()
label2=Label(root,textvariable=var,width=25,font=('Gabriola',24,'italic','underline'),bg='BLACK',fg='gold', justify='center')
label2.place(x=10,y=345-10)
artist=StringVar()
label3=Label(root,textvariable=artist,width=30,font=('Gabriola',20),fg='purple', bg='black',justify='center')
label3.place(x=10,y=380)

Button_Play = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/play.png").subsample(6)
Button(root, image=Button_Play, bg="black", bd=0, command=Play_Music).place(x=115+30, y=422+10)
Button_Stop = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/stop.png").subsample(6)
Button(root, image=Button_Stop, bg="black", bd=0, command=lambda: mixer.music.fadeout(1000)).place(x=30+30, y=500+10)
Button_Resume = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/resume new.png").subsample(6)
Button(root, image=Button_Resume,bg='black', bd=0, command=music_unpause).place(x=115+30, y=500+10)
Button_Pause = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/pause img.png").subsample(6)
Button(root, image=Button_Pause, bg="black", bd=0, command=music_pause).place(x=200+30, y=500+10)



#Playlists
play_head=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/playlist.png').subsample(3,3)
l2=Label(frame3,image=play_head, bg='black').pack()


R1 = Radiobutton(frame3, text="Favourites\t\t",variable=var1,value='Favourites',font=("Georgia",16,'italic'),background='black',fg='red')
R1.flash()
R1.pack()
R2 = Radiobutton(frame3, text="Night\t\t", variable=var1, value='Night', font=("Georgia",16,'italic'),background='black',fg='red')
R2.pack()
R3 = Radiobutton(frame3, text="Energize\t\t ", variable=var1, value='Energize', font=("Georgia",16,'italic'),background='black',fg='red')
R3.pack()
R4 = Radiobutton(frame3, text="Dance\t\t ", variable=var1, value='Dance', font=("Georgia",16,'italic'),background='black',fg='red')
R4.pack()
R5 = Radiobutton(frame3, text="K-Pop\t\t ", variable=var1, value='K-Pop', font=("Georgia",16,'italic'),background='black',fg='red')
R5.pack()

l0=Label(frame3,bg='black')
l0.pack()

select = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/select2.png").subsample(6,6)
Button(root, image=select, bg="black", bd=0, command=Add_Music).place(x=430+3,y=310)

playNext = PhotoImage(file="C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/playnext.png").subsample(6,6)
Button(root, image=playNext, bg="black", bd=0, command=Play_Next).place(x=424,y=360+35)

Button(root, bg="black",bd=0, command=Add_to_Queue,height=3,width=6).place(x=600-8,y=550-12)

copyright=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/copyright.png').subsample(4,4)
l10=Label(root,image=copyright, bg='black')
l10.place(x=400,y=470)

#Songs
song_head=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/song.png').subsample(3,3)
l3=Label(frame5,image=song_head, bg='black').place(x=680,y=0)

queue=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/queue.png').subsample(3,3)
lq=Button(frame5,image=queue, bg='black', border=0, activebackground='black', command=Queue).place(x=900,y=30)


Frame_Music = Frame(root, bd=2, bg='black')
Frame_Music.place(x=680, y=115, width=280, height=450+10)
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=28,highlightcolor='gold', highlightthickness=2,borderwidth=0,activestyle='underline',font=("Georgia",12), bg="Black", fg="blue", selectbackground="gold", cursor="hand2", bd=0, yscrollcommand=Scroll)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

search=PhotoImage(file='C:/Users/aggar/Music/#PythonJourney/The Vimsical/Assets/search.png')
search_icon=Button(frame5,image=search,bg='black',border=0,command=search_music).place(x=890,y=125)

check_music_status()
root.mainloop()
