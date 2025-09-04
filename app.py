import tkinter as tk
from tkinter import scrolledtext
from textblob import TextBlob

# Function to correct grammar
def correct_text():
    original_text = input_text.get("1.0", tk.END)
    blob = TextBlob(original_text)
    corrected = blob.correct()
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(corrected))
    result_label.config(text="✅ Grammar and spelling corrected.")

# Set up GUI
root = tk.Tk()
root.title("Grammar and Spelling Checker (TextBlob)")
root.geometry("700x500")

tk.Label(root, text="Enter your text:", font=("Helvetica", 14)).pack(pady=10)
input_text = scrolledtext.ScrolledText(root, height=10, width=80)
input_text.pack()

tk.Button(root, text="Correct Grammar", command=correct_text).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

tk.Label(root, text="Corrected Text:", font=("Helvetica", 14)).pack(pady=5)
result_text = scrolledtext.ScrolledText(root, height=10, width=80)
result_text.pack()

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("300x100")

tk.Label(root, text="If you see this, tkinter is working!").pack()

root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from textblob import TextBlob

def correct_text():
    original_text = input_text.get("1.0", tk.END)
    blob = TextBlob(original_text)
    corrected = blob.correct()
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(corrected))
    result_label.config(text="✅ Grammar and spelling corrected.")

# Print for debug
print("Starting Grammar Checker...")

# Setup GUI
root = tk.Tk()
root.title("Grammar and Spelling Checker (TextBlob)")
root.geometry("700x500")

tk.Label(root, text="Enter your text:", font=("Helvetica", 14)).pack(pady=10)
input_text = scrolledtext.ScrolledText(root, height=10, width=80)
input_text.pack()

tk.Button(root, text="Correct Grammar", command=correct_text).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

tk.Label(root, text="Corrected Text:", font=("Helvetica", 14)).pack(pady=5)
result_text = scrolledtext.ScrolledText(root, height=10, width=80)
result_text.pack()

root.mainloop()

