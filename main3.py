
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(2)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self._label.after(200, self.process_webcam)

    def login(self):
        pass

    def register_new_user(self):
    #   pass
        self.register_new_user_window = tk.Toplevel(self.main_window)
   #     self.register_new_user_window.geometry("1200x520+370+120")

        #self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Aceitar','#008a8f', self.accept_register_new_user)
       # self.accept_button_register_new_user_window.place(x=850, y=300)

       # self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window,'Tentar novamente', 'red', self.try_again_register_new_user)
       # self.try_again_button_register_new_user_window.place(x=750, y=400)

       # self.capture_label = util.get_img_label(self.register_new_user_window)
       # self.capture_label.place(x=10, y=0, width=700, height=500)

       # self.add_img_to_label(self.capture_label)

       # self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        #self.entry_text_register_new_user.place(x=750, y=150)

       # self.text_label_register_new_user = util.get_text_label('Insira o nome:')
#
 #   def try_again_register_new_user(self):
 #       self.register_new_user_window.destroy()
 #   def add_img_to_label(self, label):
   #     imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
   #     label.imgtk = imgtk
  #      label.configure(image=imgtk)

  #      self.register_new_user_capture = self.most_recent_capture_arr.copy()

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


if __name__ == "__main__":
    app = App()
    app.start()
