import time
from PIL import Image
import requests
from io import BytesIO
from selenium import webdriver

def get_random_image():
    response = requests.get('https://source.unsplash.com/random')
    img = Image.open(BytesIO(response.content))
    img.save('post.jpg')
    print("Image Fatched !")

def get_random_caption():
    driver=webdriver.Chrome()
    driver.get("https://sassycaptions.com/generator/")
    button=driver.find_element_by_id('gen')
    button.click()
    caption=driver.find_element_by_id('content')
    print("Caption Fatched !")
    return caption.text
    
def post(caption,username="",password=""):
    pass
    
if __name__ == "__main__":
    get_random_image()
    caption=get_random_caption()
    post(caption,user="insta_bot_1729",passw="********")