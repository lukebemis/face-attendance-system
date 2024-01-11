import os.path
import datetime
import pickle

import subprocess

import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import face_recognition

import util
import os
from test import test


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1000x490+350+100")
        self.main_window.title("Ponto DPU")
        self.main_window.configure(bg='#1d1d20')

        self.login_button_main_window = util.get_button(self.main_window, 'Registrar Ponto', '#008a8f', self.login)
        self.login_button_main_window.place(x=660, y=8)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Novo Estagiário', '#254713',
                                                                    self.register_new_user)
        self.register_new_user_button_main_window.place(x=660, y=264)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=8, width=640, height=470)

        self.add_webcam(self.webcam_label)

        #self.capture_label = util.get_img_label(self.main_window)
        #self.capture_label.place(x=10, y=0, width=700, height=500)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        label = test(
                image=self.most_recent_capture_arr,
                model_dir='\Silent-Face-Anti-Spoofing\resources\anti_spoof_models',
                device_id=0
                )
        if label == 1:
        #unknown_img_path = './.tmp.jpg'

        #cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)

        #output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))
        #name = output.split(',')[1][:-5]
            name = util.recognize(self.most_recent_capture_arr, self.db_dir)

            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Não reconhecido', 'Tente Novamente')
            else:
                util.msg_box('Ponto registrado', 'Qualquer coisa {}.'.format(name))
                with open(self.log_path, 'a', ) as f:
                    f.write('{},{},{}\n'.format(name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), '________________'))
                    f.close()
        else:
        #print(name)
            util.msg_box('Erro','Usuário não reconhecido')

        os.remove(unknown_img_path)

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1000x490+350+100")
        self.register_new_user_window.title("Cadastro de novo estagiário")
        self.register_new_user_window.configure(bg='#1d1d20')

        self.accept_button_register_new_user_window = util.get_buttontwo(self.register_new_user_window, 'Aceitar','#008a8f', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=660, y=170)

        self.try_again_button_register_new_user_window = util.get_buttontwo(self.register_new_user_window,'Tentar novamente', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=660, y=327)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=8, width=640, height=470)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=660, y=50)
        self.entry_text_register_new_user.configure(bg='#1d1d20', fg='white')

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,'Insira o nome:', )
        self.text_label_register_new_user.place(x=720, y=8)
        self.text_label_register_new_user.configure(bg='#1d1d20', fg='white')
        self.entry_text_register_new_user.configure(bg='#1d1d20', fg='white')

#
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

####################

    #  self.register_new_user_button_main_window = util.get_button((self.main_window, 'Cadastrar novo estagiário', 'gray',
    #                                                                 self.register_new_user, fg='black')
    #
    #      self.register_new_user_button_main_window.place(x=750, y=400)
    #

    #   self.add_webcam(self.webcam_label)
    #
    #  self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Aceitar', '#008a8f', self.accept_register_new_user)
    #  self.accept_button_register_new_user_window.place(x=850, y=400)

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c") #n sei explicar isso

        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)), self.register_new_user_capture)

        util.msg_box('Registrado com sucesso','Estagiário registrado')

        self.entry_text_register_new_user.configure(bg='#1d1d20', fg='white')
        self.register_new_user_window.destroy()



if __name__ == "__main__":
    app = App()
    app.start()
