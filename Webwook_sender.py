from tkinter import *
import requests
from urllib.request import Request, urlopen

def main():

    def starting():
        link = str(url.get("1.0", END))
        link = link.replace("\n","")

        if link.startswith('https://discord.com/api/webhooks/') == False:

            warn = Label(text="Insert a valid Discord Weebhook URL!", bg='#2e2e2e', fg="white")
            warn.pack()

            url.delete("1.0","end")

            warn.destroy()


        msg = str(txt.get("1.0", END))
        msg = msg.replace("\n","")

        data = {
            "content": msg
            }

        try:
            requests.post(link, data=data)
        except:
            pass
        
    root = Tk()

    root.geometry("500x500")

    root.resizable(0, 0)

    root.title("Webhook Message Sender")

    root.configure(bg='#2e2e2e')

    font_title = ("Calibri", 30, "normal")
    font_txt = ("Consolas", 12, "normal")
    font = ("Consolas", 12, "normal")
    font_url = ("Consolas", 9, "normal")
    
    Label(root, text="Webhook Message Sender", font=font_title, bg='#2e2e2e', fg="white").pack()

    Label(root, text="Only work for Discord", font=font_txt, fg="white",bg='#2e2e2e').pack()

    Label(root, text="Type the text do you want to Send", font=font_txt, fg="white",bg='#2e2e2e').pack(pady = 10)

    global txt
    txt = Text(root, bg='#0f0f0f', fg="white", font=font, width=100, height=10,insertbackground="white")
    txt.pack(padx = 10)

    Label(root, text="Webhook URL", fg="white",bg='#2e2e2e').pack(pady = 10)

    global url
    url = Text(root, fg="white", font=font_url,bg='#0f0f0f', width=70, height=2, insertbackground="white")
    url.pack()

    Button(root, text="Send",width=50, bg='#2e2e2e', fg="white",command=starting).pack(pady = 20)

    root.mainloop()

if __name__ == '__main__':
    main()