from tkinter import *
from tkinter import ttk
from pytube import YouTube


def download(labelInfo,url,type):
    try:
        labelInfo.configure(text="Téléchargement en cours ...")
        url=(url.get())
        type=(type.get())
        yt = YouTube(url)
        title=yt.title
        if(type=="MP3"):
            print("mp3")
            (yt.streams.filter(only_audio=True, abr="128kbps")).first().download(filename=title+".mp3")
        elif(type=="MP4"):
            tab=(yt.streams.filter(file_extension='mp4',res='720p'))
            L=[]
            for e in tab:
                if(e.includes_audio_track):
                    L.append(e)
            L[0].download()
        else:
            labelInfo.configure(text="Type de fichier non sélectionné")
            return
        labelInfo.configure(text="Téléchargement fait avec succès")
    except:
        labelInfo.configure(text="Erreur, lien non valide")
        return
   



def interface(root):    
    root.title("Téléchargement Youtube")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    url = StringVar()
    url_entry = ttk.Entry(mainframe, width=40, textvariable=url)
    url_entry.grid(column=2, row=1, sticky=(W, E))


    labelInfo=ttk.Label(mainframe, text="")
    labelInfo.grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="Lien de la vidéo").grid(column=3, row=1, sticky=W)
    type = StringVar()
    mp4 = ttk.Radiobutton(mainframe, text='MP4 (vidéo)', variable=type, value='MP4')
    mp3 = ttk.Radiobutton(mainframe, text='MP3 (audio)', variable=type, value='MP3')
    mp4.grid(column=1, row=2, sticky=(W,E))
    mp3.grid(column=2, row=2, sticky=(W))

    ttk.Button(mainframe, text="Télécharger", command=lambda: download(labelInfo,url,type)).grid(column=2, row=3, sticky=W)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    url_entry.focus()
    root.bind("<Return>", ())

root=Tk()
interface(root)
root.mainloop()

