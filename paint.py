from tkinter import * 

class Paint(PythonPaint):
    
    def __init__(self, parent): 
        PythonPaint.__init__(self, parent) 
        self.parent = parent 
        self.color = "black" 
        self.brush_size = 2 
        self.setUI()
        
    def main(): 
        root = Tk() 
        root.geometry("850x500+300+300") 
        app = Paint(root) 
        root.mainloop() 
            
    

if __name__ == '__main__': 
    main()