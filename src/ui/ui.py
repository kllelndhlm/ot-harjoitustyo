from ui.edit_view import EditView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_edit_view()

    def _show_edit_view(self):
        self._current_view = EditView(
            self._root
        )

        self._current_view.pack()
