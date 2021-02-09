#!/usr/bin/env python

import tkinter as tk
import _tkinter
import webbrowser
import library

entryText = ''
markdown_link = 'https://www.markdownguide.org/basic-syntax/'

root = tk.Tk()
root.title('Activity Logger')
root.resizable(False, False)


def write_entry():
    library.write_entry(entryText)
    text_box.delete(1.0, tk.END)


info = tk.Label(root, text='This text box supports markdown formatting. For instance, you can do *italics*, **bold text**, \n'
                           '`inline code`, [a link](https://google.com), ![an image stored in a folder](image_folder/example.png),\n'
                           '![an image stored online](https://link.to/image.png)etc.\n\n')
link = tk.Label(root, text=f'[Click this]({markdown_link}) to see everything you can do with markdown.')
text_box = tk.Text(root, wrap='word')
write_button = tk.Button(root, text='Write entry to file', command=write_entry, state='disabled')
exit_button = tk.Button(root, text='Exit', command=root.destroy)

info.grid(column=0, row=0, pady=(10, 0), padx=10, columnspan=2)
link.grid(column=0, row=1, pady=0, padx=10, columnspan=2)
text_box.grid(column=0, row=2, pady=(10, 30), padx=10, columnspan=2)
write_button.grid(column=0, row=3, pady=(0, 10), padx=(0, 20))
exit_button.grid(column=1, row=3, pady=(0, 10), padx=(20, 0))

link.bind('<Button-1>', lambda _: webbrowser.open_new_tab(markdown_link))  # lambda is used for an anonymous callback function


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
