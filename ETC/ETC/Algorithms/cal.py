import tkinter as tk
import time

num_list=['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']
op_list = ['*', '/', '+', '-', '(', ')', 'C', 'AC']
key_list = num_list + op_list
key_list.remove('AC')
key_list.remove('C')
key_list.remove('=')


def inputKey(key):
    display.configure(state=tk.NORMAL)
    
    if key.char in key_list:
        display.insert(tk.END, key.char)
    elif key.char == '=' or key.char == '\r':
        try:
            result = str(round(eval(display.get()), 2))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            result_tmp = display.get()
            display.delete(0, tk.END)
            display.insert(0, "Can't calculate!")
            display.update()
            time.sleep(1)
            display.delete(0, tk.END)
            display.insert(0, result_tmp)
    elif key.char == 'C' or key.char == 'c':
        display.delete(0, tk.END)
    elif key.char == 'A' or key.char == 'a':
        display.delete(0, tk.END)
        clip1_entry.delete(0, tk.END)
        clip2_entry.delete(0, tk.END)
        clip3_entry.delete(0, tk.END)

    if key.keysym == "BackSpace":
        display_len = len(display.get())
        display.delete(display_len-1, tk.END)
    
    if key.keysym == 'F1':
        clip1_entry.delete(0, tk.END)
        clip1_entry.insert(tk.END, display.get())
    elif key.keysym == 'F2':
        clip2_entry.delete(0, tk.END)
        clip2_entry.insert(tk.END, display.get())
    elif key.keysym == 'F3':
        clip3_entry.delete(0, tk.END)
        clip3_entry.insert(tk.END, display.get())
    elif key.keysym == 'F4':
        display.insert(tk.END, clip1_entry.get())
        clip1_entry.delete(0, tk.END)
    elif key.keysym == 'F5':
        display.insert(tk.END, clip2_entry.get())
        clip2_entry.delete(0, tk.END)
    elif key.keysym == 'F6':
        display.insert(tk.END, clip3_entry.get())
        clip3_entry.delete(0, tk.END)

    display.configure(state="readonly")
            

def click(text):
    display.configure(state=tk.NORMAL)
    
    if text == "=":
        try:
            result = str(round(eval(display.get()), 2))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.insert(tk.END, " => ERROR")
    elif text == "C":
        display.delete(0, tk.END)
    elif text == "AC":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

    display.configure(state="readonly")

def funcClick(key):
    display.configure(state=tk.NORMAL)
    
    if key == 'F1':
        clip1_entry.delete(0, tk.END)
        clip1_entry.insert(tk.END, display.get())
    elif key == 'F2':
        clip2_entry.delete(0, tk.END)
        clip2_entry.insert(tk.END, display.get())
    elif key == 'F3':
        clip3_entry.delete(0, tk.END)
        clip3_entry.insert(tk.END, display.get())
    elif key == 'F4':
        display.insert(tk.END, clip1_entry.get())
        clip1_entry.delete(0, tk.END)
    elif key == 'F5':
        display.insert(tk.END, clip2_entry.get())
        clip2_entry.delete(0, tk.END)
    elif key == 'F6':
        display.insert(tk.END, clip3_entry.get())
        clip3_entry.delete(0, tk.END)

    display.configure(state="readonly")
    
window = tk.Tk()
window.title("Calculator")
window.attributes("-topmost", True)
window.bind("<Key>", inputKey)

display = tk.Entry(window, width=35, readonlybackground="light blue", bg="light blue")
display.grid(row=0, column=0, columnspan=2)
display.configure(state="readonly")

num_frame = tk.Frame(window)
num_frame.grid(row=1, column=0)

r = 0
c = 0
for btn_text in num_list:
    def cmd(x=btn_text):
        click(x)
    tk.Button(num_frame, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c+1
    if c>2:
        c=0
        r=r+1
        
op_frame = tk.Frame(window)
op_frame.grid(row=1, column=1)

r = 0
c = 0
for btn_text in op_list:
    def cmd(x=btn_text):
        click(x)
    tk.Button(op_frame, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c=c+1
    if c>1:
        c=0
        r=r+1

clip_frame = tk.Frame(window)
clip_frame.grid(row=2, column=0, columnspan=2, sticky='N')

def cmd_F1():
    funcClick('F1')

def cmd_F2():
    funcClick('F2')

def cmd_F3():
    funcClick('F3')

def cmd_F4():
    funcClick('F4')

def cmd_F5():
    funcClick('F5')

def cmd_F6():
    funcClick('F6')

clip1_input_btn = tk.Button(clip_frame, width=2, text="+", command=cmd_F1)
clip1_input_btn.grid(row=0, column=0)
clip1_entry = tk.Entry(clip_frame, width=20, bg="light pink")
clip1_entry.grid(row=0, column=1)
clip1_output_btn = tk.Button(clip_frame, width=2, text="-", command=cmd_F4)
clip1_output_btn.grid(row=0, column=2)

clip2_input_btn = tk.Button(clip_frame, width=2, text="+", command=cmd_F2)
clip2_input_btn.grid(row=1, column=0)
clip2_entry = tk.Entry(clip_frame, width=20, bg="light yellow")
clip2_entry.grid(row=1, column=1)
clip2_output_btn = tk.Button(clip_frame, width=2, text="-", command=cmd_F5)
clip2_output_btn.grid(row=1, column=2)

clip3_input_btn = tk.Button(clip_frame, width=2, text='+', command=cmd_F3)
clip3_input_btn.grid(row=2, column=0)
clip3_entry = tk.Entry(clip_frame, width=20, bg="light green")
clip3_entry.grid(row=2, column=1)
clip3_output_btn = tk.Button(clip_frame, width=2, text='-', command=cmd_F6)
clip3_output_btn.grid(row=2, column=2)

window.mainloop()
