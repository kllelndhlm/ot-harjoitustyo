import tkinter as tk
from tkinter import ttk, constants
from tkinter import *
import tkinter.font as font


class EditView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._root.rowconfigure(0, minsize=800, weight=1)

        self._root.columnconfigure(1, minsize=800, weight=1)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _delete_line_from_result(self):
        self._txt_edit.delete(self._selection_linestart,
                              self._selection_lineend)

    def _delete_selection(self):
        self._txt_edit.delete(self._selection_start, self._selection_end)

    def _remove_markdown(self):
        while self._selection[0] == "#" or self._selection[0] == " ":
            self._selection = self._selection[1:]

    def _selection_indices(self):
        self._selection_linestart = self._txt_edit.index("sel.last linestart")
        self._selection_lineend = self._txt_edit.index("sel.last lineend")
        self._selection_start = self._txt_edit.index("sel.first")
        self._selection_end = self._txt_edit.index("sel.last")
        self._up_till_selection = self._txt_edit.get(
            "1.0", self._selection_start)
        self._following_selection = self._txt_edit.get(
            self._selection_end, END)

    def _h1_markdown(self):
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "# " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _h2_markdown(self):
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "## " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _h3_markdown(self):
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "### " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _body_markdown(self):
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _italic_markdown(self):
        self._selection = self._txt_edit.get("sel.first", "sel.last")
        self._selection_indices()
        if self._selection[0] == "_" and self._selection[-1] == "_":
            while self._selection[0] == "_":
                self._selection = self._selection[1:]
            while self._selection[-1] == "_":
                self._selection = self._selection[:-1]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), self._selection)
        else:
            while self._selection[0] == "_":
                self._selection = self._selection[1:]
            while self._selection[-1] == "_":
                self._selection = self._selection[:-1]
            self._delete_selection()
            self._txt_edit.insert(self._selection_start,
                                  "_" + self._selection + "_")
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _bold_markdown(self):
        self._selection = self._txt_edit.get("sel.first", "sel.last")
        self._selection_indices()
        if self._selection[0] == "*" and self._selection[-1] == "*":
            while self._selection[0] == "*":
                self._selection = self._selection[1:]
            while self._selection[-1] == "*":
                self._selection = self._selection[:-1]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), self._selection)
        else:
            while self._selection[0] == "*":
                self._selection = self._selection[1:]
            while self._selection[-1] == "*":
                self._selection = self._selection[:-1]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), "**" + self._selection + "**")
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def _copy_txt(self):
        self._root.clipboard_clear()
        copied = self._txt_edit.get("1.0", "end-1c")
        self._root.clipboard_append(copied)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._txt_edit = tk.Text(self._root)

        h1_button = ttk.Button(
            master=self._frame,
            text="Headline1",
            command=self._h1_markdown
        )
        h2_button = ttk.Button(
            master=self._frame,
            text="Headline2",
            command=self._h2_markdown
        )
        h3_button = ttk.Button(
            master=self._frame,
            text="Headline3",
            command=self._h3_markdown
        )
        body_button = ttk.Button(
            master=self._frame, text="Body",
            command=self._body_markdown
        )
        italic_button = ttk.Button(
            master=self._frame, text="Italic",
            command=self._italic_markdown
        )
        bold_button = ttk.Button(
            master=self._frame, text="Bold",
            command=self._bold_markdown
        )
        copy_button = ttk.Button(
            master=self._frame, text="Copy",
            command=self._copy_txt
        )

        self._txt_edit.pack(fill="both", expand=True, side="right")
        h1_button.pack()
        h2_button.pack()
        h3_button.pack()
        body_button.pack()
        italic_button.pack()
        bold_button.pack()
        copy_button.pack()
