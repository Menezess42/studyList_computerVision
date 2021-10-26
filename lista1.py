import cv2
import numpy as np

def openImg(img):
    """[a simple function to open a image file]
    """
    image=cv2.imread(img)
    return image

def vertical_mirror(img):
    """[this function takes an image and vertical mirror it]
    """
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    for y in range(rows):
        for x in range(coluns):
            blank[y][x]=img[y][-x]

    return blank

def horizontal_mirror(img):
    """[this function takes an image and hroizontal mirror it]
    """
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    for y in range(rows):
        for x in range(coluns):
            blank[y][x]=img[-y][x]

    return blank

def vertical_and_horizontal_mirror(img):
    """[this function takes an image and mirrors it vertically and horizontally]
    """
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    blank = vertical_mirror(img)
    blank = horizontal_mirror(blank)
    return blank

def chanel_separation(img, cor=0):
    """[this function take an image and separate the chosen color chanel]
    
    Args:
        img (matrix): [its a image file]
        cor (int): [is the selected color channel cam be 0,1,2]
   """
    if cor==0:
        cb = img
        cb[:,:,1] = 0
        cb[:,:,2] = 0
        return cb
    elif cor==1:
        cg = img
        cg[:,:,0] = 0
        cg[:,:,2] = 0
        return cg
    elif cor==2:
        cr = img
        cr[:,:,0] = 0
        cr[:,:,1] = 0
        return cr

def luminancia(img):
    """[a simple function that converts a given image into a luminance image]
    """
    rows,coluns,_ = img.shape 
    img2 = np.zeros((img.shape[0],img.shape[1],1), dtype=np.uint8)
    for i in range(rows):
        for j in range(coluns): 
            img2[i][j][0] = int(img[i][j][0]*0.1140+img[i][j][1]*0.5870+img[i][j][2]*0.2990)
    return img2

def black_and_white(img):
    """[a simple function that converts a given image into a black_and_white image]
   """
    img2 = luminancia(img)
    rows, coluns,_ = img2.shape
    for i in range(rows):
        for j in range(coluns): 
            if img2[i][j][0] >= 127:
                img2[i][j][0] = 255
            else:
                img2[i][j][0] = 0               
    return img2

def rotacao_90(img):
    """[rotate a image in 90 degrees]
   """
    rows,coluns,_ = img.shape 
    blank = np.zeros([coluns,rows,3],dtype=np.uint8)
    for x in range(coluns):
        for y in range(rows):
            blank[x,y] = img[-y,x]
    return blank
 
def invert_RB(img):
    """[invert the R channel with the B chanel]
   """
    copia = img.copy()
    copia[:,:,0] = copia[:,:,2]
    copia[:,:,2] = img[:,:,0]
    
    return copia

def espelho_diagonal_principal(img):
    """[invert the image in the diagonal principal]
   """
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    print(rows,coluns)
    for y in range(rows):
         for x in range(coluns):
            blank[-y,-x] = img[y,x]
    return blank

def quadrant_mirror(img):
    """[invert the quadrants in diagonal, the first quadrant turns into the fourth, 
    the second into the third, the third into the second and the fourth into the first]
    """
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    ty = rows+1
    tx = coluns+1
    for y in range(int(rows/2)):
        for x in range(int(coluns/2)):
            blank[y][x] = img[y+int(ty/2)][x+int(tx/2)]
            blank[y+int(ty/2)][x+int(tx/2)] = img[y][x]
            blank[y][int(x+int(tx/2))]=img[int(y+int(ty/2))][x]
            blank[int(y+int(ty/2))][x]=img[y][int(x+int(tx/2))]
            
    return blank  

if __name__ == "__main__":
    img = openImg("imgs/wifi.jpg")
    img2 = quadrant_mirror(img)
    cv2.imshow("img",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
