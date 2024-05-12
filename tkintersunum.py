import tkinter as tk
from tkinter import PhotoImage
import os


def close_fullscreen(event):
    event.widget.attributes("-fullscreen", False)  # Event'in geldiği widget (pencere) üzerinde tam ekranı kapat
    event.widget.unbind("<Escape>")  # ESC tuşu olayını bağlamayı kaldır
    event.widget.destroy()  # Pencereyi kapat

class Presentation(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        

        # Pencereyi tam ekran yap
        self .attributes("-fullscreen", True)

        self.title("My Presentation")
        self.geometry(f"{screen_width}x{screen_height}")

        
        self.slides = [
            Slide1(self),
            Slide2(self),
            Slide3(self),
            Slide4(self),
            Slide5(self),
            Slide6(self),
            Slide7(self),
            Slide8(self),
            Slide9(self),
            Slide10(self),
            Slide11(self),
            Slide12(self),
            Slide13(self)
            # Add more slides here
        ]
        
        self.current_slide = 0
        self.slides[self.current_slide].pack(fill=tk.BOTH, expand=True)
        
        self.bind("<Right>", self.next_slide)
        self.bind("<Left>", self.prev_slide)
        self.bind("<Escape>", close_fullscreen)  # ESC tuşuna basıldığında close_fullscreen fonksiyonunu çağır

        
    def next_slide(self, event):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.show_slide()
        
    def prev_slide(self, event):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.show_slide()
            
    def show_slide(self):
        for i, slide in enumerate(self.slides):
            if i == self.current_slide:
                slide.pack(fill=tk.BOTH, expand=True)
            else:
                slide.pack_forget()

class Slide1(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.configure(bg="#EADBC8")  # Set background color
        
        current_directory = os.path.dirname(__file__)
        image_path = os.path.join(current_directory, "tkinterimage.png")


        image = PhotoImage(file=image_path)  # Specify your image path
        resized_image = image.subsample(4, 4)  # Resize the image by a factor of 2
        image_label = tk.Label(self, image=resized_image, bg="#EADBC8")
        image_label.image = resized_image  # Keep a reference to the resized image to prevent garbage collection
        image_label.pack(side=tk.TOP, pady=(70,10))  # Pack the image label at the bottom with padding

        header_label = tk.Label(self, text="PYTHON\nTKINTER\n KÜTÜPHANESİ", font=("Arial", 64, "bold"), bg="#C7B7A3", fg="#322C2B")
        header_label.pack(fill=tk.BOTH, pady=(100, 20), expand=True )  # Add padding between header and content
        
        content_frame = tk.Frame(self, bg="#EADBC8")  # Frame to hold content with white background
        content_frame.pack(fill=tk.BOTH, expand=True)  # Pack content frame with expand and padding
        
        content_label = tk.Label(content_frame, text="210205012-Tunahan Akdere\n210205002-Yiğithan Çetinkaya\n210205029-Görkem Melih Cin", font=("Arial", 14,"bold"), bg="#C7B7A3", fg="#322C2B")
        content_label.pack(fill=tk.BOTH, padx=10, pady=10)  # Pack content label with expand to fill frame



class Slide2(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  # Set background color to light green using RGB color values

        

        #frame = tk.Frame(self, bg="white")  # Create a frame with white background
        #frame.pack(pady=(100, 20), padx=20)  # Add padding around the frame
        
        header_label = tk.Label(self, text="TKINTER Nedir?", font=("Arial", 64, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to white
        header_label.pack(pady=(150, 50), anchor="n")  # Add padding between header and content
        
        
        content_label = tk.Label(self, text="Tkinter, Python programlama dilinin standart kütüphanelerinden biridir\n ve\n GUI (Grafiksel Kullanıcı Arayüzü) uygulamaları oluşturmak için kullanılır.", font=("Arial", 24, "bold"), bg="#C7B7A3", fg="#322C2B")  # Set text color to white
        content_label.pack(padx=20, pady=20, anchor="center")  # Add padding to content label
        content_label.config(highlightthickness=2, highlightbackground="black", padx=30, pady=30)


class Slide3(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  # Set background color to light green using RGB color values

        
        header_label = tk.Label(self, text="Nasıl Kullanmaya Başlarım?", font=("Arial", 64, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to white
        header_label.pack(pady=(150, 50), anchor="n")  # Add padding between header and content
        
        content_label_1 = tk.Label(self, text="Tkinter kütüphanesini kullanmaya başlamak için Python indirmeniz yeterlidir çünkü Tkinter Python standart kütüphanesiyle birlikte gelir.\n\nHerhangi bir metin düzenleyiciye Tkinter kütüphanesi import edildikten sonra kullanılmaya hemen başlanılabilir.", font=("Arial", 16, "bold"), bg="#C7B7A3", fg="#322C2B")  # Set text color to white
        content_label_1.pack(padx=30, pady=30, anchor="center")  # Add padding to content label
        content_label_1.config(highlightthickness=2, highlightbackground="black", padx=40, pady=40)
        

class Slide4(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  # Set background color to slate blue using HEX color code

        header_label = tk.Label(self, text="Basit Bir Kullanım Örneği", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(150, 20), anchor="n")  # Add padding between header and content and anchor to the top

        current_directory2 = os.path.dirname(__file__)
        image_path2 = os.path.join(current_directory2, "slide4.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path2)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)

class Slide5(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  # Set background color to slate blue using HEX color code

        header_label = tk.Label(self, text="TKINTER - WIDGETS\nButon", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(120, 20), anchor="n")  # Add padding between header and content and anchor to the top


        current_directory3 = os.path.dirname(__file__)
        image_path3 = os.path.join(current_directory3, "slide5.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path3)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)


class Slide6(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  # Set background color to slate blue using HEX color code

        header_label = tk.Label(self, text="TKINTER - WIDGETS\nButon", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(10, 1), anchor="n")  # Add padding between header and content and anchor to the top

        current_directory4 = os.path.dirname(__file__)
        image_path4 = os.path.join(current_directory4, "slide6.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path4)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)


class Slide7(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS\nRadioButon", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(90, 10), anchor="n")  # Add padding between header and content and anchor to the top
        
        current_directory5 = os.path.dirname(__file__)
        image_path5 = os.path.join(current_directory5, "slide7.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path5)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)
        


class Slide8(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS\nWidget Özellikleri", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(90, 10), anchor="n")  # Add padding between header and content and anchor to the top
        
        current_directory6 = os.path.dirname(__file__)
        image_path6 = os.path.join(current_directory6, "slide8.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path6)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)



class Slide9(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS\nOlaylar ve İşlevler", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(90, 10), anchor="n")  # Add padding between header and content and anchor to the top
        
        current_directory7 = os.path.dirname(__file__)
        image_path7 = os.path.join(current_directory7, "slide9.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path7)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)


class Slide10(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(50, 1), anchor="n")  # Add padding between header and content and anchor to the top
        
        content_label_2 = tk.Label(self, text="Grid Yerleşimi - Birden Fazla Pencere - Stil ve Görünüm", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to white
        content_label_2.pack(padx=10, pady=10, anchor="center")  # Add padding to content label


        current_directory8 = os.path.dirname(__file__)
        image_path8 = os.path.join(current_directory8, "slide10.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path8)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)


class Slide11(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(50, 1), anchor="n")  # Add padding between header and content and anchor to the top
        
        content_label_3 = tk.Label(self, text="Grid Yerleşimi - Birden Fazla Pencere - Stil ve Görünüm", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to white
        content_label_3.pack(padx=10, pady=10, anchor="center")  # Add padding to content label

        current_directory9 = os.path.dirname(__file__)
        image_path9 = os.path.join(current_directory9, "slide11.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path9)
        image_label = tk.Label(self, image=self.image, bg="#44546a")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)


class Slide12(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="TKINTER - WIDGETS\nResim Yerleştirme", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(150, 20), anchor="n")  # Add padding between header and content and anchor to the top
        
        current_directory10 = os.path.dirname(__file__)
        image_path10 = os.path.join(current_directory10, "slide12.png")

        # Load and store the image
        self.image = tk.PhotoImage(file=image_path10)
        image_label = tk.Label(self, image=self.image, bg="#EADBC8")  # Specify your image path
        image_label.pack(pady=20)  # Pack the image label with padding
        image_label.config(highlightthickness=2, highlightbackground="black", padx=20, pady=20)

class Slide13(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="#EADBC8")  
        
        header_label = tk.Label(self, text="Kaynakça\n", font=("Arial", 32, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to slate blue
        header_label.pack(pady=(200, 50), anchor="n")  # Add padding between header and content and anchor to the top
        
        content_label_4 = tk.Label(self, text="https://docs.python.org/3/library/tkinter.html\nhttps://www.geeksforgeeks.org/python-gui-tkinter/", font=("Arial", 24, "bold"), bg="#EADBC8", fg="#322C2B")  # Set text color to white
        content_label_4.pack(padx=10, pady=10, anchor="center")  # Add padding to content label



if __name__ == "__main__":
    app = Presentation()
    app.mainloop()

