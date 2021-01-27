import tkinter as tk
import _tkinter
import acca_lib

entryText = ''

root = tk.Tk()
root.title('Activity Logger')
root.resizable(False, False)


def write_entry():
    acca_lib.write_entry(entryText)
    text_box.delete(1.0, tk.END)


info = tk.Label(root, text='This text box supports markdown formatting. For instance, you can do *italics*, **bold**, `code`, [links](https://links.com), etc.')
text_box = tk.Text(root)
write_button = tk.Button(root, text='Write entry to file', command=write_entry, state='disabled')

info.grid(column=0, row=0, pady=(10, 0), padx=10)
text_box.grid(column=0, row=1, pady=(10, 30), padx=10)
write_button.grid(column=0, row=2, pady=(0, 10))


def update_loop():
    global entryText

    while True:
        try:
            entryText = text_box.get(1.0, tk.END)
            if entryText != '\n':
                write_button.config(state='normal')
            else:
                write_button.config(state='disabled')

            root.update()
        except _tkinter.TclError:
            return


if __name__ == '__main__':
    update_loop()
