import time
from PIL import Image
import requests
from io import BytesIO
from selenium import webdriver
import instabot
import random
import os

def get_random_image():
    res=random.randint(32,108)
    res*=10
    print(res)
    link=f'https://source.unsplash.com/random/{res}x{res}'
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    img.save('post.jpg')
    print("Image Fatched !")
        
def get_random_caption():
    driver = webdriver.Chrome()
    driver.get("https://randomtextgenerator.com/")
    caption = driver.find_element_by_id('generatedtext')
    captions = caption.text.split('.')
    print("Caption Fatched !")
    return captions[0]+'.' 

def post(caption,username="",password=""):
    caption+="#python #bot #programming #random #code"
    bot=instabot.Bot()
    bot.login(username=username,password=password)
    bot.upload_photo('post.jpg', caption=caption)
    
if __name__ == "__main__":
    get_random_image()
    caption=get_random_caption()
    post(caption,username="insta_bot_1729",password="XXX")
