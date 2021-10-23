import cv2
import numpy as np

def openImg(img):
    image=cv2.imread(img)
    return image

def vertical_mirror(img):
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    for y in range(rows):
        for x in range(coluns):
            blank[y][x]=img[y][-x]

    return blank

def horizontal_mirror(img):
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    for y in range(rows):
        for x in range(coluns):
            blank[y][x]=img[-y][x]

    return blank

def vertical_and_horizontal_mirror(img):
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    blank = vertical_mirror(img)
    blank = horizontal_mirror(blank)
    return blank

def chanel_separation(img, cor=0):
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
    """function que converte uma img em grayScale"""
    rows,coluns,_ = img.shape # retorna quantas linhas, quantas colunas e o tipo mas o tipo a gente ignora
    #imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = np.zeros((img.shape[0],img.shape[1],1), dtype=np.uint8)
    for i in range(rows):
        for j in range(coluns): 
            img2[i][j][0] = int(img[i][j][0]*0.1140+img[i][j][1]*0.5870+img[i][j][2]*0.2990)
    return img2

def black_and_white(img):
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
     rows,coluns,_ = img.shape 
     blank = np.zeros([coluns,rows,3],dtype=np.uint8)
     for x in range(coluns):
         for y in range(rows):
             blank[x,y] = img[-y,x]
     return blank
 
def invert_RB(img):
    copia = img.copy()
    copia[:,:,0] = copia[:,:,2]
    copia[:,:,2] = img[:,:,0]
    
    return copia

def espelho_diagonal_principal(img): 
    rows,coluns,_ = img.shape
    blank = np.zeros([rows,coluns,3],dtype=np.uint8)
    print(rows,coluns)
    for y in range(rows):
         for x in range(coluns):
            blank[-y,-x] = img[y,x]
    return blank

def quadrant_mirror(img):
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
    #cb = chanel_separation(img,2)
    #img2 = black_and_white(img)
    #img2 = vertical_and_horizontal_mirror(img)
    #img2 = rotacao_90(img)
    #img2 = invert_RB(img)
    #img2 = espelho_diagonal_principal(img)
    img2 = quadrant_mirror(img)
    cv2.imshow("img",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
