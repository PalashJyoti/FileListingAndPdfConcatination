import tkinter as tk
from Package import browse, concatenate


def show_toast(root, message, duration):
    toast = tk.Toplevel(root)
    toast.overrideredirect(True)  # Remove window decorations
    toast.attributes('-topmost', True)  # Keep the window on top
    toast.geometry(
        f"+{toast.winfo_screenwidth() - 10}+{toast.winfo_screenheight() - 10}")  # Position the window in the bottom-right corner
    toast.configure(bg="#333333")  # Set the background color of the window

    label = tk.Label(toast, text=message, fg="white", bg="#333333", padx=10, pady=5)  # Customize the label
    label.pack()

    # Schedule the dismissal of the toast after the specified duration
    toast.after(duration, toast.destroy)


def button_click():
    path = entry.get()
    fileList = browse.listFiles(path)
    # Add items to the list view
    for item in fileList:
        listbox.insert(tk.END, item)


def list_button_click():
    path = entry.get()
    try:
        # Usage example
        directory = path
        output_file = f"{path}/merged.pdf"
        concatenate.merge_pdfs(directory, output_file)
        show_toast(window, "Successfully Concatenated All PDFs.", 3000)
    except Exception as e:
        print(e)


# Create the main window
window = tk.Tk()
window.title("FileO")

# Create a frame to hold the label, entry, and button horizontally
frame_top = tk.Frame(window)
frame_top.pack()

# Label
label = tk.Label(frame_top, text="Location:")
label.pack(side=tk.LEFT)

# Entry (Edit text)
entry = tk.Entry(frame_top)
entry.pack(side=tk.LEFT)

# Button
button = tk.Button(frame_top, text="Browse", command=button_click)
button.pack(side=tk.LEFT)

# Create a frame to hold the list view and button
frame_bottom = tk.Frame(window)
frame_bottom.pack()

# List view
listbox = tk.Listbox(frame_bottom)
listbox.pack(side=tk.LEFT)

# Button for list view
list_button = tk.Button(frame_bottom, text="Concatenate", command=list_button_click)
list_button.pack(side=tk.RIGHT)

# Run the GUI
window.mainloop()
