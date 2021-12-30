import tkinter as tk

# 선택:0, 점:1, 선:2, 사각형:3, 원:4, 텍스트:5
draw_mode = 0
draw_color = "black"

x1 = None
y1 = None

obj_array = []

class Object:
    def __init__(self, color, width):
        self.color = color
        self.width = width

    def thicker(self):
        self.width = self.width+1
        if self.width > 10:
            self.width = 10

    def thiner(self):
        self.width = self.width-1
        if self.width < 1:
            self.width = 1    

class Point(Object):
    def __init__(self, x, y, color, width=2):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, canvas):
        canvas.create_oval(self.x-self.width, self.y-self.width,
                           self.x+self.width, self.y+self.width,
                           fill=self.color, outline=self.color)


class Text(Object):
    def __init__(self, x, y, color, text, width=2):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.width = width

    def draw(self, canvas):
        canvas.create_text(self.x, self.y,
                           fill=self.color, text=self.text, font=("Courier", self.width))

    def thicker(self):
        self.width = self.width+5
        if self.width > 50:
            self.width = 50

    def thiner(self):
        self.width = self.width-5
        if self.width < 1:
            self.width = 5  

class Line(Object):
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
                           fill=self.color, width=self.width)

class Rectangle(Object):
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline=self.color, width=self.width)

class Circle(Object):
    def __init__(self, x1, y1, x2, y2, color, width=2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                           outline=self.color, width=self.width)
        
def mouseLDown(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Down")

    if draw_mode == 1:
        point = Point(event.x, event.y, draw_color)
        obj_array.append(point)
        list_box.insert(tk.END, "point")
    elif draw_mode == 5:
        text = Text(event.x, event.y, draw_color, input_text.get())
        obj_array.append(text)
        list_box.insert(tk.END, "text")
        
    elif draw_mode >= 2 and draw_mode <= 4:
        x1 = event.x
        y1 = event.y

    render()

def mouseMove(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" Move")

    render()

def mouseLUp(event):
    global x1, y1
    mouse_text.set("X:"+str(event.x)+" Y:"+str(event.y)+" L Up")

    if draw_mode == 2:
        line = Line(x1, y1, event.x, event.y, draw_color)
        obj_array.append(line)
        list_box.insert(tk.END, "line")
    elif draw_mode == 3:
        rec = Rectangle(x1, y1, event.x, event.y, draw_color)
        obj_array.append(rec)
        list_box.insert(tk.END, "rectangle")

    elif draw_mode == 4:
        circle = Circle(x1, y1, event.x, event.y, draw_color)
        obj_array.append(circle)
        list_box.insert(tk.END, "circle")

    render()

def render():
    canvas.create_rectangle(0, 0, 400, 300, fill="white")

    for i in range(len(obj_array)):
        obj_array[i].draw(canvas)
        

def selectButton():
    global draw_mode
    draw_mode = 0

def pointButton():
    global draw_mode
    draw_mode = 1

def lineButton():
    global draw_mode
    draw_mode = 2

def rectangleButton():
    global draw_mode
    draw_mode = 3

def circleButton():
    global draw_mode
    draw_mode = 4

def textButton():
    global draw_mode
    draw_mode = 5

def whiteButton():
    global draw_color
    draw_color = "white"

def blackButton():
    global draw_color
    draw_color = "black"

def redButton():
    global draw_color
    draw_color = "red"

def yellowButton():
    global draw_color
    draw_color = "yellow"

def blueButton():
    global draw_color
    draw_color = "blue"

def greenButton():
    global draw_color
    draw_color = "green"

def widthPlusButton():
    cs = list_box.curselection()
    cur_index = cs[0]
    obj_array[cur_index].thicker()
    render()

def widthMinusButton():
    cs = list_box.curselection()
    cur_index = cs[0]
    obj_array[cur_index].thiner()
    render()

def delButton():
    if len(obj_array) > 0:
        cs = list_box.curselection()
        cur_index=cs[0]
        obj_array.pop(cur_index)
        list_box.delete(cur_index)
        render()

window = tk.Tk()
window.title("painter")

style_frame = tk.Frame(window)
style_frame.grid(row=0, column=0, sticky=tk.W)

select_button = tk.Button(style_frame, text="↖", width=3, command=selectButton)
select_button.grid(row=0, column=0, sticky=tk.W)

point_button = tk.Button(style_frame, text=".", width=3, command=pointButton)
point_button.grid(row=0, column=1, sticky=tk.W)
line_button = tk.Button(style_frame, text="/", width=3, command=lineButton)
line_button.grid(row=0, column=2, sticky=tk.W)

rectangle_button = tk.Button(style_frame, text="□", width=3, command=rectangleButton)
rectangle_button.grid(row=0, column=3, sticky=tk.W)
circle_button = tk.Button(style_frame, text="○", width=3, command=circleButton)
circle_button.grid(row=0, column=4, sticky=tk.W)

text_button = tk.Button(style_frame, text="T", width=3, command=textButton)
text_button.grid(row=0, column=5, sticky=tk.W)

color_frame = tk.Frame(window)
color_frame.grid(row=0, column=1, sticky=tk.E)

white_button = tk.Button(color_frame, highlightbackground="white", width=3, command=whiteButton)
white_button.grid(row=0, column=0, sticky=tk.E)
black_button = tk.Button(color_frame, highlightbackground="black", width=3, command=blackButton)
black_button.grid(row=0, column=1, sticky=tk.E)
red_button = tk.Button(color_frame, highlightbackground="red", width=3, command=redButton)
red_button.grid(row=0, column=2, sticky=tk.E)
blue_button = tk.Button(color_frame, highlightbackground="blue", width=3, command=blueButton)
blue_button.grid(row=0, column=3, sticky=tk.E)
yellow_button = tk.Button(color_frame, highlightbackground="yellow", width=3, command=yellowButton)
yellow_button.grid(row=0, column=4, sticky=tk.E)
green_button = tk.Button(color_frame, highlightbackground="green", width=3, command=greenButton)
green_button.grid(row=0, column=5, sticky=tk.E)

info_frame = tk.Frame(window)
info_frame.grid(row=1, column=0, columnspan=2)

mouse_text = tk.StringVar()
mouse_entry = tk.Entry(info_frame, textvariable=mouse_text, width=25)
mouse_entry.grid(row=0, column=0)

input_label = tk.Label(info_frame, text="              Text Input:")
input_label.grid(row=0, column=1)

input_text = tk.StringVar()
input_entry = tk.Entry(info_frame, textvariable=input_text, width=15)
input_entry.grid(row=0, column=2)

canvas_frame = tk.Frame(window, bd=2, highlightbackground="black")
canvas_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W)

canvas = tk.Canvas(canvas_frame, width=500, height=300, highlightbackground="white")
canvas.pack()

canvas.bind("<Button-1>", mouseLDown)
canvas.bind("<Motion>", mouseMove)
canvas.bind("<ButtonRelease-1>", mouseLUp)

list_frame = tk.Frame(window)
list_frame.grid(row=0, rowspan=3, column=2)

list_box = tk.Listbox(list_frame, width=20, height=20)
list_box.grid(row=0, column=0, columnspan=3)

width_plus_button = tk.Button(list_frame, text="+", width=4, command=widthPlusButton)
width_plus_button.grid(row=1, column=0)

width_minus_button = tk.Button(list_frame, text="-", width=4, command=widthMinusButton)
width_minus_button.grid(row=1, column=1)

del_button = tk.Button(list_frame, text="Del", width=4, command=delButton)
del_button.grid(row=1, column=2)

window.mainloop()
