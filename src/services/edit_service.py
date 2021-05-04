import tkinter as tk
from tkinter import ttk, constants
from tkinter import *

class EditService:
    """Tekstin muokkauksesta vastaavat funktiot
    """
    def __init__(self, root):
        self._root = root
        self._frame = None

    def selection_indices(self):
        """Muodostaa tekstin muokkauksessa tarvittavat indeksit
           graaffisessa käyttöliittymässä valitun tekstin perusteella.
        """
        self._selection_linestart = self._txt_edit.index("sel.last linestart")
        self._selection_lineend = self._txt_edit.index("sel.last lineend")
        self._selection_start = self._txt_edit.index("sel.first")
        self._selection_end = self._txt_edit.index("sel.last")
        self._up_till_selection = self._txt_edit.get(
            "1.0", self._selection_start)
        self._following_selection = self._txt_edit.get(
            self._selection_end, END)

    def h1_markdown(self):
        """Muokkaa valitusta tekstistä koon 1 otsikon.
        """
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "# " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def h2_markdown(self):
        """Muokkaa valitusta tekstistä koon 2 otsikon.
        """
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "## " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def h3_markdown(self):
        """Muokkaa valitusta tekstistä koon 3 otsikon.
        """
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "### " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def body_markdown(self):
        """Poistaa mahdollisen muotoilun; tekee valinnasta leipätekstiä.
        """
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def italic_markdown(self):
        """Kursivoi tai poistaa aiemman kursivoinnin."""
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

    def bold_markdown(self):
        """Lihavoi tai poistaa aiemman lihavoinnin"""
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

    def strikethrough_markdown(self):
        """Yliviivaa tai poistaa aiemman yliviivauksen."""
        self._selection = self._txt_edit.get("sel.first", "sel.last")
        self._selection_indices()
        if self._selection[:2] == "~~" and self._selection[-2:] == "~~":
            while self._selection[:2] == "~~":
                self._selection = self._selection[2:]
            while self._selection[-2:] == "~~":
                self._selection = self._selection[:-2]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), self._selection)
        else:
            while self._selection[:2] == "~~":
                self._selection = self._selection[3:]
            while self._selection[:-2] == "~~":
                self._selection = self._selection[:-2]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), "~~" + self._selection + "~~")
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def copy_txt(self):
        """Kopioi tekstin leikepöydälle."""
        self._root.clipboard_clear()
        copied = self._txt_edit.get("1.0", "end-1c")
        self._root.clipboard_append(copied)
