# NTKUtils by not-nef

import ctypes
import re
import tkinter
from functools import partial
import platform
from tkinter import ttk

from win32mica import MICAMODE, ApplyMica

from .cfgtools import *

win_error = "Your window specification does not appear to be a tkinter window."

def placeappincenter(window:tkinter.Tk):
    try:
        window.update()
        x_coordinate = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
        y_coordinate = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
        window.geometry("+{}+{}".format(x_coordinate, y_coordinate - 20))
    except:
        print(f"{win_error}")

def ttktheme(window:tkinter.Tk, source_file, theme):
    try:
        try:
            window.tk.call("source", f"{source_file}")
        except:
            print("The specified theme file doesnt seem to exist.")

        if theme == "dark" or theme == "light":
            window.tk.call("set_theme", f"{theme}")
        else:
            print("Unknown theme specification. Use dark or light.")
    except:
        print("Your window specification does not appear to be a tkinter window.")

def windowsetup(window:tkinter.Tk, title="Window", icon=None, resizeable=True, size="300x300"):
    try:
        window.title(f"{title}")
    except:
        print(f"{win_error}")

    if not icon == None:
        try:
            icon_image = tkinter.PhotoImage(file=f"{icon}")
            window.iconphoto(False, icon_image)
        except:
            print("The file that your specified path leads to either doesnt exist or your window specification is not a tkinter window")
    else:
        pass

    if not resizeable == True:
        try:
            window.resizable(False, False)
        except:
            print(f"{win_error}")
    else:
        pass

    try:
        window.geometry(f"{size}")
    except:
        print("Your size specification seems to be wrong. Do it like this: WIDTHxHEIGHT")

def sv_msgbox(parent, title, details, icon, darktb=None, *, buttons):
    dialog = tkinter.Toplevel()

    result = None

    big_frame = ttk.Frame(dialog)
    big_frame.pack(fill="both", expand=True)
    big_frame.columnconfigure(0, weight=1)
    big_frame.rowconfigure(0, weight=1)

    info_frame = ttk.Frame(big_frame)
    info_frame.grid(row=0, column=0, sticky="nsew")
    info_frame.columnconfigure(1, weight=1)
    info_frame.rowconfigure(1, weight=1)

    try:
        color = big_frame.tk.call("set", "themeColors::dialogInfoBg")
    except tkinter.TclError:
        color = big_frame.tk.call("ttk::style", "lookup", "TFrame", "-background")

    icon_label = ttk.Label(info_frame, image=icon, anchor="nw", background=color)
    if icon is not None:
        icon_label.grid(row=0, column=0, sticky="nsew", padx=(12, 0), pady=10, rowspan=2)

    title_label = ttk.Label(info_frame, text=title, anchor="nw", font=("Segoe UI Variable", 14, "bold"), background=color)
    title_label.grid(row=0, column=1, sticky="nsew", padx=(12, 17), pady=(10, 8))

    detail_label = ttk.Label(info_frame, text=details, anchor="nw", background=color, font=("Segoe UI", 10))
    detail_label.grid(row=1, column=1, sticky="nsew", padx=(12, 17), pady=(5, 10))

    button_frame = ttk.Frame(big_frame, padding=(22, 22, 12, 22), style="Dialog_buttons.TFrame")
    button_frame.grid(row=2, column=0, sticky="nsew")

    def on_button(value):
        nonlocal result
        result = value
        dialog.destroy()

    for index, button_value in enumerate(buttons):
        style = None
        state = None
        default = False
        sticky = "nes" if len(buttons) == 1 else "nsew"

        if len(button_value) > 2:
            if button_value[2] == "accent":
                style = "Accent.TButton"
                default = True
            elif button_value[2] == "disabled":
                state = "disabled"
            elif button_value[2] == "default":
                default = True

        button = ttk.Button(button_frame, text=button_value[0], width=18, command=partial(on_button, button_value[1]), style=style, state=state)
        if default:
            button.bind("<Return>", button["command"])
            button.focus()

        button.grid(row=0, column=index, sticky=sticky, padx=(0, 10))
        button_frame.columnconfigure(index, weight=1)

    dialog.update()

    placeappincenter(dialog)

    if darktb:
        dark_title_bar(dialog)

    #dialog.transient(parent)
    #dialog.grab_set()

    #dialog.wait_window()
    return result

def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ctypes.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ctypes.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value))

def blur_window_background(window:tkinter.Tk, bg_color=None, dark:bool=False):
    ttkbgcolor = str(ttk.Style().lookup(".", "background"))
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', ttkbgcolor)
    if match:                      
        bg_color = ttkbgcolor
    else:
        if bg_color == None:
            bg_color="#fafafa"
            window.configure(bg=bg_color)

    if int(platform.version().lstrip("10.0.")) >= 22000:
        window.wm_attributes("-transparent", bg_color)
        window.update()
        if dark:
            ApplyMica(
                HWND=ctypes.windll.user32.GetParent(window.winfo_id()), ColorMode=MICAMODE.DARK
            )
        else:
            ApplyMica(
                HWND=ctypes.windll.user32.GetParent(window.winfo_id()), ColorMode=MICAMODE.LIGHT
            )
    else:
        # Disabled because it didnt work.
        #
        #from BlurWindow.blurWindow import GlobalBlur
        #window.wm_attributes("-transparent", bg_color)
        #if dark:
        #    GlobalBlur(
        #        ctypes.windll.user32.GetParent(window.winfo_id()),
        #        Acrylic=True,
        #        hexColor="#1c1c1c",
        #        Dark=True,
        #    )
        #else:
        #    pass
        print("Your operating system doesnt support mica blurring!")

def isint(string, bottomlimit=None, upperlimit=None):
    if bottomlimit == None and upperlimit == None:
        try:
            int(string)
            return True
        except ValueError:
            return False
    elif not bottomlimit == None and upperlimit == None:
        try:
            int(string)
            if int(string) < bottomlimit:
                return False
            else:
                return True
        except ValueError:
            return False
    elif bottomlimit == None and not upperlimit == None:
        try:
            int(string)
            if int(string) > upperlimit:
                return False
            else:
                return True
        except ValueError:
            return False
    elif not bottomlimit == None and not upperlimit == None:
        try:
            int(string)
            if int(string) < bottomlimit or int(string) > upperlimit:
                return False
            else:
                return True
        except ValueError:
            return False

def clearwin(win:tkinter.Tk):
    slaves_list = win.slaves() + win.place_slaves() + win.grid_slaves()
    for slave in slaves_list:
        slave.destroy()          