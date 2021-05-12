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

    def h123_sel_rmv_ind_del(self):
        """Kaikissa otsikkomuotoiluissa kutsutut funktiot
        """
        self._selection = self._txt_edit.get(
            "sel.last linestart", "sel.last lineend")
        self._remove_markdown()
        self._selection_indices()
        self._delete_line_from_result()

    def h1_markdown(self):
        """Muokkaa valitusta tekstistä koon 1 otsikon.
        """
        self._h123_sel_rmv_ind_del()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "# " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def h2_markdown(self):
        """Muokkaa valitusta tekstistä koon 2 otsikon.
        """
        self._h123_sel_rmv_ind_del()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "## " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def h3_markdown(self):
        """Muokkaa valitusta tekstistä koon 3 otsikon.
        """
        self._h123_sel_rmv_ind_del()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), "### " + self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def body_markdown(self):
        """Poistaa mahdollisen muotoilun; tekee valinnasta leipätekstiä.
        """
        self._h123_sel_rmv_ind_del()
        self._txt_edit.insert(self._txt_edit.index(
            self._selection_linestart), self._selection)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def italic_bold_strikethrough(self, indx, markdn):
        """Käsittelee valinnan alkuun ja loppuun tulevat muotoilut
        """
        self.indx = indx
        self.markdn = markdn
        self._selection = self._txt_edit.get("sel.first", "sel.last")
        self._selection_indices()
        if self._selection[:indx] == markdn and self._selection[indx*-1:] == markdn:
            self._selection = self._selection[indx:]
            self._selection = self._selection[:indx*-1]
            self._delete_selection()
            self._txt_edit.insert(self._txt_edit.index(
                self._selection_start), self._selection)
        else:
            self._delete_selection()
            self._txt_edit.insert(self._selection_start,
                                  markdn + self._selection + markdn)
        self._txt_edit.tag_remove(SEL, "1.0", END)

    def italic_markdown(self):
        """Kursivoi tai poistaa aiemman kursivoinnin.
        """
        self._italic_bold_strikethrough(1, "_")

    def bold_markdown(self):
        """Lihavoi tai poistaa aiemman lihavoinnin
        """
        self._italic_bold_strikethrough(1, "*")

    def strikethrough_markdown(self):
        """Yliviivaa tai poistaa aiemman yliviivauksen.
        """
        self._italic_bold_strikethrough(2, "~~")

    def copy_txt(self):
        """Kopioi tekstin leikepöydälle.
        """
        self._root.clipboard_clear()
        copied = self._txt_edit.get("1.0", "end-1c")
        self._root.clipboard_append(copied)
