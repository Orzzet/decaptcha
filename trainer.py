__author__ = 'Dell'

from Geticons import *
from Crack import *
from Historigram import *
from tkinter import *
from tkinter.filedialog import askopenfilename


class App():

    lowerpix = 1000
    higherpix = 0
    filename = ""

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        lf_historigram = LabelFrame(frame, text='First')
        lf_historigram.pack(side = LEFT, fill='both',expand='yes')

        b_historigram = Button(lf_historigram, text="Historigram", command= lambda:self.drawhistorigram(lf_historigram))
        b_historigram.pack(side=TOP)

        lf_geticons = LabelFrame(frame, text='Second')
        lf_geticons.pack(side=LEFT, fill='both',expand='yes')

        b_geticons = Button(lf_geticons, text="Get icons", command=lambda:self.geticons(lf_geticons))
        b_geticons.pack(side=BOTTOM)

        L1 = Label(lf_geticons, text='From')
        L1.pack(side = TOP)
        self.E1 = Entry(lf_geticons, width = 4)
        self.E1.pack(side = TOP)

        L2 = Label(lf_geticons, text = 'To')
        L2.pack(side = TOP)
        self.E2 = Entry(lf_geticons, width = 4)
        self.E2.pack(side = TOP)

        self.checkhistorigram = IntVar()
        self.checkfields = IntVar()
        self.CheckVar3 = IntVar()

        self.C1 = Checkbutton(lf_geticons, text = "Select from histogram", variable = self.checkhistorigram,
                              onvalue = 1, offvalue = 0)
        self.C2 = Checkbutton(lf_geticons, text = "From _ to _ fields", variable = self.checkfields,
                              onvalue = 1, offvalue = 0)

        self.Test = Checkbutton(lf_geticons, text = "Test", variable = self.CheckVar3,
                              onvalue = 1, offvalue = 0)
        self.C1.pack()
        self.C2.pack()
        self.Test.pack()

        self.Test.select()

        self.lf_crack = LabelFrame(frame, text = 'Third')
        self.lf_crack.pack()
        b_crack = Button(self.lf_crack, text="Crack test", command=lambda: self.crack())
        b_crack.pack(side=TOP)


    def drawhistorigram(self, master):
        try:
            self.Lb1.delete(0, END)
        except:
            self.Lb1 = Listbox(master, selectmode=MULTIPLE)

        self.filename = askopenfilename()
        mostpixels = historigram(self.filename)
        for i in range(len(mostpixels)):
            self.Lb1.insert(i+1, "Pixels: " + str(mostpixels[i][1]) + ', ' + "Value: " +str(mostpixels[i][0]))
            self.Lb1.pack()


    def geticons(self, master):
        if self.checkhistorigram.get() == 1 and self.checkfields.get() == 1:
            self.C1.deselect()

        if self.checkfields.get() == 1:
            self.lowerpix = int(self.E1.get())
            self.higherpix = int(self.E2.get())
            im = geticons(self.filename, self.lowerpix,self.higherpix, self.CheckVar3.get())

            top = Toplevel()
            capout = Label(top, image = im)
            capout.image = im
            selectedpix = Label(top, text = str(self.lowerpix)+' - '+str(self.higherpix))
            capout.pack()
            selectedpix.pack(side = BOTTOM)

        if self.checkhistorigram.get() == 1:
            self.indexselected = self.Lb1.curselection()

            for i in range(len(self.indexselected)):
                pix = self.Lb1.get(self.indexselected[i]).split()
                if int(pix[0]) > self.higherpix:
                    self.higherpix = int(pix[0])
                if int(pix[0]) < self.lowerpix:
                    self.lowerpix = int(pix[0])

            im = geticons(self.filename, self.lowerpix,self.higherpix, self.CheckVar3.get())

            top = Toplevel()
            capout = Label(top, image = im)
            capout.image = im
            selectedpix = Label(top, text = str(self.lowerpix)+' - '+str(self.higherpix))
            capout.pack()
            selectedpix.pack(side = BOTTOM)

    def crack(self):
        lowerpix = int(self.E1.get())
        higherpix = int(self.E2.get())
        sol = Label(self.lf_crack, text = str(solve_image(self.filename, lowerpix, higherpix)))
        sol.pack(side = BOTTOM)


root = Tk()
root.title("Decaptcha")

app = App(root)

root.mainloop()
root.destroy()