from tkinter import Tk, Button, filedialog, Label, messagebox, simpledialog
from tkinter.ttk import Treeview
import pandas as pd
df=None

def upload_file():
    global df
    file_path=filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
     try:
            df=pd.read_csv(file_path, encoding="ISO-8859-1")
            file_label.config(text=f"File Uploaded:{file_path.split('/')[-1]}")
            print("File uploaded successfully")
            print(df.head())

     except Exception as e:
        file_label.config(text="Error to upload file")
        print(f"Error: {e}")

def missing_value() :
    global df
    if df is  None:
        df.dropna()
        fill_value = simpledialog.askstring("Input", "Enter a value to replace missing values:")
        if fill_value is not None:
            df.fillna(fill_value, inplace=True)
            messagebox.showinfo("Success", f"Missing values filled with '{fill_value}'!")
        else:
            messagebox.showerror("Error", "No file uploaded. Please upload a CSV file first.")


def remove_duplicate():
    global df
    if df is not None:
      df.drop_duplicates(inplace=True)
      messagebox.showinfo("Success", "Duplicate rows removed!")
    else:
         messagebox.showerror("Error", "No file uploaded. Please upload a CSV file first.")


def display_data():
    global df
    if df is not None:
        print("DataFrame Content:")
        print(df)  # Debugging: Check DataFrame content
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        print(f"Columns: {list(df.columns)}")  # Debugging: Check columns
        tree["show"] = "headings"

        # Add column headers
        for col in df.columns:
            print(f"Adding column: {col}")  # Debugging: Confirm column headers
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Add rows
        for index, row in df.iterrows():
            print(f"Inserting row: {list(row)}")  # Debugging: Confirm rows
            tree.insert("", "end", values=list(row))
    else:
        messagebox.showerror("Error", "No file uploaded or data to display.")



root=Tk()
root.title('Data Visualizer')
root.geometry("900x900")
Button(root, text='Upload CSV' , command=upload_file).pack(pady=10)
#label to display file name
file_label= Label(root, text="No file uploaded" )

Button(root, text='Remove missing values', command=missing_value).pack(pady=10)
Button(root, text='Remove duplicate values', command=remove_duplicate).pack(pady=10)
file_label.pack(pady=10)
tree=Treeview(root)
tree.pack(pady=10)
root.mainloop()