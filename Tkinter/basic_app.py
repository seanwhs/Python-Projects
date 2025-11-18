from tkinter import *
from tkinter import messagebox

# Frame class
class WidgetFrame(Frame):
    """A reusable frame containing a label, entry, and buttons."""
    def __init__(self, master, title="Frame", **kwargs):
        super().__init__(master, **kwargs)
        self.configure(relief=RIDGE, bd=2, padx=10, pady=10, bg="#f4f4f4")
        self.create_widgets(title)

    def create_widgets(self, title):
        # Header label
        self.label = Label(self, text=title, font=('Arial', 14, 'bold'), bg="#f4f4f4")
        self.label.pack(pady=10)

        # Entry field
        self.entry = Entry(self, font=('Arial', 12), width=20)
        self.entry.pack(pady=10)

        # Buttons
        self.submit_button = Button(self, text="Submit", bg="#007bff", fg="white",
                                    command=self.submit_action)
        self.submit_button.pack(pady=5, fill='x')

        self.exit_button = Button(self, text="Exit", bg="#dc3545", fg="white",
                                  command=self.master.quit)
        self.exit_button.pack(pady=5, fill='x')

    def submit_action(self):
        text = self.entry.get()
        if text.strip():
            messagebox.showinfo("Input Received", f"You entered: {text}")
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Missing Input", "Please enter something!")

# Main application class
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window with Frames")
        self.root.geometry("600x250")
        self.root.configure(bg="#f4f4f4")
        self.create_frames()

    def create_frames(self):
        # Instantiate two frame objects side by side
        self.frame1 = WidgetFrame(self.root, title="Frame 1")
        self.frame1.grid(row=0, column=0, padx=20, pady=20)

        self.frame2 = WidgetFrame(self.root, title="Frame 2")
        self.frame2.grid(row=0, column=1, padx=20, pady=20)

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
