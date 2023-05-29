def delete_duplicate(image_folder,filetype):
                # import required libraries
                import os
                import cv2
                import numpy as np
                duplicate_files= []
                dall=[]
                not_duplicate_files= []
                image_files = [_ for _ in os.listdir(image_folder) if _.endswith(filetype)]
                for file_org in image_files:
                        if file_org not in duplicate_files:
                                fo=image_folder+"//"+file_org
                                img1=cv2.imread(fo)
                                img1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                for file_check in image_files:
                                        if file_check != file_org:
                                                fc=image_folder+"//"+file_check
                                                img2=cv2.imread(fc)
                                                img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                                                #print(img1,"\n",img2)
                                                if np.array_equal(img1, img2):
                                                        duplicate_files.append(file_check)
                                                        dall.append(file_check)
                                                        dall.append(file_org)
                #print(duplicate_files)                              
                if (duplicate_files!=[]):
                        for i in duplicate_files:
                                f=image_folder+"\\"+i
                                os.remove(f)
                else:
                        pass
                return list(set(dall))


def text_extracter(image_path):
    from PIL import Image
    from pytesseract import pytesseract
    # import cv2
    path_to_tesseract = r'C:\Users\Lakshya Sharma\AppData\Local\Tesseract-OCR\tesseract.exe'
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)

    #Displaying the extracted text
    print(text[:-1])


def scanqrcode(img):
    import cv2
    import numpy as np
    import sys
    import time
    if len(sys.argv)>1:
        inputImage = cv2.imread(sys.argv[1])
    else:
        inputImage = cv2.imread(img)
    # Display barcode and QR code location
    def display(im, bbox):
        n = len(bbox)
        for j in range(n):
            cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
     
            # Display results
            cv2.imshow("Results", im)

    qrDecoder = cv2.QRCodeDetector()
     
    # Detect and decode the qrcode
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    if len(data)>0:
        return format(data)
        #display(inputImage, bbox)
        #rectifiedImage = np.uint8(rectifiedImage);
        #cv2.imshow("Rectified QRCode", rectifiedImage);
    else:
        return "QR Code not detected"
        #cv2.imshow("Results", inputImage


def compress(file_path):
        import PIL
        from PIL import Image
        from tkinter.filedialog import askopenfilename,asksaveasfilename
        img = PIL.Image.open(file_path)
        myHeight, mywidth = img.size
        #img = img.resize((160,300), PIL.Image.ANTIALIAS)
        img = img.resize((myHeight,mywidth), PIL.Image.ANTIALIAS)
        save_path = asksaveasfilename()
        try:
                img.save(save_path+"_compressed.JPG")
        except:
                img.save(save_path+"_compressed.PNG")