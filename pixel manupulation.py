from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Image Manupulation")
root.geometry("400x300")
root.config(background='#F6FDC3')

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg' , '*.jpg') , ('jpeg', '*.jpeg')]) # Reading file and specifying the supported formats.
    if file1 is not None:
        print(file1)
        file_name = file1.name
        key = Choice.get(1.0,END) # Getting the key value given by user 
        print(file_name, key)
        fi = open( file_name, 'rb') # Reading file as Bytes
        image= fi.read()
        fi.close()
        image = bytearray(image)
        try:
            for index , values  in enumerate(image): # Provide index to all values
                image[index] = values^int(key)  # Main logic 
            fi1 = open(file_name,'wb') # To write bytes 
            fi1.write(image)
            fi1.close()
        except ValueError:
            print("Enter a Key value to proceed")
    else:
        print("Select an image to proceed")


def decrypt_image():
    file2 = filedialog.askopenfile(mode='r', filetypes=[('jpg','*.jpg'), ('jpeg', '*.jpeg')])
    if file2 is not None:
        print(file2)
        file_name = file2.name
        key = Choice.get(1.0,END)
        print(file_name,key)
        f2 = open(file_name, 'rb')
        image = f2.read()
        f2.close()
        image = bytearray(image)
        try:
            for index, values in enumerate(image):
                image[index] = values^int(key)
            fi2 = open(file_name, 'wb')
            fi2.write(image)
            fi2.close()
        except ValueError:
            print("Enter a key Value to proceed")
    else:
        print("Select an image to proceed")

# Buttons in GUI 
B1 = Button(root, text="Encrypt" , command=encrypt_image)
B1.place(x=100,y=10)

B2 = Button(root , text="Decrypt", command=decrypt_image)
B2.place(x=200,y=10)
# TextBox parameters
Choice = Text(root , height=3 , width=30)
Choice.place(x=50,y= 50)

root.mainloop()