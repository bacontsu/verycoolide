from tkinter import ttk

class VeryCoolScrollbar(ttk.Scrollbar):
    def save_pack_data(self, *args, **kwargs):
        self.pack_data = kwargs
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.pack_forget()
        else:
            self.pack(self.pack_data)
        ttk.Scrollbar.set(self, low, high)