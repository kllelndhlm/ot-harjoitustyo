import unittest
import tkinter as tk
from tkinter import ttk, constants
import tkinter.font as font
from services.edit_service import EditService
from ui.edit_view import EditView
from ui.ui import UI
from services.edit_service import EditService

class TestEditService(unittest.TestCase):
    def setUp(self):
        self.kokeilu = EditService(root)

    def test_copy(self):
        self.kokeilu._txt_edit = tk.Text(root)
        self.assertEqual(self.kokeilu.copy_txt(), "")

root = tk.Tk()
