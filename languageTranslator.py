from tkinter import *
from googletrans import Translator
from gtts import gTTS

def transLanguage():
    input_text = entry_window.get()
    translator = Translator()
    selected_language = drpDwn.get()




    if selected_language == "Japanese":
        change = "ja"
    elif selected_language == "English":
        change = "en"
    elif selected_language == "German":
        change ="de"
    elif selected_language == "Irish":
        change = "ga"
    elif selected_language == "French":
        change = "fr"
    elif selected_language == "Spanish":
        change = "es"
    elif selected_language == "Chinese":
        change = "zh-CN"
    else:
        # Handle unsupported language
        print(f"Language {selected_language} is not supported.")
        return

    text_translate = translator.translate(input_text, dest=change).text
    n4 = gTTS(text = text_translate, slow=False, lang=change)
    two_label.config(text=text_translate)

lang_choice = [
        "Japanese", 
        "English",
        "German",
        "Irish",
        "French",
        "Spanish",
        "Chinese"
    ]


tk_window = Tk()
tk_window.geometry("600x300")
tk_window.config(bg="Teal")



entry_window = Entry(tk_window, bg="yellow", fg="black", font=("Arial", 20, "bold"))
entry_window.place(x=25, y=60)

drpDwn = StringVar()
drpDwn.set("Pick A Language")

list_lang = OptionMenu(tk_window, drpDwn, *lang_choice)
list_lang.configure(bg="green", fg="white", font=("Arial", 16, "bold"))
list_lang.place(x=350, y=60)

two_label = Label(tk_window, text="\t\t\t\t\t\t\t", bg="white", fg="red", font=("Arial", 16, "bold"))
two_label.place(x=0, y=120)

two_label = Label(tk_window, text="Translated language", bg="white", fg="red", font=("Arial", 26, "bold"))
two_label.place(x=180, y=140)

translate_b = Button(tk_window, text="Translate", bg="silver", fg="black", font=("Arial", 20, "bold"), command=transLanguage)
translate_b.place(x=220, y=220)

tk_window.mainloop()