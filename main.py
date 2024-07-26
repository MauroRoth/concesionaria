from controllers.controller import Controller
class Main:
    def run():
        try:
            app = Controller()
            app.menuController()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()