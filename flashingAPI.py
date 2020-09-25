import time
import requests
import os
from pexpect import pxssh


# Get latest shifu image url from server
def get_url():
    global download_url
    try:

        print("")
        print("     ##### GET SHIFU LATEST IMAGE URL FROM SERVER #####")
        print("")
        print("")

        print("ajju =============> Getting shifu image url from server in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        # api-endpoint
        url = "https://d10fcns44yeyj9.cloudfront.net/json-file/alexa-dev-sign.json"

        # sending get request and saving the response as response object
        r = requests.get(url)

        # extracting data in json format
        json_data = r.json()

        latest_data = json_data[0]

        download_url = latest_data["download_url"]

        print("ajju =============> Download URL obtained...")
        print("")
        print("URL - " + download_url)
        print("")
        time.sleep(2)

    except Exception as e:
        print(str(e))

    return download_url

# Download shifu image from obtained url
def download_image(url):
    try:

        print("     ##### DOWNLAOD SHIFU IMAGE FROM OBTAINED URL #####")
        print("")
        print("")

        print("ajju =============> Downloading shifu image from obtained URL...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        # curl command downloads shifu image and renames it to image.img
        os.system("curl --output image.img -OL " + url)

        print("ajju =============> Download completed successfully")
        time.sleep(2)

    except Exception as e:
        print("pxssh failed on login.")
        print(str(e))


# copying image to server
def copy_file(file_name):
    try:

        print("")
        print("     ##### COPYING SHIFU LATEST IMAGE TO SHIFU #####")
        print("")
        print("")

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
        os.system("sshpass -p root scp ./"+file_name+" root@192.168.221.1:/tmp")

        print("ajju =============> Copied the shifu image to shifu terminal")
        time.sleep(2)

    except Exception as e:
        print("pxssh failed on login.")
        print(str(e))

# login to shifu terminal and run system upgrade
def run_upgrade(file_name):
    try:

        print("")
        print("     ##### SSH LOGIN TO SHIFU & START FLASHING #####")
        print("")
        print("")

        print("ajju =============> Logging into shifu terminal in...")
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
        print("")
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
        s.sendline("sysupgrade -v "+file_name)
        s.prompt()
        print("ajju =============> Flashing the hub started")

        time.sleep(2)
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(str(e))