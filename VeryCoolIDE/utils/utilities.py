import sys, os
import subprocess
import asyncio


def center(win, width=100, height=100):
    win.update_idletasks()

    width = width
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = height
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    win.deiconify()

def fetch_installed_packages():
    req = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in req.split()]
    return installed_packages


def check_python_installation():
    path = os.environ['PATH'].split(';')
    for i in path:
        if 'Python3' in i:
            return True
    return False


def check_pyinstaller_installation():
    packages = fetch_installed_packages()
    if 'pyinstaller' in packages:
        return True

    return False