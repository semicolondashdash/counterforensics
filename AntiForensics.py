from Tkinter import *
import ttk
import os, stat
import shutil

class Run:

    def __init__(self, master):

        master.title('Anti-Forensics Tool')
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        
        self.LabelA = ttk.Label(self.frame_content, text = "Please Select Browser to erase", font = ('Arial', 11, 'bold')).grid(row = 0, column = 0, columnspan = 2)
        
        self.ButtonA = ttk.Button(self.frame_content, text = "Delete Chrome", command = self.Delete_Chrome).grid(row = 1, column =0, columnspan =4, padx =5,pady=5, sticky = 'nsew')
        self.ButtonB = ttk.Button(self.frame_content, text = "Delete IE", command = self.Delete_IE).grid(row = 2, column =0, columnspan =4, padx =5,pady=5, sticky = 'nsew')
        #self.ButtonC = ttk.Button(self.frame_content, text = "Delete Edge", command = self.Delete_Edge).grid(row = 3, column =0, columnspan =4, padx =5,pady=5, sticky = 'nsew')
        self.ButtonD = ttk.Button(self.frame_content, text = "Delete FireFox", command = self.Delete_FF).grid(row = 4, column =0, columnspan =4, padx =5, pady=5, sticky = 'nsew')
        
    def Delete_Chrome(self):
        try:
            #All Chrome artifacts are located in a SQLlite DB under %localappdata%\Google\Chrome\User Data\Default
            home = os.environ['USERPROFILE']
            path = home + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
            os.chmod(path, stat.S_IWRITE)
            shutil.rmtree(path)
            return True
        except WindowsError:
            return False
        
    def Delete_IE(self):
        try:
            #Windows API to delete IE history
            cmd = "RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 4351"
            os.system(cmd)
            #Delete IE Cookies that the above command does not
            #STILL NEED TO DELETE THE FOLLOWING 
            #NTUSER\Software\Microsoft\Windows\CurrentVersion\SettingsSync\Namespace\BrowserSettings\WinInet-Internet-Explorer\LastRoamed
            home = os.environ['USERPROFILE']
            paths = [
            home + '\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE',
            home + '\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Low\\IE',
            home + '\\AppData\\Local\\Microsoft\\Windows\\INetCookies',
            home + '\\AppData\\Local\\Microsoft\\Vault',
            home + '\\AppData\\Roaming\\Microsoft\\Vault',
            home + '\\AppData\\Local\\Packages\\windows_ie_ac_001',
            home + '\\AppData\\Local\\Microsoft\\Windows\\WebCache',
            home + '\\AppData\\Local\\Microsoft\\Internet Explorer\\Recovery'
            ]
            for path in paths:
                os.chmod(path, stat.S_IWRITE)
                shutil.rmtree(path)
            return True
        except WindowsError:
            return False
			
    def Delete_FF(self):
        try:
            home = os.environ['USERPROFILE']
            paths = [home + '\\AppData\\Roaming\\Mozilla', home + '\\AppData\\Local\\Mozilla']
 
            for path in paths:
                os.chmod(path, stat.S_IWRITE)
                shutil.rmtree(path)
            return
        except WindowsError:
            return False
			
def main():
    
    root = Tk()
    run = Run(root)
    root.mainloop()

if __name__ == "__main__": main()
