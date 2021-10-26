import cv2
import random
import numpy as np


def create_color():
    """[create a random color]

    Returns:
        lista[vector]: [a vector contain hte values of BGR]
    """
    b = random.randint(0,256)
    g = random.randint(0,256)
    r = random.randint(0,256)
    if r==g and r==b:
        while(r==g and r==b):
            g = random.randint(0,256)
    lista = []
    lista.append(b)
    lista.append(g)
    lista.append(r)
    return lista


def mark_object(key: int, img, y: int, x: int, pixel):
    """[function to colorize black objects inside the image using knn k being 4 or 8]

    Args:
        key (int): [can receive two values, 4 or 8, this value define de K of knn, K-nearest neighbors]
        img ([matrix]): [pass a image to colorize the black object inside]
        y (int): [y is the coordinate in the Y-axis of the pixel identify as black]
        x (int): [x is the coordinate in the X-axis of the pixel identify as black]
        pixel ([matrix]): [pixel is list of lists that contain the coordinates of the black pixels in the image,
                           the pixel variable act like a pile]

    Returns:
        img ([matrix]): [returns the modified image]
        vector ([vector]): [returns a vector, if the key is 8 returns a vector containing the coordinates y:x for the first black pixel
                            of the object in the image and the coordinates x:y for the last black pixel of the object. however, if the key
                            is 4 then returns an empty vector]
    """
    b,g,r = create_color()
    count_pixel = 0
    if key == 4:  
        while pixel != []:
            y_aux, x_aux = pixel.pop(0)
            count_pixel+=1
            img[y_aux][x_aux][0]=r
            img[y_aux][x_aux][1]=g
            img[y_aux][x_aux][2]=b
            if img[y_aux-1][x_aux][0] == 0 and img[y_aux-1][x_aux][1] == 0 and img[y_aux-1][x_aux][2]==0:
                if [y_aux-1, x_aux] not in pixel:
                 pixel.append([y_aux-1, x_aux])
                
            if img[y_aux][x_aux-1][0] == 0 and img[y_aux][x_aux-1][1] == 0 and img[y_aux][x_aux-1][2] == 0:
                if [y_aux,x_aux-1] not in pixel:
                    pixel.append([y_aux, x_aux-1])
                
            if img[y_aux][x_aux+1][0] == 0 and img[y_aux][x_aux+1][1] == 0 and img[y_aux][x_aux+1][2] == 0:
                if [y_aux,x_aux+1] not in pixel:
                 pixel.append([y_aux, x_aux+1])
                
            if img[y_aux+1][x_aux][0] == 0 and  img[y_aux+1][x_aux][1] == 0 and img[y_aux+1][x_aux][2] == 0:
                if [y_aux+1,x_aux] not in pixel:
                    pixel.append([y_aux+1,x_aux])
        cv2.rectangle(img,pt1=(x,y),pt2=(x_aux,y_aux),color=(0,0,255), thickness=1)
   
    if key == 8:
        while pixel != []:
                y_aux, x_aux = pixel.pop(0)
                #print(f"y:{y_aux} x:{x_aux}")
                count_pixel+=1
                img[y_aux][x_aux][0]=r
                img[y_aux][x_aux][1]=g
                img[y_aux][x_aux][2]=b
                if img[y_aux-1][x_aux-1][0] == 0 and img[y_aux-1][x_aux-1][1] == 0 and img[y_aux-1][x_aux-1][2]==0:
                    if [y_aux-1, x_aux-1] not in pixel:
                        pixel.append([y_aux-1, x_aux-1])
                 
                if img[y_aux-1][x_aux][0] == 0 and img[y_aux-1][x_aux][1] == 0 and img[y_aux-1][x_aux][2]==0:
                    if [y_aux-1, x_aux] not in pixel:
                        pixel.append([y_aux-1, x_aux])
                
                if img[y_aux-1][x_aux+1][0] == 0 and img[y_aux-1][x_aux+1][1] == 0 and img[y_aux-1][x_aux+1][2]==0:
                    if [y_aux-1, x_aux+1] not in pixel:
                        pixel.append([y_aux-1, x_aux+1])
                    
                if img[y_aux][x_aux-1][0] == 0 and img[y_aux][x_aux-1][1] == 0 and img[y_aux][x_aux-1][2] == 0:
                    if [y_aux,x_aux-1] not in pixel:
                        pixel.append([y_aux, x_aux-1])
                    
                if img[y_aux][x_aux+1][0] == 0 and img[y_aux][x_aux+1][1] == 0 and img[y_aux][x_aux+1][2] == 0:
                    if [y_aux,x_aux+1] not in pixel:
                        pixel.append([y_aux, x_aux+1])
                
                if img[y_aux+1][x_aux-1][0] == 0 and img[y_aux+1][x_aux-1][1] == 0 and img[y_aux+1][x_aux-1][2] == 0:
                    if [y_aux+1,x_aux-1] not in pixel:
                        pixel.append([y_aux+1, x_aux-1])
                
                if img[y_aux+1][x_aux+1][0] == 0 and img[y_aux+1][x_aux+1][1] == 0 and img[y_aux+1][x_aux+1][2] == 0:
                    if [y_aux+1,x_aux+1] not in pixel:
                        pixel.append([y_aux+1, x_aux+1])
                     
                if img[y_aux+1][x_aux][0] == 0 and  img[y_aux+1][x_aux][1] == 0 and img[y_aux+1][x_aux][2] == 0:
                    if [y_aux+1,x_aux] not in pixel:
                        pixel.append([y_aux+1,x_aux]) 
        vetor = []
        vetor.append(y) 
        vetor.append(x) 
        vetor.append(y_aux) 
        vetor.append(x_aux) 
                
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,text=str(f"Massa:{count_pixel}"), org=(x+8,y+30),fontFace=font,fontScale=0.5,color=(255,254,53),thickness=1,lineType=cv2.LINE_AA)
    if key == 8:
        return (img,vetor)
    else:
        return (img,[])
               
def reduce_by_half(img):
    """[this function take an given image and reduce it by half]

    Args:
        img ([matrix]): [an image file]

    Returns:
       img ([matrix]): [returns a half-scale image]
    """
    rows,coluns,shape = img.shape
    rows2 = int(rows/2)
    coluns2 = int(coluns/2)
    img2 = np.zeros((rows2,coluns2,shape), dtype=np.uint8)
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    while y < rows:
        x=0
        x2=0   
        while x < coluns:
            soma = [0,0,0]
            soma = soma + img[y][x]
            soma = soma + img[y][x+1]
            soma = soma + img[y+1][x]
            soma = soma + img[y+1][x+1]
            soma = soma//4
            img2[y2][x2] = soma
            x+=2
            x2+=1
        y+=2
        y2+=1
    
    return img2

def conected(img,key):
    """[this function takes an image and identifies,colorizes,selected,and tells the mass of pixels of the black objects]

    Args:
        img ([matrix]): [a given image file]
        key ([int]): [can assume the 4 and 8 values, the key is the K of the Knn]

    Returns:
        img [matrix]: [returns a modified image]
    """
    rows, coluns,shape = img.shape
    qtdPixel = []
    pixel = []
    for y in range(rows):
        for x in range(coluns):
            if img[y][x][0] ==0 and  img[y][x][1]==0 and  img[y][x][2] == 0:
                pixel.append([y,x])
                img,vetor = mark_object(key,img,y,x,pixel)
                print("saiu")
                qtdPixel.append(vetor)
    if key==8:
        if qtdPixel != []:
            var = "imgSegmentada8.png"
            while qtdPixel != []:
                vetor = qtdPixel.pop(0)
                print(vetor)
                cv2.rectangle(img,pt1=(vetor[1],vetor[0]),pt2=(vetor[3],vetor[2]),color=(0,0,255), thickness=1)    
    else:
        var = "imgSegmentada4.png"        
    print(qtdPixel)
                
    return (img,var)

def gray_scale_reduction(img, percent, channel = False):
    """[this function reduces the grayscale of the image,for example, if you pass percent as 0.5 and the R channel has a value
        of 255(white) it will reduce by half, so the new value of the channel will be 127.
        the third parameter of this function is optional, if you don't pass it will assume that the grayscale reduction must be
        applied to the tree color channels]

    Args:
        img (matrix): an given image file
        percent (flot): can receive values between 0 and 1, is the percent of reduction aply to the colors channel
        channel (bool,list, optional): [channel is a variable that is false by default, if false implies that the grayscale reduction
                                        must be applied to the three color channels, else you pass a list containing the index of the
                                        color channel you want to apply the reduction]. Defaults to False.

    Returns:
        img[image file]: [returns a modified image]
    """
    rows,coluns,_ = img.shape
    percent=1-percent
    for y in range(rows):
        for x in range(coluns):
            if channel == False:
                img[y][x] = img[y][x] * percent
            else:
                for i in channel:
                    img[y][x][i] = img[y][x][i] * percent
    return img

def openImg(arqImg):
    """function to open a image"""
    img = cv2.imread(arqImg)
    return img

def luminancia(img):
    """function to convert a colorful image to a gray iamge"""
    rows,coluns,_ = img.shape 
    img2 = np.zeros((img.shape[0],img.shape[1],1), dtype=np.uint8)
    for i in range(rows):
        for j in range(coluns): 
            img2[i][j][0] = int(img[i][j][0]*0.1140+img[i][j][1]*0.5870+img[i][j][2]*0.2990)
    return img2

def blackandWhite(img):
    """function to convert a gray image to a black and white image"""
    rows, coluns,_ = img.shape
    for i in range(rows):
        for j in range(coluns): 
            if img[i][j][0] >= 127:
                img[i][j][0] = 255
            else:
                img[i][j][0] = 0               
    return img

def main():
    pass

if __name__ == "__main__":
    main()


