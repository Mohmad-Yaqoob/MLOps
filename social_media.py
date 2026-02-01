class chatting:
    __user_id = 1
    def __init__(self):
        self.id = chatting.__user_id
        chatting.__user_id += 1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()
        # self.users = []
    
    @staticmethod
    def get_id():
        return chatting.__user_id
    
    @staticmethod
    def set_id(val):
        chatting.__user_id = val
        
        
    def get_name(self):
        return self.__name
    @staticmethod
    def set_name(self, val):
        self.__name = val

    
        
    def menu(self):
        user_input = input("""Welcome to Chatting woooo
                           1. Press 1 to signin
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit 
                            """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sending()
        else:
            exit()
    
    def signup(self):
        email = input("enter your email-> ")
        password = input("enter your password-> ")
        self.username = email
        self.password = password
        print("Success")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("Please SignUp first !")
        else:
            uname = input("enter your username or email ->")
            pwd = input("enter your password ->")
            if self.username==uname and self.password==pwd:
                print("Success !!")
                self.loggedin = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()
    
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter content-> ")
            print(f"Following content has been posted -> {txt}")
            
        else:
            print("First SignIn")
        print("\n")
        self.menu()
        
    def sending(self):
        if self.loggedin==True:
            txt = input("Enter your message-> ")
            frnd = input("Whome message to send")
            print(f"message {txt} sended to {frnd}")
        else:
            print("SignIn first! ")
        print("\n")
        self.menu()
        
        
# obj = chatting()