import os
import tkinter
import tkinter as tk
from tkinter import messagebox

import pchealthlogic


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My PC Health")
        self.root.geometry("700x500")
        self.root.protocol("WM_DELETE_WINDOW",self.action_btn_exit)
        image_path = os.path.abspath("D:\Python Projects\PC_HEALTH\icons\icon.png")
        self.root_icon = tk.PhotoImage(file=image_path)
        #self.root_icon=tkinter.PhotoImage(file="icons/root_icon.png")
        self.root.iconphoto(True,self.root_icon)
        self.lbl_user_name=tkinter.Label(self.root,text="Enter Your Name",font=("consolas",12,"bold"))
        self.entry_user_name=tkinter.Entry(self.root, font=("consolas",12,"bold"))
        self.btn_diagnose=tkinter.Button(self.root,text="Diagnose",font=("consolas",12,"bold"),command=self.action_btn_diagnose)
        self.lbl_free_disk_space=tkinter.Label(self.root,text="Free Space Available",font=("consolas",12,"bold"))
        self.entry_free_disk_space=tkinter.Entry(self.root,font=("consolas",12,"bold"))
        self.lbl_per_cpu_usage=tkinter.Label(self.root,text="average CPU usage in past 1 second",font=("consolas",12,"bold"))
        self.entry_per_cpu_usage=tkinter.Entry(self.root,font=("consolas",12,"bold"))
        self.lbl_prescription=tkinter.Label(self.root,text="Prescription",font=("consolas",12,"bold"))
        self.text_prescription=tkinter.Text(self.root,font=("consolas",10,"normal"),width=50,height=20)
        self.text_prescription.config(wrap=tk.WORD)
        self.btn_reset=tkinter.Button(self.root,text="Reset",font=("consolas",12,"bold"),command=self.action_btn_reset)
        self.btn_exit=tkinter.Button(self.root,text="Exit",font=("consolas",12,"bold"),command=self.action_btn_exit)
        self.lbl_user_name.grid(row=0,column=0,sticky='E')
        self.entry_user_name.grid(row=0,column=1,sticky='E',padx=4,pady=4)
        self.btn_diagnose.grid(row=1,column=0,sticky='E',padx=4,pady=4)
        self.lbl_free_disk_space.grid(row=2,column=0,sticky='E',padx=4,pady=4)
        self.entry_free_disk_space.grid(row=2,column=1,sticky='E',padx=4,pady=4)
        self.lbl_per_cpu_usage.grid(row=3,column=0,sticky='E',padx=4,pady=4)
        self.entry_per_cpu_usage.grid(row=3,column=1,sticky='E',padx=4,pady=4)
        self.lbl_prescription.grid(row=4,column=0,sticky='E',padx=4,pady=4)
        self.text_prescription.grid(row=4,column=1,sticky='E',padx=4,pady=4,columnspan=5)
        self.btn_reset.grid(row=5,column=0,sticky='E',padx=4,pady=4)
        self.btn_exit.grid(row=5,column=1,sticky='E',padx=4,pady=4)
        self.user_name=None
        self.root.mainloop()

    def action_btn_diagnose(self):
        self.user_name=self.entry_user_name.get()
        greeting_message="Welcome Dear, "+self.user_name+", "
        if self.user_name=='':
            messagebox.showerror("User Name Missing","Please Enter Your Name")
            self.entry_user_name.delete(0,tkinter.END)
            self.entry_user_name.focus()
        else:
            self.obj_pchealthlogic=pchealthlogic.PCHealth()
            self.entry_free_disk_space.delete(0,tkinter.END)
            self.entry_per_cpu_usage.delete(0,tkinter.END)
            self.entry_free_disk_space.insert(0, self.obj_pchealthlogic.get_free_disk_space())
            self.entry_per_cpu_usage.insert(0,self.obj_pchealthlogic.get_per_cpu_usage())
            if self.obj_pchealthlogic.is_free_disk_space_ok():
                self.entry_free_disk_space.config(fg="green")
            else:
                self.entry_free_disk_space.config(fg="red")
            if self.obj_pchealthlogic.is_per_cpu_usage_ok():
                self.entry_per_cpu_usage.config(fg='green')
            else:
                self.entry_per_cpu_usage.config(fg="red")
            if self.obj_pchealthlogic.is_per_cpu_usage_ok() and self.obj_pchealthlogic.is_free_disk_space_ok():
                self.text_prescription.delete(1.0,tkinter.END)
                message="Congratulations \U0001F600 Your PC is Healthy "
                self.text_prescription.insert(1.0,greeting_message+message)
            elif self.obj_pchealthlogic.is_per_cpu_usage_ok()==False and self.obj_pchealthlogic.is_free_disk_space_ok()==False:
                self.text_prescription.delete(1.0,tkinter.END)
                message1="Sad News \U0001F614 disk usage is not healthy, There are some suggestions to reduce the disk usage : Delete unnecessary files, Uninstall unused " \
                        "programs,Move files to external storage,Clear cache and temporary files,Use disk cleanup " \
                        "tools,Compress files, Disable hibernation, Disable system restore, Upgrade to a larger hard " \
                        "drive\n\n"
                message2="Sad News \U0001F614 cpu usage is not healthy, There are some suggestions to reduce the CPU Overhead : Close unnecessary applications and " \
                         "processes, Optimize programs, Use caching, Use concurrency, Use hardware acceleration, " \
                         "Upgrade hardware"
                self.text_prescription.insert(1.0,greeting_message+message1+message2)
            elif self.obj_pchealthlogic.is_free_disk_space_ok()==True and self.obj_pchealthlogic.is_per_cpu_usage_ok()==False:
                message1="Good News \U0001F600 Disk Usage is in healthy state\n\n"
                message2="Sad News \U0001F614 cpu usage is not healthy, There are some suggestions to reduce the CPU Overhead : Close unnecessary applications and " \
                         "processes, Optimize programs, Use caching, Use concurrency, Use hardware acceleration, " \
                         "Upgrade hardware"
                self.text_prescription.insert(1.0,greeting_message+message1+message2)
            elif self.obj_pchealthlogic.is_free_disk_space_ok()==False and self.obj_pchealthlogic.is_per_cpu_usage_ok()==True:
                message1 = "Sad News \U0001F614 disk usage is not healthy, There are some suggestions to reduce the disk usage : Delete unnecessary files, Uninstall unused " \
                        "programs,Move files to external storage,Clear cache and temporary files,Use disk cleanup " \
                        "tools,Compress files, Disable hibernation, Disable system restore, Upgrade to a larger hard " \
                        "drive\n\n"
                message2="Good News \U0001F600 CPU usage is in healthy state"
                self.text_prescription.insert(1.0,greeting_message+message1+message2)

    def action_btn_exit(self):
        ans = messagebox.askyesno("Quitting...", "Are You Sure Want to Exit ?")
        if ans == True:
            self.root.destroy()

    def action_btn_reset(self):
        self.entry_free_disk_space.delete(0,tk.END)
        self.entry_per_cpu_usage.delete(0,tk.END)
        self.text_prescription.delete(1.0,tk.END)




obj = MyGUI()
