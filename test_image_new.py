import os #this gives list of names of images 
import game_config as gc # this contains some standard info about all the image regulations

from pygame import image, transform #It helps load the image in class


class Image: #The main class / stuff 
    def __init__(self,name):
        self.name = name #this is the label
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)#required to load the image
        self.row = 0#will be needed later to fill the board
        self.col = 0#will be needed later to fill the board
        self.image = image.load(self.image_path)#initial load
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))#the finished product
        self.box = self.image.copy()#placing the image in a box
        self.box.fill((200, 200, 200))#filling the box, i.e. making sure image occupies the box

if __name__ == '__main__':
    file_list=os.listdir(gc.ASSET_DIR)
    print(file_list)
    print("##############################")
    for i in range(len(gc.ASSET_FILES)):
        temp = Image(file_list[i])
        print(temp.name,temp.image_path,temp.box,temp)
