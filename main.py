import os
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk
from imageprocessing.inputImage import InputImage
from imageprocessing.sourceImage import SourceImage


def openFile(window: Tk):
    file = askopenfile(mode='r',
                       filetypes=[('Image Files', '*.png'), ('Image Files', '*.jpg'), ('Image Files', '*.jpeg')])
    if file is not None:
        path = '.\\images'
        image = Image.open(file.name)
        testImage = InputImage(image)

        sourceImages = []
        files = os.listdir(path)
        for f in files:
            temp = SourceImage(Image.open(path + '\\' + f))
            sourceImages.append(temp)

        testImage.compareAverages(sourceImages)
        mosaic = testImage.makeMosaic()
        img = ImageTk.PhotoImage(mosaic)
        panel = Label(window, image=img)
        panel.image = img
        panel.pack()
        saveButton = Button(window, text='Save', command=lambda: save(mosaic))
        saveButton.pack(side=TOP, pady=10)


def save(mosaic: Image):
    files = [('Jpeg Files', '*.jpg')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    if file is not None:
        mosaic.save(file.name, "JPEG")


def main():
    window = Tk()
    window.geometry('1200x800')
    window.title("PyMosaic")
    button = Button(window, text='Choose Photo...', command=lambda: openFile(window))
    button.pack(side=TOP, pady=10)
    mainloop()


if __name__ == "__main__":
    main()
