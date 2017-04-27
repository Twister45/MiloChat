from tkinter import *
from PIL import ImageTk, Image
from chatterbot import ChatBot
from settings import TWITTER
import logging


class MiloChat:

    def __init__(self, master):
        self.master = master
        self.chatbotInit()
        self.reply = StringVar()
        self.reply.set("Say something to Milo")
        self.size = (500, 500)
        master.title("Milo The Meme Chat")
        self.image = Image.open("C:\\Users\\jessie_twister\\PycharmProjects\\MemeChat\\Pic\\milo.jpg")
        self.image = self.image.resize(self.size)
        self.photo = ImageTk.PhotoImage(self.image)
        self.information()
        self.grid()

    def information(self):
        self.app_title = Label(root, text="Milo The ... Chat", font=("Times", "20"))
        self.input_chat_text = Label(root, textvariable=self.reply, font=("Times", "16"))
        self.input_chat_box = Entry(root)
        self.input_chat_box.bind('<Return>', self.response)
        self.chat_enter_button = Button(root, text=" Enter ", anchor=E)
        self.chat_enter_button.bind('<Button-1>', self.response)
        self.ImageResult = Label(root, width=500, height=500, image=self.photo)

    def grid(self):
        self.app_title.grid(row=0, columnspan=3)
        self.ImageResult.grid(row=1, column=2, padx=30)
        self.input_chat_text.grid(row=2, column=2)
        self.input_chat_box.grid(row=3, column=2, pady=(10,15))
        self.chat_enter_button.grid(row=3, column=2, sticky=E, padx=(0,150), pady=(10,15))

    def response(self, event):
        self.response = self.input_chat_box.get()
        self.input_chat_box.delete(0, END)
        self.replyMilo = self.chatbot.get_response(self.response)
        self.reply.set(self.replyMilo)

    def chatbotInit(self):
        logging.basicConfig(level=logging.INFO)

        self.chatbot = ChatBot("TwitterBot")
        self.chatbot.train()


root = Tk()
my_gui = MiloChat(root)
root.mainloop()


        #api_key = "&api_key=dc6zaTOxFJmzC"
        #search_url = ("http://api.giphy.com/v1/gifs/search?q=" + self.response + api_key)
        #self.image2 = Image.open("C:\\Users\\jessie_twister\\PycharmProjects\\MemeChat\\Pic\\Sponge.gif")
        #self.image2 = self.image2.resize(self.size)
        #self.photo = ImageTk.PhotoImage(self.image2)
        #self.ImageResult.config(image=self.photo)
        #print(search_url)
