import flashingAPI as flash

# Get latest shifu image url from server
url = flash.get_url()

# Download shifu image from obtained url
flash.download_image(url)

# copying image to server
flash.copy_file("TRQ44INDEDSHBB-1.1.241.img")

# login to shifu terminal and run system upgrade
flash.run_upgrade("TRQ44INDEDSHBB-1.1.241.img")