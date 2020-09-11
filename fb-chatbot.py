from fbchat import Client
from fbchat.models import *
import os 
import shutil
import random
import config

img_files = []
img = ""
meme_dir = config.meme_dir
own_ID = 1234567890

# comment in following code to get specific user info to add to user_dict
#---------------------------
# user = client.searchForUsers("J Doe")[0]
# print("user ID: {}".format(user.uid))
# print("user's name: {}".format(user.name))
# print("user's photo: {}".format(user.photo))
# print("Is user client's friend: {}".format(user.is_friend))
#---------------------------

# add as many users as you like here
user_dict = {
    # 'Jane Doe': 100006234566789,
    # 'Jim Doe': 100000022333344,
}


client = Client(config.user, config.password)
print("Own id: {}".format(client.uid))

# client.send(Message (text="Hi me again!"), thread_id=client.uid, thread_type=ThreadType.USER)


files = os.listdir(meme_dir)
for f in files:
    ext = f.split(".")[-1]
    if ext == "jpg" or ext == "png" or ext == "gif" or ext == "webp":
        img_files.append(f)

print(img_files)
meme = img_files[0]

# for user in user_dict: 
for entry in user_dict.values():
    client.sendLocalImage(
        meme_dir + meme,  
        message=Message(text='Meme-bot:'),
        thread_id=entry,
        thread_type=ThreadType.USER,
    )    

shutil.move(meme_dir+meme, meme_dir+'old-memes/'+meme)

client.logout()
