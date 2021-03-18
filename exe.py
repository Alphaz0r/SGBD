import mysql.connector
import interface_console
import sys
sys.path.append("./controller/")
from client_controller import *

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.Menu()
        if choix=="1":
            controller_client=Client_controller(launcher.cnx)
        elif choix=="2":
            pass
        elif choix=="3":
            pass
        elif choix=="4":
            pass
        elif choix=="5":
            pass
    