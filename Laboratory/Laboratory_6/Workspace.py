import ctypes


def raise_if_0(result, func, arguments):
    if result == 0:
        exit()


def color_print(text, color):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleTextAttribute = _k32.SetConsoleTextAttribute
    _SetConsoleTextAttribute.restype = ctypes.c_bool
    _SetConsoleTextAttribute.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
    _SetConsoleTextAttribute.errcheck = raise_if_0
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleTextAttribute(hout, color)
    print(text, end='', flush=True)
    _SetConsoleTextAttribute(hout, 7)


def goto_xy(x,y):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleCursorPosition = _k32.SetConsoleCursorPosition
    _SetConsoleCursorPosition.restype = ctypes.c_bool
    _SetConsoleCursorPosition.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    _SetConsoleCursorPosition.errcheck = raise_if_0
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleCursorPosition(hout, ctypes.c_ulong(x + (y << 16)))



class Object ():

    def __init__ (self, x, y, w, h, color, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.label = label
        self.objects = []


        def add_object (self, obj):
            self.objects.append(obj)

        def add_objects(self, *obj):
            for obj in obj:
                self.objects.append(obj)

        def draw ():
            return


class Button (Object):

    def __init__ (self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = '|' + ' ' * (self.w - 2) + '|'
        self.window_label = "|" + self.label + " " * (self.w - 2) + "|"
        self.window_label = f"|{self.window_label}^(self.w - 2) + "|"

    def draw (self):
        for i in range (self.h):
            goto_xy(self.x, self.y + i)
            if i == 0 or i == 2 or i == self.h - 1:
                color_print(self.composed_line, self.color)
            elif i == self.h // 2:
                color_print(self.window_label, self.color)
            else:
                color_print(self.middle_line, self.color)
        for i in self.objects:
            i.draw()



class Window (Object):

    def __init__ (self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = '|' + ' ' * (self.w - 2) + '|'
        self.window_label = "|" + self.label + " " * (self.w - 2) + "|"
        self.window_label = f"|{self.window_label}^(self.w - 2) + "|"

    def draw (self):
        for i in range (self.h):
            goto_xy(self.x, self.y + i)
            if i == 0 or i == 2 or i == self.h - 1:
                color_print(self.composed_line, self.color)
            elif i == self.h // 2:
                color_print(self.window_label, self.color)
            else:
                color_print(self.middle_line, self.color)
        for i in self.objects:
            i.draw()


class Panel (Object):
    def __init__ (self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = '|' + ' ' * (self.w - 2) + '|'
        self.panel_label = f"|self.label + " " * (self.w - 2) + "|"


my_window = Window(5, 5, 200, 50, 0x1F, "Window")

left_panel = Panel(5, 5, 50, 30, 0x71, "Panel 1")
right_panel = Panel(60, 5, 50, 30, 0x72, "Panel 2")
panel_3 = Panel(60, 5, 50, 30, 0x71, "Panel 3")
ok_button = Button(7, 29, 15, 3, 0xA0, "OK")
cancel_button = Button(7, 29, 15, 3, 0xA0, "Cancel")
left_panel.add_object(panel_3)
panel_3.add_object(ok_button)
my_window.add_objects(left_panel, right_panel)

my_window.draw()