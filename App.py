import datetime
class App:
    def HelloWorldFunc(self,name):
        print("Hello "+name+" !")

    def TodaysDate(self):
        tdate=datetime.datetime.now()
        print(tdate)


print("Inital of Python app")
a1=App()
a1.HelloWorldFunc("Bushra")
a1.TodaysDate()

