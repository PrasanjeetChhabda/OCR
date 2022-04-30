import os
from PIL import Image
import pytesseract as ptc


def hindiocr(): 
    #Folder Path For Giving The Input 
    get_images_path ="hindi/images/get"
   
    #Folder Path For Displaying The Output 
    output_images_path ="hindi/output/post"
  
    # iterating the images inside the folder 
    for imageName in os.listdir(get_images_path): 
        print ("Success")
              
        inputPath = os.path.join(get_images_path, imageName) 
        img = Image.open(inputPath) 
  
       
        text = ptc.image_to_string(img, lang ="hin") 
  
       
        imageName = imageName[0:-4] 
  
        outputPath = os.path.join(output_images_path, imageName+".txt") 
        print(text) 
  
         
        file1 = open(outputPath, "w", encoding='utf-8') 
        file1.write(text) 
        file1.close()  




def gujaratiocr(): 
    #Folder Path For Giving The Input 
    get_images_path ="gujarati/images/get"
   
    #Folder Path For Displaying The Output 
    output_images_path ="gujarati/output/post"
  
    # iterating the images inside the folder 
    for imageName in os.listdir(get_images_path): 
        print ("Success")
              
        inputPath = os.path.join(get_images_path, imageName) 
        img = Image.open(inputPath) 
  
        
        text = ptc.image_to_string(img, lang ="guj") 
  
        
        imageName = imageName[0:-4] 
  
        outputPath = os.path.join(output_images_path, imageName+".txt") 
        print(text) 
  
         
        file1 = open(outputPath, "w", encoding='utf-8') 
        file1.write(text) 
        file1.close()  

        os.system('cls')
        
        print("DONE!")
        print("Please check the `post` folder in hindi and gujarati directory")
        print("Note: The text would be saved in the .txt format with same name as of the image")
if __name__ == '__main__': 
    hindiocr() 
    gujaratiocr()