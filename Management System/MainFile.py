import cv2
from tkinter import *
import tkinter.filedialog
from abc import *
import os
import tkinter as tk
import GraphicalUserInterface

class Visualize:
    def __init__(self, cam_port=0):
        self.cam = cv2.VideoCapture(cam_port)
        self.root = tk.Tk()
        self.root.title("Webcam Capture")
        self.root.geometry("300x200")
        self.start_button = tk.Button(self.root, text="Start Capture", command=self.run)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop Capture", command=self.stop_capture)
        self.stop_button.pack()
        

    def take_photo(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            result, image = self.cam.read()
            if result:
                root = tk.Tk()
                root.title("Enter the name of the photo")
                label = Label(root, text="Enter the name of the photo")
                label.pack()
                entry = Entry(root)
                entry.pack()
                button = Button(root, text="Save", command=lambda: self.save_photo(entry.get(),image,root))
                button.pack()
                cv2.imshow("Take Photo",image)
                root.mainloop()

    def save_photo(self, name,image,root):
        folder_path = "/home/livan/Desktop/Proje OOP/Raw Materials"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        image_path = os.path.join(folder_path, name + ".png")
        cv2.imwrite(image_path, image)
        cv2.destroyWindow("Take Photo")
        root.destroy()
        self.stop_capture()
        self.root = tk.Tk()
        self.root.title("Webcam Capture")
        self.root.geometry("300x200")
        self.start_button = tk.Button(self.root, text="Start Capture", command=self.run)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop Capture", command=self.stop_capture)
        self.stop_button.pack()
        self.root.mainloop()


    def run(self):
        while True:
            _, frame = self.cam.read()
            cv2.imshow("Press 'Take photo' button to take a photo", frame)
            cv2.setMouseCallback("Press 'Take photo' button to take a photo", self.take_photo)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

    def stop_capture(self):
        self.cam.release()
        cv2.destroyAllWindows()
        self.root.destroy()


if __name__ == "__main__":
    app = Visualize()
    app.root.mainloop()


class RawMaterials(ABC):
    def __init__(self, name, purchase_date, supplier, expiration_date, storage_code, description):
        self.name = name
        self.purchase_date = purchase_date
        self.supplier = supplier
        self.expiration_date = expiration_date
        self.storage_code = storage_code
        self.description = description    

    @abstractmethod
    def set_name(self):
        pass
    
    @abstractmethod
    def set_purchase_date(self):
        pass
    
    @abstractmethod
    def set_supplier(self):
        pass
    
    @abstractmethod
    def set_expiration_date(self):
        pass
    
    @abstractmethod
    def set_storage_code(self):
        pass
    
    @abstractmethod
    def set_description(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_purchase_date(self):
        pass
    
    @abstractmethod
    def get_supplier(self):
        pass
    
    @abstractmethod
    def get_expiration_date(self):
        pass
    
    @abstractmethod
    def get_storage_code(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass 

class Products(RawMaterials):
    def __init__(self, name,purchase_date,supplier, production_date, customer, expiration_date, storage_code, raw_material_codes, description):
        super().__init__(name, purchase_date, supplier, expiration_date, storage_code, description)
        self.production_date = production_date
        self.customer = customer
        self.raw_material_codes = raw_material_codes
        
    def set_production_date(self, date):
        self.production_date = date
        
    def set_customer(self, customer):
        self.customer = customer
        
    def set_raw_material_codes(self, codes):
        self.raw_material_codes = codes
        
    def get_production_date(self):
        return self.production_date

    def get_customer(self):
        return self.customer
    
    def get_raw_material_codes(self):
        return self.raw_material_codes
    
    def set_name(self, name):
        self.name = name
        
    def set_purchase_date(self, date):
        self.purchase_date = date
        
    def set_supplier(self, supplier):
        self.supplier = supplier
        
    def set_expiration_date(self, date):
        self.expiration_date = date
        
    def set_storage_code(self, code):
        self.storage_code = code
        
    def set_description(self, description):
        self.description = description
    
    def get_name(self):
        return self.name
    
    def get_purchase_date(self):
        return self.purchase_date
    
    def get_supplier(self):
        return self.supplier
    
    def get_expiration_date(self):
        return self.expiration_date
    
    def get_storage_code(self):
        return self.storage_code
    
    def get_description(self):
        return self.description
    
    @classmethod
    def from_excel(cls, file):
        pass
    
    def save_to_excel(self, file):
        pass  
    
v = Visualize()
v.run()