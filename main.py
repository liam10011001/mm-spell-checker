from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import spelling_checker as sc

root = Tk()
root.call('encoding', 'system', 'utf-8')
root.title("Myanmar Spell Checker")
root.iconbitmap("favicon_io\\favicon.ico")
root.geometry("800x400")

global err_index
global errors

err_index = -1

def warning(message):
    messagebox.showwarning("Warning", message)

def info(title, message):
    messagebox.showinfo(title, message)

def error(message):
    messagebox.showerror("Error", message)

def disableButtons(buttons):
    for btn in buttons: btn.config(state="disabled")

def enableButtons(buttons):
    for btn in buttons: btn.config(state="active")

def disableText(tbs):
    for tb in tbs: tb.config(state="disabled")

def enableText(tbs):
    for tb in tbs: tb.config(state="normal")

def showText(text):
    input_text.delete(1.0, "end")
    input_text.insert("end", text)

def openFile():
    root.filename = filedialog.askopenfilename(
        title="Select a file", 
        filetypes=(("Text Files (*.txt)", "*.txt"), ("All Files", "*.*"))
    )
    try:
        with open(root.filename, "r", encoding="utf-8") as f:
            showText(f.read())
    except:
        error("Can't open " + root.filename)

def show(error):
    enableText([err_text, possible_text])
    (word, possible_words) = error
    err_text.delete(1.0, "end")
    err_text.insert("end", word)
    possible_text.delete(1.0, "end")
    for p in possible_words:
        possible_text.insert("end", p + "\n")
    disableText([err_text, possible_text])

def showResult(words, typo, phonetic, unknown):
    global errors
    global err_index
    errors = typo + phonetic
    if errors:
        err_index = 0
        if len(errors) > 1:
            enableButtons([btn_next])
        enableButtons([btn_detail])
        show(errors[err_index])        

def showPrevious():
    global err_index
    global errors
    if err_index > 0:
        err_index -= 1
        show(errors[err_index])
        enableButtons([btn_next])
    if err_index <= 0:
        disableButtons([btn_pre])

def showNext():
    global err_index
    global errors
    if err_index < len(errors)-1:
        err_index += 1
        show(errors[err_index])
        enableButtons([btn_pre])
    if err_index >= len(errors)-1:
        disableButtons([btn_next])

def checkSpelling():
    global result
    root.config(cursor="circle")
    text = input_text.get(1.0, "end-1c")
    if not text:
        warning("No input text")
    else:
        try:
            (words, typo, phonetic, unknown) = sc.check(text)
            result = (words, typo, phonetic, unknown)
            total_err = len(typo) + len(phonetic)
            msg = ''
            if total_err:
                msg += " ".join([str(total_err), "spelling error(s) detected", "\n"])
            if unknown:
                msg += " ".join([str(len(unknown)), "unverifiabl word(s) detected"])
            if msg:
                info("Result", msg)
                showResult(words, typo, phonetic, unknown)
            else:
                info("Result", "No misspelled word found")
        except Exception as exc:
            error(exc)
        finally:
            root.config(cursor="arrow")

def showDetails():
    new_window = Toplevel(root)
    new_window.title("Myanmar Spell Checker")
    new_window.iconbitmap("favicon_io\\favicon.ico")
    new_window.geometry("800x400")


def clearAll():
    enableText([err_text, possible_text])
    input_text.delete(1.0, "end")
    err_text.delete(1.0, "end")
    possible_text.delete(1.0, "end")
    disableButtons([btn_detail, btn_pre, btn_next])
    disableText([err_text, possible_text])
    err_index = -1
    
# body
input_field = Frame(root, padx=10, pady=10, highlightbackground="grey", highlightthickness=1)
input_field.place(x=0, y=0, width=500, height=400)

output_field = LabelFrame(root, padx=10, pady=10, highlightbackground="grey", highlightthickness=1)
output_field.place(x=500, y=0, width=300, height=400)

# input area 
global input_text
input_text = Text(input_field)
input_text.place(x=10, y=10, width=400, height=360)

btn_upload = Button(input_field, text="Open", command=openFile)
btn_clear = Button(input_field, text="Clear", command=clearAll)
btn_check = Button(input_field, text="Check", command=checkSpelling)

btn_upload.place(x=425, y=10, width=50, height=25)
btn_clear.place(x=425, y=55, width=50, height=25)
btn_check.place(x=425, y=100, width=50, height=25)

# output area
global btn_pre
global btn_next
global err_text
global possible_text
global btn_detail

err_text = Text(output_field, state="disabled")
btn_pre = Button(output_field, text="<<", command=showPrevious,state="disabled")
btn_next = Button(output_field, text=">>", command=showNext, state="disabled")
btn_detail = Button(output_field, text="More details", command=showDetails, state="disabled")
possible_text = Text(output_field, state="disabled")

err_text.place(x=10, y=10, width=100, height=30)
#btn_detail.place(x=180, y=10, width=80, height=30)
btn_pre.place(x=10, y=45, width=25, height=25)
btn_next.place(x=50, y=45, width=25, height=25)
possible_text.place(x=10, y=75, width=260, height=290)

root.mainloop()
