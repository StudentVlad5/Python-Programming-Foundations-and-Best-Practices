import urwid

class SimpleMultiLineEdit(urwid.Edit):
    """
    A simple Edit widget for multiline input.
    """
    def __init__(self, caption="", edit_text="", multiline=True, **kwargs):
        """
        Initializes the SimpleMultiLineEdit widget.

        :param caption: String that appears above the edit field.
        :param edit_text: Initial text in the edit field.
        :param multiline: Boolean indicating if the edit field is multiline.
        :param kwargs: Additional keyword arguments for customization.
        """
        super().__init__(caption, edit_text, multiline=multiline, **kwargs)

    def keypress(self, size, key):
        """
        Handles keypress events to allow for exiting the editor.

        :param size: The size of the widget.
        :param key: The key that was pressed.
        :return: The result of the superclass keypress method.
        """
        global entered_text
        if key == 'ctrl d':
            print("Exiting editor.")
            entered_text = self.edit_text
            raise urwid.ExitMainLoop()
        return super().keypress(size, key)


class TextEditor:
    """
    TextEditor class that encapsulates the functionality of the text editor.
    """
    def __init__(self):
        """
        Initializes the TextEditor instance.
        """
        self.entered_text = None

    def run_editor(self, initial_text=""):
        """
        Runs the text editor with an optional initial text for editing.

        :param initial_text: Optional string to pre-fill the editor.
        """
        global edit
        edit = SimpleMultiLineEdit(caption="Enter multiline text (Ctrl+D to exit):\n", 
                                    multiline=True, 
                                    edit_text=initial_text)  # Pre-fill with initial text
        fill = urwid.Filler(edit, 'top')
        loop = urwid.MainLoop(fill, palette=[('reversed', 'standout', '')])

        try:
            loop.run()
        except urwid.ExitMainLoop:
            pass

        self.entered_text = edit.edit_text  # Store entered text

    def get_entered_text(self):
        """
        Returns the text entered in the editor.

        :return: The text entered by the user.
        """
        return self.entered_text


def simple_editor(initial_text=""):
    """
    Function to run the text editor.

    :param initial_text: Optional string to pre-fill the editor.
    :return: The text entered by the user.
    """
    editor = TextEditor()
    editor.run_editor(initial_text)  # Pass in text for editing
    return editor.get_entered_text()  # Return the entered text


if __name__ == "__main__":
    initial_text = "My text"
    edited_text = simple_editor(initial_text)  # Call editor as a function
    if edited_text:
        print("\nEntered text:\n", edited_text)
    else:
        print("\nEditor was closed without saving.")