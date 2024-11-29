
import os,sys
from tkinter import *

perm = int(os.getuid())
if perm != 0:
    print("You must be a root to use this program.")
    sys.exit(1)

window = Tk()
window.geometry("600x250")
window.title("Jellyb0n Simple Firewall")
window.geometry("600x400")
window.title("Jellyb0n Simple Firewall v1.0")


target_port = Label(window, text="Enter port to close: ")
target_port.grid(column=0, row=0)
@@ -35,16 +36,22 @@
blocker_ent.grid(column=1, row=8)
blocker_inf = Label(window, text="")
blocker_inf.grid(column=0, row=9)

conn_lbl = Label(window, text="Interface: ")
conn_lbl.grid(column=0, row=10)
iface_ent = Entry(window, width="15")
iface_ent.grid(column=1, row=10)


def closer():
   try:
      killer0 = "iptables -A INPUT -p tcp --destination-port {} -j DROP".format(port.get())
      killer1 = "iptables -A OUTPUT -p tcp --destination-port {} -j DROP".format(port.get())
      os.system(killer0)
      os.system(killer1)
      information.configure(text="Port {} successfully closed.".format(port.get()))
       killer0 = "iptables -A INPUT -p tcp --destination-port {} -j DROP".format(port.get())
       killer1 = "iptables -A OUTPUT -p tcp --destination-port {} -j DROP".format(port.get())
       os.system(killer0)
       os.system(killer1)
       information.configure(text="Port {} successfully closed.".format(port.get()))
   except:
      information.configure(text="An error occured while closing the port.")
       information.configure(text="An error occured while closing the port.")
def restore():
   try:
       os.system("sudo iptables -F")
@@ -54,7 +61,7 @@ def restore():
def openn():
   try:
       listen_area.configure(text="Port {}/tcp opened and listening connections.".format(open_enter.get()))
       server = "nc -lvp {}".format(open_enter.get())
       server = "nc -lvp {} &".format(open_enter.get())
       os.system(server)
   except:
       listen_area.configure(text="An error occured while listening the server.")
@@ -65,7 +72,14 @@ def blocker():
       blocker_inf.configure(text="IP Address: {} successfully blocked.".format(blocker_ent.get()))
   except:
       blocker_inf.configure(text="An error occured while blocking.")

def catcher():
   try:
       interface = str(iface_ent.get())
       monitor = "./netm0n.sh {} &".format(interface)
       os.system(monitor)
   except:
       sys.exit(1)

buttons = Button(window, text="Close", command=closer)
buttons.grid(column=2, row=0)
buttons2 = Button(window, text="Restore", command=restore)
@@ -74,4 +88,8 @@ def blocker():
buttons3.grid(column=2, row=6)
buttons4 = Button(window, text="Block", command=blocker)
buttons4.grid(column=2, row=8)
butt = Button(window, text="Start", command=catcher)
butt.grid(column=1, row=12)


window.mainloop()