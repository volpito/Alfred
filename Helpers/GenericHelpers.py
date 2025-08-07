import ctypes  # An included library with Python install.

class GenericHelpers:
    
    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
