try:
    import os
    import tkinter
    import darkdetect
    import customtkinter
    from pytube import YouTube
    from tkinter.font import BOLD
    from tkinter import filedialog
    from tkinter import messagebox
    from typing_extensions import Self
    from tkinter.__init__ import (StringVar, Label)
    from customtkinter.widgets.customtkinter_entry import CTkEntry
    from customtkinter.widgets.customtkinter_button import CTkButton
    from customtkinter.widgets.customtkinter_checkbox import CTkCheckBox

except ModuleNotFoundError.__doc__ as mnfe:
    raise mnfe

finally:
    ...




class YoutubeDownloader(tkinter.Tk):
    def __init__(self : Self) -> None:
        self.root = tkinter.Tk()
        self.root.title(string='Youtube Downloader')
        self.root.geometry(newGeometry='550x300')
        self.root.resizable(width=False , height=False)
        self.tester = Label(master=self.root)
        self.svLink = StringVar(master=self.root)
        self.svPath = StringVar(master=self.root)
        
        def getTheme():
            if (darkdetect.isLight()):
                customtkinter.set_appearance_mode(mode_string='light')
                self.root.configure(background='#F5EEDC')
                self.linkEntry.configure(fg_color='#1D94D0')
                self.linkDestination.configure(bg_color='#F5EEDC' , fg_color='#1D94D0')
                self.downloadStatus.configure(background='#F5EEDC' , foreground='#ffea00')
                self.videoLinkLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.status.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.highestQualityBtn.configure(bg_color='#F5EEDC' , fg_color='#1D94D0')
                self.lowestQualityBtn.configure(bg_color='#F5EEDC' , fg_color='#1D94D0')
                self.browseSaveDialogLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
            elif (darkdetect.isDark()):
                customtkinter.set_appearance_mode(mode_string='dark')
                self.root.configure(background='#323331')
                self.linkEntry.configure(fg_color='#CA3E47')
                self.linkDestination.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.downloadStatus.configure(background='#323331' , foreground='#ffea00')
                self.videoLinkLabel.configure(background='#323331' , foreground='#CA3E47')
                self.status.configure(background='#323331' , foreground='#CA3E47')
                self.highestQualityBtn.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.lowestQualityBtn.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.browseSaveDialogLabel.configure(background='#323331' , foreground='#CA3E47')
            self.tester.after(ms=2500 , func=getTheme)
            
        def browseFile(arg):
            if (arg == 'browse'):
                downloadDirectory = filedialog.askdirectory(initialdir=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__))) , title='Save Video')
                self.svPath.set(downloadDirectory)
                
        def downloadVideo(arg):
            if (arg == 'download'):
                if (self.svLink.get() is not None):
                    if (self.highestQualityBtn.check_state == True):
                        try:
                            self.downloadStatus.configure(text='Downloading' , fg='#ffea00')
                            self.root.update()
                            video = YouTube(url=self.svLink.get())
                            videoStream = video.streams.get_highest_resolution()
                            videoStream.download(self.svPath.get())
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                        except Exception:
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                    elif (self.lowestQualityBtn.check_state == True):
                        try:
                            self.downloadStatus.configure(text='Downloading' , fg='#ffea00')
                            self.root.update()
                            video = YouTube(url=self.svLink.get())
                            videoStream = video.streams.get_lowest_resolution()
                            videoStream.download(self.svPath.get())
                            self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                        except Exception:
                            self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                            self.root.update()
                else:
                    messagebox.askokcancel(title='Invalid Link' , message='Please Enter a Valid Link')
                    
        self.status = Label(master=self.root , text='Status :' , font=('normal' , 12 , BOLD))
        
        self.status.place(x=320 , y=183.4)
                
        self.downloadStatus = Label(master=self.root , text=f'Not Using' , font=('normal' , 10 , BOLD))
        
        self.downloadStatus.place(relx=0.82 , rely=0.65 , anchor=tkinter.CENTER)
            
        self.videoLinkLabel = Label(master=self.root , text='Video Link :' , font=('normal' , 12 , BOLD))
        
        self.videoLinkLabel.place(x=20 , y=30)
        
        self.linkEntry = CTkEntry(
            master=self.root ,
            textvariable=self.svLink ,
            corner_radius=5 ,
            width=400 ,
            justify=tkinter.CENTER
        )
        
        self.linkEntry.place(x=128 , y=28)
        
        self.browseSaveDialogLabel = Label(master=self.root , text='Destination :' , font=('normal' , 12 , BOLD))
        
        self.browseSaveDialogLabel.place(x=12 , y=105)
        
        self.linkDestination = CTkEntry(
            master=self.root ,
            textvariable=self.svPath ,
            corner_radius=5 ,
            width=285 ,
            justify=tkinter.CENTER
        )
        
        self.linkDestination.place(x=128 , y = 102)
        
        self.btnBrowse = CTkButton(
            master=self.root ,
            text='Browse' ,
            corner_radius=5 ,
            width=100 ,
            command=lambda:browseFile(arg='browse') ,
            cursor='hand2'
        )
        
        self.btnBrowse.place(x=428 , y = 102)
        
        self.btnDownload = CTkButton(
            master=self.root ,
            text='Download' ,
            corner_radius=5 ,
            width=220 ,
            command=lambda:downloadVideo(arg='download') ,
            cursor='hand2'
        )
        
        self.btnDownload.place(relx=0.32 , y=235)
        
        self.highestQualityBtn = CTkCheckBox(
            master=self.root ,
            text='Highest Quality' ,
            state=tkinter.NORMAL
        )
        
        self.highestQualityBtn.place(relx=0.05 , y = 184)
        
        self.lowestQualityBtn = CTkCheckBox(
            master=self.root ,
            text='Lowest Quality' ,
            state=tkinter.NORMAL
        )
        
        self.lowestQualityBtn.place(relx=0.3 , y = 184)
            
        getTheme()
        
        self.root.mainloop()
        
        
if (__name__ == '__main__' and __package__ is None):
    YoutubeDownloader()