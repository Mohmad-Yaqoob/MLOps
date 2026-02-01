class chatting:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        self.users = []
        
        
    def menu(self):
        user_input = input("""Welcome to Chatting woooo
                           1. Press 1 to signin
                           2. Press 2 to signin
                           3. Press 3 to write a pow
                           4. Press 4 to message a friend
                           5. Press any other key to exit 
                            """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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
        
        
obj = chatting()