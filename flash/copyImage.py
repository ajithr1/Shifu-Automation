import os
import time


def copy_file():
    try:

        print("ajju =============> Coping the shifu image to shifu terminal...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        # moving to folder consisting image
        os.system("cd /home/ajith/PycharmProjects/home")

        # copy downloaded shifu firmware image to shifu storage using secure copy command
        os.system("sshpass -p root scp ./TRQ44INDEDSHBB-1.1.241.img root@192.168.221.1:/tmp")

        print("ajju =============> Copied the shifu image to shifu terminal")
        time.sleep(2)

    except Exception as e:
        print("pxssh failed on login.")
        print(str(e))
