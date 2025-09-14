from Core.Module.ModuleEntrance import password_verification
# from kivymd.app import MDApp
# from kivy.lang import Builder

# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_file(r'Style\GUI\Entrance\Login.kv')


def main():
    password_verification_instance = password_verification.IsPasswordVerification(password="ExamplePassword1!", confirmation="ExamplePassword1!")
    print(password_verification_instance())  # True
    
    # MyApp().run()

if __name__ == '__main__':
    main()