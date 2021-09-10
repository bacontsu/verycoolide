import TKlighter
from tkinter import *
import json


class HighLighter:
    def __init__(self, code):
        self.code = code
        with open("config/syntax_config.json", "r") as f:
            self.syntax_colors = json.load(f)["highlight"]
            f.close()
        self.SetSyntaxColors()

    def SetSyntaxColors(self):
        self.string = self.syntax_colors['string']
        self.number = self.syntax_colors['number']
        self.if_else = self.syntax_colors['if_else']
        self.print = self.syntax_colors['print']
        self.method = self.syntax_colors['method']
        self.keywords = self.syntax_colors['keywords']

    def Highlight(self, event):
        TKlighter.double_qouts_h(self.code, self.string)   
        TKlighter.int_h(self.code, self.number)
        TKlighter.if_h(self.code, self.if_else)
        TKlighter.elif_h(self.code, self.if_else)
        TKlighter.else_h(self.code, self.if_else)
        TKlighter.print_h(self.code, self.print)
        TKlighter.input_h(self.code, self.print)
        TKlighter.and_h(self.code, self.keywords)
        TKlighter.or_h(self.code, self.keywords)
        TKlighter.return_h(self.code, self.keywords)
        TKlighter.break_h(self.code, self.keywords)
        TKlighter.None_h(self.code, self.keywords)
        TKlighter.try_h(self.code, self.keywords)
        TKlighter.except_h(self.code, self.keywords)
        TKlighter.del_h(self.code, self.keywords)
        TKlighter.False_h(self.code, self.keywords)
        TKlighter.True_h(self.code, self.keywords)
        TKlighter.def_h(self.code, self.method)
        TKlighter.class_h(self.code, self.method)
        TKlighter.as_h(self.code, self.keywords)
        TKlighter.for_h(self.code, self.keywords)
        TKlighter.from_h(self.code, self.keywords)
        TKlighter.global_h(self.code, self.keywords)
        TKlighter.import_h(self.code, self.keywords)
        TKlighter.in_h(self.code, self.keywords)
        TKlighter.while_h(self.code, self.keywords)
        TKlighter.lambda_h(self.code, self.keywords)
        TKlighter.with_h(self.code, self.keywords)
        TKlighter.pass_h(self.code, self.keywords)

        


