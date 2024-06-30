import tkinter as tk
from tkinter import messagebox
import os

class NoteLister:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepy")

        # Note list
        self.notes = []

        # Load notes from file
        self.load_notes()

        # Frame for note entry
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)

        self.note_label = tk.Label(self.entry_frame, text="Enter Note:")
        self.note_label.pack(side=tk.LEFT)

        self.note_entry = tk.Entry(self.entry_frame, width=40)
        self.note_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.entry_frame, text="Add Note", command=self.add_note)
        self.add_button.pack(side=tk.LEFT)

        # Frame for displaying notes
        self.notes_frame = tk.Frame(root)
        self.notes_frame.pack(pady=10)

        self.notes_listbox = tk.Listbox(self.notes_frame, width=50, height=15)
        self.notes_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.notes_frame, orient=tk.VERTICAL, command=self.notes_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.notes_listbox.config(yscrollcommand=self.scrollbar.set)

        self.update_notes_listbox()

        # Frame for actions
        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=10)

        self.delete_button = tk.Button(self.action_frame, text="Delete Selected Note", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT)

        # Save notes on closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_note(self):
        note = self.note_entry.get()
        if note:
            self.notes.append(note)
            self.update_notes_listbox()
            self.note_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Note cannot be empty")

    def delete_note(self):
        selected_note_index = self.notes_listbox.curselection()
        if selected_note_index:
            note_index = selected_note_index[0]
            del self.notes[note_index]
            self.update_notes_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a note to delete")

    def update_notes_listbox(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note)

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for note in self.notes:
                file.write(note + "\n")

    def load_notes(self):
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as file:
                self.notes = [line.strip() for line in file.readlines()]

    def on_closing(self):
        self.save_notes()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteLister(root)
    root.mainloop()
