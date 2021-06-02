
import tkinter
import platform
import os  
# import asyncio  
from tkinter import *
import tkinter.font as TKFont
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import messagebox
import webbrowser
from ttkthemes import ThemedStyle




from terminal import Terminal
from utilities import *

# Notepad Version
NotepadVer = "VeryCoolIDE Public Alpha 1.0"
WindowsVer = platform.platform()



    
class Notepad:



    __root = Tk()
    
    def add_terminal(self, terminal):
        self.terminal = terminal
  
    # default window width and height
    __thisWidth = 1200
    __thisHeight = 1200
    __thisTextArea = Text(__root)
    terminal = Terminal(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisRunMenu = Menu(__thisMenuBar, tearoff=0)
    __thisSettingsMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
      
    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None





  
    def __init__(self,**kwargs):
        # Set icon
        try:
            self.__root.wm_iconbitmap("IDE.ico") 
        except:
            pass
  
        # Set window size (the default is 300x300)
  
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
  
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
  
        # Set the window text
        self.__root.title("Untitled - VeryCoolIDE")


  
        # Center the window
        screenWidth = 1200 #self.__root.winfo_screenwidth()
        screenHeight = 1200 #self.__root.winfo_screenheight()
      
        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
          
        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight /2) 
          
        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top)) 
  
        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
  
        # Add controls (widget)
        self.__thisTextArea.grid(sticky = N + E + S + W, row=0,column=0)
        self.terminal.grid(sticky = N + E + S + W, row=1,column=0)
          
        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)    
          
        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)
          
        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)    
  
        # To create a line in the dialog        
        self.__thisFileMenu.add_separator()                                         
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)     
          
        # To give a feature of cut 
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)   
   
        # to give a feature of copy    
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
          
        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
          
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)  

        # To give a feature of running the script
        self.__thisRunMenu.add_command(label="Run",
                                        command=self.__coderun)

        self.__thisRunMenu.add_command(label="Compile",
                                        command=self.__codecompile) 
        
        # To give a feature of running & debugging
        self.__thisMenuBar.add_cascade(label="Run",
                                       menu=self.__thisRunMenu)  


        

        # To create a feature of description of the notepad

        self.__thisHelpMenu.add_command(label="About VeryCoolIDE",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

 
  
        self.__root.config(menu=self.__thisMenuBar)
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                    
          
        # Scrollbar will adjust automatically according to the content        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        center(self.__root, self.__thisWidth, self.__thisHeight)
      
          
    def __quitApplication(self):
        self.__root.destroy()
        # exit()
  
    def __showAbout(self):
        showinfo("About VeryCoolIDE",f"IDE Version: {NotepadVer}\nOperating System: {WindowsVer}")
    


    def raise_exception(self, string):
        messagebox.showerror("Exception  Found!", string)
    
    def raise_python_not_found_exception(self):
        messagebox.showerror(
            "Python Installation not Found!",
            "Python (3.x) not installed, or not in PATH.\nMake sure python is in path to continue execution."
        )

    def raise_pyinstaller_not_found_exception(self):
        install = messagebox.askyesno(
            "Pyinstaller not Installed!",
            "Proceed to install pyinstaller?"
        )
        if ans:
            install_pyinstaller_cmd = "pip install pyinstaller"
            self.terminal.automation("{0}".format(install_pyinstaller_cmd))
    
    def check_python(self):
        if check_python_installation():
            return True
        else:
            self.raise_python_not_found_exception()
            return False

    def check_pyinstaller(self):
        if check_pyinstaller_installation():
            return True
        else:
            self.raise_pyinstaller_not_found_exception()
            return False

    def __openFile(self):
          
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
  
        if self.__file == "":
              
            # no file to open
            self.__file = None
        else:
              
            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - VeryCoolIDE")
            self.__thisTextArea.delete(1.0,END)
  
            file = open(self.__file,"r")
  
            self.__thisTextArea.insert(1.0,file.read())
  
            file.close()
  
          
    def __newFile(self):
        self.__root.title("Untitled - VeryCoolIDE")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
  
    def __saveFile(self):
  
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
  
            if self.__file == "":
                self.__file = None
            else:
                  
                # Try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                  
                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - VeryCoolIDE")
                  
              
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
  
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
  
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
  
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __coderun(self, *args):
        if self.__file is None:
            return
        if not self.check_python():
            return
        dir_cmd = "cd {0}".format(os.path.dirname(self.__file))
        build_cmd = "python {1}".format(os.getcwd(), self.__file)
        self.terminal.automation("{0} && {1}".format(dir_cmd, build_cmd))

    def __codecompile(self, *args):
        if self.__file is None:
            return

        # loop = asyncio.get_event_loop()
        # checks = loop.create_task(self.check_pyinstaller())
        # loop.run_until_complete(checks)

        if not self.check_python() or not self.check_pyinstaller():
            return
        dir_cmd = "cd {0}".format(os.path.dirname(self.__file))
        build_cmd = "pyinstaller  -F {1}".format(os.getcwd(), self.__file)
        self.terminal.automation("{0} && {1}".format(dir_cmd, build_cmd))

  
    def run(self):

        # Run main application
        self.__root.mainloop()
        print(NotepadVer)
        

# Run main application
notepad = Notepad(width=1500,height=800)
notepad.run()

