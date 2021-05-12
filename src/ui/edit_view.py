import tkinter as tk
from tkinter import ttk, constants
from tkinter import *
import tkinter.font as font
from services.edit_service import EditService as edit_service

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
        """Poistaa tekstivalinnan."""
        self._txt_edit.delete(self._selection_start, self._selection_end)

    def _remove_markdown(self):
        """Poistaa valitusta otsikkomuotoillusta tekstistä risuaidat."""
        while self._selection[0] == "#" or self._selection[0] == " ":
            self._selection = self._selection[1:]

    def _selection_indices(self):
        edit_service.selection_indices(self)

    def _h123_sel_rmv_ind_del(self):
        edit_service.h123_sel_rmv_ind_del(self)

    def _italic_bold_strikethrough(self, indx, markdn):
        edit_service.italic_bold_strikethrough(self, indx, markdn)

    def _h1_markdown(self):
        edit_service.h1_markdown(self)

    def _h2_markdown(self):
        edit_service.h2_markdown(self)

    def _h3_markdown(self):
        edit_service.h3_markdown(self)

    def _body_markdown(self):
        edit_service.body_markdown(self)

    def _italic_markdown(self):
        edit_service.italic_markdown(self)

    def _bold_markdown(self):
        edit_service.bold_markdown(self)

    def _strikethrough_markdown(self):
        edit_service.strikethrough_markdown(self)

    def _copy_txt(self):
        edit_service.copy_txt(self)

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
        strikethrough_button = ttk.Button(
            master=self._frame, text="Strikethrough",
            command=self._strikethrough_markdown
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
        strikethrough_button.pack()
        copy_button.pack()
