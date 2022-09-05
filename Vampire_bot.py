#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2,keyboard,pyautogui as pg, numpy as np,os,gc,sys
from fastai.vision.all import *
import utils
import torch
#import torch.nn as nn
#import torch.nn.functional as F
import torchvision
from torch.utils.data import Dataset, DataLoader
import random


# In[2]:


def process_cfg(cfg_file_arr):
    global directions_str_arr
    cfg_file_result=[]
    direction_count_str=['directions']
    direction_count=[]
    path=cfg_file_arr[0][1]
    path_imgs=os.path.join(path,"directions_imgs")
    if os.path.exists(path_imgs)==False:
        os.mkdir(path_imgs)
    for i in directions_str_arr:
        try:
            #direction_count_str.append(str(len(os.listdir(os.path.join(path,i)))))
            direction_count.append(len(os.listdir(os.path.join(path_imgs,i))))
        except:
            os.mkdir(os.path.join(path_imgs,i))
            #direction_count_str.append("0")
            direction_count.append(0)
    cfg_file_result.append(direction_count_str)
    
    screen_arr=[]
    for i in range(1,len(cfg_file_arr[1])):
        if i<5:
            screen_arr.append(int(cfg_file_arr[1][i]))  
    return direction_count,screen_arr,path


# In[3]:


class ArrayDataset_fake(Dataset):
    def __init__(self):
        labels=[]
        img_arr=[]
        for i in range(8):
            for j in range(5):
                img=np.array([[[0]*224]*224]*3)
                img_arr.append(img)
                #this_label=[[0,0,0,0]]
                #this_label[0][i]=1
                #this_label=[0,0,0,0]
                #this_label[i]=1
                this_label=i
                labels.append(np.array(this_label))
        img_arr=np.array(img_arr)
        labels=np.array(labels)
        self.x, self.y = img_arr, labels
        #self.c = 2 # binary label
    
    def __len__(self):
        return len(self.x)
    
    def __getitem__(self, i):
        #j=random.randint(0,len(self))
        return torch.tensor(self.x[i],device="cuda",dtype=torch.float), torch.tensor(self.y[i],device="cuda",dtype=torch.int)


# In[4]:


root_path=r"Vampire_survivors_bot\Vampire_survivors_cfg.txt"
path_adding=""
#path_adding_arr=["\\right","\\left","\\forward","\\back","\\space","\\nothing"]
directions_str_dict={"r":0,"l":1,"u":2,"d":3,"ru":4,"rd":5,"lu":6,"ld":7}
directions_str_arr=["r","l","u","d","ru","rd","lu","ld"]
direction_buttons=["right","left","up","down"]
cfg_file_arr=[]
#path_1=r"G:\DS\Vampire_survivors"
try:
    file=open(root_path)
    for it, line in enumerate(file):
        line = line.strip()
        cfg_file_arr.append(line.split())
    file.close()
except:
    print("First run grab screen script")
    cv2.waitKey(10000)
    sys.exit()
direction_count,screen_pos_arr,root_path=process_cfg(cfg_file_arr)
path_1=os.path.join(root_path,"directions_imgs")
path_2=os.path.join(root_path,"etc","screenshots")
x1,y1=screen_pos_arr[0],screen_pos_arr[1]
x2,y2=screen_pos_arr[2],screen_pos_arr[3]


# In[ ]:





# In[5]:


images_data_1=ArrayDataset_fake()
images_data_2=ArrayDataset_fake()
dls = DataLoaders.from_dsets(images_data_1,images_data_2,bs=8,device=torch.device('cuda'))


# In[6]:


learner = vision_learner(dls, resnet18,n_out=8,metrics=error_rate, loss_func=CrossEntropyLossFlat())


# In[7]:


try:
    learner = learner.load(root_path+"\\trained_model")
except:
    print("No models trained")
    cv2.waitKey(10000)
    sys.exit()


# In[13]:


a=learner.predict(images_data_1[0])[0].item()


# In[ ]:


screen_count=0
cv2.waitKey(10000)
#direction_count=[0,0,0,0,0,0] #r,l,u,d,space,nothing
pressed_keys=[]
while True:
    #this_direction=[0,0,0,0,0,0]
    screen=pg.screenshot(region=(x1,y1, x2-x1, y2-y1))
    screen=cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (224, 224))
    screen = cv2.GaussianBlur(screen, (3, 3), 1)
    screen = cv2.Canny(screen, threshold1=100, threshold2=155)
    cv2.imshow("frame",screen)
    screen = cv2.cvtColor(screen,cv2.COLOR_GRAY2BGR)
    
    keyboard.press("space")
    keyboard.release("space")
    for i in range(len(pressed_keys)):
        keyboard.release(pressed_keys[i])
    pressed_keys=[]
    
    screen=np.swapaxes(screen,0,2)
    screen=torch.tensor(screen,device="cuda",dtype=torch.float)
    predict=learner.predict([screen])[0].item()
    
    if (predict<4):
        pressed_keys=[direction_buttons[predict]]
    elif predict==4:
        pressed_keys=[direction_buttons[0],direction_buttons[2]]
    elif predict==5:
        pressed_keys=[direction_buttons[0],direction_buttons[3]]
    elif predict==6:
        pressed_keys=[direction_buttons[1],direction_buttons[2]]
    elif predict==7:
        pressed_keys=[direction_buttons[1],direction_buttons[3]]
    for i in range(len(pressed_keys)):
        keyboard.press(pressed_keys[i])
    
    if keyboard.is_pressed("escape"):
        for i in range(len(pressed_keys)):
            keyboard.release(pressed_keys[i])
        break
    
    cv2.waitKey(30)
cv2.destroyWindow('frame')
try:
    sys.exit() # this always raises SystemExit
except SystemExit:
    print("sys.exit() worked as expected")
except:
    print("Something went horribly wrong") # some other exception got raised


# In[ ]:





# In[ ]:




