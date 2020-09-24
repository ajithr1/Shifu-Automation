import time

from pexpect import pxssh


def run_upgrade():
    try:
        print("ajju =============> Logging into shifu terminal and flash the device will start in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        # Accessing shifu remotely
        s = pxssh.pxssh()
        hostname = "192.168.221.1"
        username = "root"
        password = "root"

        # login to shifu server
        s.login(hostname, username, password)
        s.sendline('uptime')  # run a command
        s.prompt() # match the prompt
        print("ajju =============> Logged in successfully")
        time.sleep(2)
        s.sendline('cd /tmp')
        s.prompt()
        print("ajju =============> Moved to tmp directory")
        time.sleep(1)
        # starting the flashing process
        print("ajju =============> Flashing the hub will start in ...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        s.sendline('sysupgrade -v TRQ44INDEDSHBB-1.1.241.img')
        s.prompt()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(str(e))
