import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.select_dir_button = tk.Button(self, text="Select directory", command=self.select_dir)
        self.select_dir_button.grid(row=0, column=0)

        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=1, column=0)

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=1)

        self.results_text = tk.Text(self, height=20, width=60)
        self.results_text.grid(row=2, column=0, columnspan=2)

        self.download_button = tk.Button(self, text="Download", command=self.download, state=tk.DISABLED)
        self.download_button.grid(row=3, column=1)

    def select_dir(self):
        selected_dir = filedialog.askdirectory(initialdir=os.getcwd(), title="Select directory")
        if selected_dir:
            self.selected_dir = selected_dir
            messagebox.showinfo("Selected directory", "Selected directory: {}".format(selected_dir))

    def search(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showerror("Error", "Please enter a query")
            return
        if not hasattr(self, 'selected_dir'):
            messagebox.showerror("Error", "Please select a directory")
            return
        index_file = os.path.join(os.getcwd(), 'index.csv')
        subprocess.run(['python', 'index.py', '--input_dir', self.selected_dir, '--output_file', index_file])
        results_file = os.path.join(os.getcwd(), 'results.csv')
        subprocess.run(['python', 'search.py', '--input_file', index_file, '--query', query, '--output_file', results_file])
        with open(results_file, 'r', encoding='utf-8') as f:
            self.results_text.delete('1.0', tk.END)
            for line in f:
                file_path, text = line.strip().split(',', 1)
                self.results_text.insert(tk.END, "{}\n{}\n\n".format(file_path, text))
            if self.results_text.get('1.0', tk.END) != '\n':
                self.download_button.config(state=tk.NORMAL)

    def download(self):
        results_file = os.path.join(os.getcwd(), 'results.csv')
        subprocess.run(['python', 'download.py', '--input_file', results_file])
        messagebox.showinfo("Download", "Downloaded files to current directory")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()