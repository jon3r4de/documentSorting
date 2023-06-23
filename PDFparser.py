import tkinter
from transformers import MarianMTModel, MarianTokenizer, BartTokenizer, BartForConditionalGeneration
import PyPDF2
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
from pypdf import PdfReader
import dateparser

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def PDF_renamer(input_file):
    tokenizer = AutoTokenizer.from_pretrained("nsi319/legal-pegasus")  
    model = AutoModelForSeq2SeqLM.from_pretrained("nsi319/legal-pegasus")


    filename = input_file

    # current_directory = os.getcwd()
    # pdf_path = os.path.join(current_directory, filename)

    date_pattern = r'(\d{1,2})/(\d{1,2})/(\d{2,4})'

    # opened_file = None

    with open(filename, 'rb') as file:
        # opened_file = file
        reader = PdfReader(file)
        page = reader.pages[0]
        extracted_text = ''

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            extracted_text += page.extract_text()
        dates = dateparser.parse('(collectively referred to as the "Parties"). Effective Date: 19/2/2023')
        other_dates = re.findall(date_pattern, extracted_text)

    print(extracted_text)

    input_tokenized = tokenizer.encode(extracted_text, return_tensors='pt',max_length=1024,truncation=True)
    summary_ids = model.generate(input_tokenized,
                                    num_beams=9,
                                    no_repeat_ngram_size=3,
                                    length_penalty=2.0,
                                    min_length=5,
                                    max_length=15,
                                    early_stopping=True)

    summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
    earliest_date = None
    if dates:
        earliest_date = min(dates)
        formatted_date = earliest_date.strftime('%Y%m%d')

    elif other_dates:
        earliest_date = min(other_dates)
        day, month, year = earliest_date
        formatted_date = f"{year}{month.zfill(2)}{day.zfill(2)}"

    new_file_path = os.path.join(os.path.dirname(filename), f"{formatted_date} {summary}")
    os.rename(os.path.basename(filename), new_file_path)


def rename_file():
    file = filedialog.askopenfilename(title="Select File")

    if not file:
        messagebox.showerror("Error", "No file selected.")
        return

    # output_path = filedialog.asksaveasfilename(title="Save Output File", defaultextension=".pdf")

    # if not output_path:
    #     messagebox.showerror("Error", "No output file selected.")
    #     return

    PDF_renamer(file)
    messagebox.showinfo("Success", "File renamed successfully.")


def main():
    root = tk.Tk()
    root.title("PDF Renamer")
    
        # Calculate the window position to center it on the screen
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 4

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)

    # Create a custom style for the button
    style = ttk.Style()
    style.configure("RoundedButton.TButton", font=("Arial", 12), borderwidth=0, relief="flat", background="#FFFFFF")
    style.map("RoundedButton.TButton", background=[("active", "#FFFFFF")])

    frame = ttk.Frame(root)
    frame.pack(pady=20)

    generate_button = ttk.Button(frame, text="Rename PDF", command=rename_file, style="RoundedButton.TButton")
    generate_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
