import os
import time


def download_image():
    try:

        print("ajju =============> Downloading shifu image from server...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        # Link contains the shifu image file
        s = "http://d10fcns44yeyj9.cloudfront.net/image-file/dev-sign/image-1.1.183.img"

        # curl command downloads shifu image and renames it to image.img
        os.system("curl --output image.img -OL "+s)

        print("ajju =============> Download completed successfully")
        time.sleep(2)

    except Exception as e:
        print("pxssh failed on login.")
        print(str(e))