try:
    import os
    import pafy
    import tkinter
    import darkdetect
    import customtkinter
    from typing import Any
    from pytube import YouTube
    from threading import Thread
    from tkinter import filedialog
    from tkinter import messagebox
    from typing_extensions import Self
    from tkinter.font import (BOLD , NORMAL)
    from tkinter.__init__ import (StringVar, Label)
    from customtkinter.widgets.customtkinter_entry import CTkEntry
    from customtkinter.widgets.customtkinter_button import CTkButton
    from customtkinter.widgets.customtkinter_checkbox import CTkCheckBox

except ModuleNotFoundError.__doc__ as mnfe:
    raise mnfe

finally:
    ... 

    



class YoutubeDownloader:
    def __init__(self : Self) -> None:
        super(YoutubeDownloader , self).__init__()
        self.root = tkinter.Tk()
        self.root.title(string='Youtube Downloader')
        self.root.geometry(newGeometry='950x300')
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
                self.downloadStatus.configure(background='#F5EEDC')
                self.videoLinkLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.videoLinkLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.videoLiveLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.videoAuthorLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.channelPrivateLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.videoID.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.channelPrivateLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.status.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.labelCheckBoxSelectInfo.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.svVideoAuthor.configure(background='#F5EEDC' , foreground='#000000')
                self.svChannelPrivate.configure(background='#F5EEDC' , foreground='#000000')
                self.svVideoLive.configure(background='#F5EEDC' , foreground='#000000')
                self.svVideoID.configure(background='#F5EEDC' , foreground='#000000')
                self.svChannelPrivate.configure(background='#F5EEDC' , foreground='#000000')
                self.svViewsCount.configure(background='#F5EEDC' , foreground='#000000')
                self.viewsCount.configure(background='#F5EEDC' , foreground='#1D94D0')
                self.highestQualityBtn.configure(bg_color='#F5EEDC' , fg_color='#1D94D0')
                self.lowestQualityBtn.configure(bg_color='#F5EEDC' , fg_color='#1D94D0')
                self.browseSaveDialogLabel.configure(background='#F5EEDC' , foreground='#1D94D0')
            elif (darkdetect.isDark()):
                customtkinter.set_appearance_mode(mode_string='dark')
                self.root.configure(background='#323331')
                self.linkEntry.configure(fg_color='#CA3E47')
                self.linkDestination.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.downloadStatus.configure(background='#323331')
                self.videoLinkLabel.configure(background='#323331' , foreground='#CA3E47')
                self.videoLiveLabel.configure(background='#323331' , foreground='#CA3E47')
                self.videoAuthorLabel.configure(background='#323331' , foreground='#CA3E47')
                self.channelPrivateLabel.configure(background='#323331' , foreground='#CA3E47')
                self.svVideoAuthor.configure(background='#323331' , foreground='#ffffff')
                self.svChannelPrivate.configure(background='#323331' , foreground='#ffffff')
                self.svVideoLive.configure(background='#323331' , foreground='#ffffff')
                self.svVideoID.configure(background='#323331' , foreground='#ffffff')
                self.svViewsCount.configure(background='#323331' , foreground='#ffffff')
                self.videoID.configure(background='#323331' , foreground='#CA3E47')
                self.channelPrivateLabel.configure(background='#323331' , foreground='#CA3E47')
                self.viewsCount.configure(background='#323331' , foreground='#CA3E47')
                self.videoLinkLabel.configure(background='#323331' , foreground='#CA3E47')
                self.status.configure(background='#323331' , foreground='#CA3E47')
                self.labelCheckBoxSelectInfo.configure(background='#323331' , foreground='#CA3E47')
                self.highestQualityBtn.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.lowestQualityBtn.configure(bg_color='#323331' , fg_color='#CA3E47')
                self.browseSaveDialogLabel.configure(background='#323331' , foreground='#CA3E47')
            self.tester.after(ms=2500 , func=getTheme)
            
        def browseFile(arg : Any):
            if (arg == 'browse'):
                downloadDirectory = filedialog.askdirectory(initialdir=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__))) , title='Save Video')
                self.svPath.set(downloadDirectory)
                
        def startDownload():
            startThread = Thread(target=downloadVideo)
            startThread.start()
            
        def getVideoInfo():
            try:
                videoAuthor = YouTube(url=self.svLink.get()).vid_info['videoDetails']['author']
                channelPrivate = YouTube(url=self.svLink.get()).vid_info['videoDetails']['isPrivate']
                videoLive = YouTube(url=self.svLink.get()).vid_info['videoDetails']['isLiveContent']
                videoId = YouTube(url=self.svLink.get()).vid_info['videoDetails']['videoId']
                videoViews = f"{int(YouTube(url=self.svLink.get()).vid_info['videoDetails']['viewCount']):,}"
                
                self.svVideoAuthor.configure(text=videoAuthor)
                if (channelPrivate == 0):
                    channelPrivate = 'False'
                    self.svChannelPrivate.configure(text=channelPrivate)
                elif (channelPrivate == 1):
                    channelPrivate = 'True'
                    self.svChannelPrivate.configure(text=channelPrivate)
                if (videoLive == 0):
                    videoLive = 'False'
                    self.svVideoLive.configure(text=videoLive)
                elif (videoLive == 1):
                    videoLive = 'True'
                    self.svVideoLive.configure(text=videoLive)
                self.svVideoID.configure(text=videoId)
                self.svViewsCount.configure(text=videoViews)
            except:
                pass
                
        def downloadVideo():
            if (self.svLink.get() is not None):
                if (self.highestQualityBtn.check_state == True):
                    try:
                        self.downloadStatus.configure(text='Downloading' , fg='#ffea00')
                        self.root.update()
                        video = YouTube(url=self.svLink.get())
                        getVideoInfo()
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
                        getVideoInfo()
                        videoStream = video.streams.get_lowest_resolution()
                        videoStream.download(self.svPath.get())
                        self.downloadStatus.configure(text='Downloaded' , fg='#28A745')
                    except Exception:
                        self.downloadStatus.configure(text='Failed' , fg='#CA3E47')
                        self.root.update()
            else:
                messagebox.askokcancel(title='Invalid Link' , message='Please Enter a Valid Link')
        
        def checkBoxesChecked():
            if (self.highestQualityBtn.check_state is True):
                self.labelCheckBoxSelectInfo.configure(text='You Can Only Select Highest')
            if (self.lowestQualityBtn.check_state is True):
                self.labelCheckBoxSelectInfo.configure(text='You Can Only Select Lowest')
            if ((self.highestQualityBtn.check_state is True) and (self.lowestQualityBtn.check_state is True)):
                self.labelCheckBoxSelectInfo.configure(text='You Cannot Select Both')
            if ((self.highestQualityBtn.check_state is False) and (self.lowestQualityBtn.check_state is False)):
                self.labelCheckBoxSelectInfo.configure(text='')
                
        
        self.labelCheckBoxSelectInfo = Label(
            master=self.root ,
            text= '',
            font=('System' , 7 , NORMAL)
        )
        
        self.labelCheckBoxSelectInfo.place(x=30 , y=160)
                    
        self.status = Label(master=self.root , text='Status :' , font=('normal' , 12 , BOLD))
        
        self.status.place(x=350 , y=183.4)
                
        self.downloadStatus = Label(master=self.root , text=f'Not Using' , foreground='#ffea00' , font=('normal' , 10 , BOLD))
        
        self.downloadStatus.place(x=465 , rely=0.65 , anchor=tkinter.CENTER)
            
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
            command= startDownload ,
            cursor='hand2'
        )
        
        self.btnDownload.place(x=190 , y=235)
        
        self.highestQualityBtn = CTkCheckBox(
            master=self.root ,
            text='Highest Quality' ,
            state=tkinter.NORMAL ,
            command=checkBoxesChecked
        )
        
        self.highestQualityBtn.place(x=30 , y = 184)
        
        self.lowestQualityBtn = CTkCheckBox(
            master=self.root ,
            text='Lowest Quality' ,
            state=tkinter.NORMAL ,
            command=checkBoxesChecked
        )
        
        self.lowestQualityBtn.place(x=180 , y = 184)
        
        self.videoAuthorLabel = Label(master=self.root , text='Author :' , font=('normal' , 11 , BOLD))
        
        self.videoAuthorLabel.place(x=604 , y=30)
        
        self.svVideoAuthor = Label(master=self.root , text='' , font=('normal' , 10 , BOLD))
        
        self.svVideoAuthor.place(x=690 , y=30)
        
        self.channelPrivateLabel = Label(master=self.root , text='Private :' , font=('normal' , 11 , BOLD))
        
        self.channelPrivateLabel.place(x=600 , y=80)
        
        self.svChannelPrivate = Label(master=self.root , text='' , font=('normal' , 10 , BOLD))
        
        self.svChannelPrivate.place(x=690 , y=80)
        
        self.videoLiveLabel = Label(master=self.root , text='Live :' , font=('normal' , 11 , BOLD))
        
        self.videoLiveLabel.place(x=619 , y=130)
        
        self.svVideoLive = Label(master=self.root , text='' , font=('normal' , 10 , BOLD))
        
        self.svVideoLive.place(x=690 , y=130)
        
        self.videoID = Label(master=self.root , text='Video ID :' , font=('normal' , 11 , BOLD))
        
        self.videoID.place(x=591 , y=180)
        
        self.svVideoID = Label(master=self.root , text='' , font=('normal' , 10 , BOLD))
        
        self.svVideoID.place(x=690 , y=180)
        
        self.viewsCount = Label(master=self.root , text='Views :' , font=('normal' , 11 , BOLD))
        
        self.viewsCount.place(x=609 , y=230)
        
        self.svViewsCount = Label(master=self.root , text='' , font=('normal' , 10 , BOLD))
        
        self.svViewsCount.place(x=690 , y=230)
            
        getTheme()
        
        self.root.mainloop()
        
        
if (__name__ == '__main__' and __package__ is None):
    YoutubeDownloader()