#!/usr/bin/env python
# coding: utf-8

# In[34]:


import cv2,keyboard,pyautogui as pg, numpy as np,os,gc,sys
import utils


# In[44]:


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


# In[40]:


def mouseClick(events, x, y, flags, params):
        global posList
        if events == cv2.EVENT_LBUTTONDOWN:
            posList.append((x, y))
        elif events == cv2.EVENT_RBUTTONDOWN:
            posList.pop(-1)

def action():
    global root_path
    #path_1=r"G:\DS\Vampire_survivors\directions_imgs"
    path_1=os.path.join(root_path,"directions_imgs")
    #path_2=r"G:\DS\Vampire_survivors\etc\screenshots"
    path_2=os.path.join(root_path,"etc","screenshots")

    path_adding=""
    #path_adding_arr=["\\right","\\left","\\forward","\\back","\\space","\\nothing"]

    cfg_file_arr=[]
    #path_1=r"G:\DS\Vampire_survivors"
    file=open(root_path)
    for it, line in enumerate(file):
        line = line.strip()
        cfg_file_arr.append(line.split())
    file.close()
    direction_count,screen_pos_arr,root_path=process_cfg(cfg_file_arr)
    x1,y1=screen_pos_arr[0],screen_pos_arr[1]
    x2,y2=screen_pos_arr[2],screen_pos_arr[3]

    cv2.waitKey(5000)
    img_np=np.array(pg.screenshot())
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    while True:
        #cv2.imwrite(os.path.join(path_1,'123231.png'), frame)
        img_np_drawn=img_np.copy()
        for i in posList:
            cv2.circle(img_np_drawn, (i), radius=3, color=(255, 0, 255), thickness=2)
        if len(posList)>1:
            cv2.rectangle(img_np_drawn, posList[0], (posList[1][0], posList[1][1]), (255, 0, 255), 2)
        cv2.waitKey(1)
        cv2.imshow("frame",img_np_drawn)
        cv2.setMouseCallback("frame", mouseClick)
        if keyboard.is_pressed("escape"):
            break
    cv2.destroyWindow('frame')
    try:
        x1,y1=posList[0]
        x2,y2=posList[1]
    except:
        print("Ошибка: Неверное количество точек")

    file=open(r"Vampire_survivors_bot\Vampire_survivors_cfg.txt","w")
    file.write("path "+root_path+"\n"+"screen ")
    for i in [x1,y1,x2,y2]:
        file.write(str(i)+" ")
    file.close()


# In[46]:


if __name__ == '__main__':
    posList=[]
    directions_str_dict={"r":0,"l":1,"u":2,"d":3,"ru":4,"rd":5,"lu":6,"ld":7}
    directions_str_arr=["r","l","u","d","ru","rd","lu","ld"]
    root_path=r"Vampire_survivors_bot\Vampire_survivors_cfg.txt"
    if (os.path.exists(root_path)):
        action()
    else:
        try:
            os.mkdir("Vampire_survivors_bot")
        except:
            pass
        file=open(root_path,"w")
        file.write("path "+os.path.join(os.path.abspath(os.getcwd()),"Vampire_survivors_bot")+"\n"+"screen ")
        for i in [0,0,1920,1080]:
            file.write(str(i)+" ")
        file.close()
    sys.exit()


# In[ ]:





# In[ ]:




