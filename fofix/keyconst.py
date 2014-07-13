import sdl2 as sdl

KEY_A = 1
KEY_B = 2
KEY_C = 3
KEY_D = 4
KEY_E = 5
KEY_F = 6
KEY_G = 7
KEY_H = 8
KEY_I = 9
KEY_J = 10
KEY_K = 11
KEY_L = 12
KEY_M = 13
KEY_N = 14
KEY_O = 15
KEY_P = 16
KEY_Q = 17
KEY_R = 18
KEY_S = 19
KEY_T = 20
KEY_U = 21
KEY_V = 22
KEY_W = 23
KEY_X = 24
KEY_Y = 25
KEY_Z = 26
KEY_1 = 27
KEY_2 = 28
KEY_3 = 29
KEY_4 = 30
KEY_5 = 31
KEY_6 = 32
KEY_7 = 33
KEY_7 = 34
KEY_8 = 35
KEY_9 = 36
KEY_RETURN = 37
KEY_ESCAPE = 38
KEY_BACKSPACE = 39
KEY_TAB = 40
KEY_SPACE = 41
KEY_MINUS = 42
KEY_EQUALS = 43
KEY_LEFT_BRACKET = 44
KEY_RIGHT_BRACKET = 45
KEY_BACKSLASH = 46
KEY_SEMICOLON = 47
KEY_APOSTROPHE = 48
KEY_GRAVE = 49
KEY_COMMA = 50
KEY_PERIOD = 51
KEY_SLASH = 52
KEY_CAPS_LOCK = 53
KEY_F1 = 54
KEY_F2 = 55
KEY_F3 = 56
KEY_F4 = 57
KEY_F5 = 58
KEY_F6 = 59
KEY_F7 = 60
KEY_F8 = 61
KEY_F9 = 62
KEY_F10 = 63
KEY_F11 = 64
KEY_F12 = 65
KEY_PRINT_SCREEN = 66
KEY_SCROLL_LOCK = 67
KEY_PAUSE = 68
KEY_INSERT = 69
KEY_HOME = 70
KEY_PAGE_UP = 71
KEY_DELETE = 72
KEY_END = 73
KEY_PAGE_DOWN = 74
KEY_RIGHT = 75
KEY_LEFT = 76
KEY_DOWN = 77
KEY_UP = 78
KEY_NUMLOCK_CLEAR = 79
KEY_KP_DIVIDE = 80
KEY_KP_MULTIPLY = 81
KEY_KP_MINUS = 82
KEY_KP_PLUS = 83
KEY_KP_ENTER = 84
KEY_KP_1 = 85
KEY_KP_2 = 86
KEY_KP_3 = 87
KEY_KP_4 = 88
KEY_KP_5 = 89
KEY_KP_6 = 90
KEY_KP_7 = 91
KEY_KP_8 = 92
KEY_KP_9 = 93
KEY_KP_0 = 94
KEY_KP_PERIOD = 95
KEY_NON_US_BACKSLASH = 96
KEY_LEFT_CTRL = 97
KEY_LEFT_SHIFT = 98
KEY_LEFT_ALT = 99
KEY_LEFT_SUPER = 100
KEY_RIGHT_CTRL = 101
KEY_RIGHT_SHIFT = 102
KEY_RIGHT_ALT = 103
KEY_RIGHT_SUPER = 104

MOD_NONE = None
MOD_LEFT_SHIFT = 1
MOD_RIGHT_SHIFT = 2
MOD_LEFT_CTRL = 3
MOD_RIGHT_CTRL = 4
MOD_LEFT_ALT = 5
MOD_RIGHT_ALT = 6
MOD_LEFT_SUPER = 7
MOD_RIGHT_SUPER = 8
MOD_NUM = 9
MOD_CAPS = 10


modmap = {sdl.KMOD_NONE: MOD_NONE,
          sdl.KMOD_LSHIFT: MOD_LEFT_SHIFT,
          sdl.KMOD_RSHIFT: MOD_RIGHT_SHIFT,
          sdl.KMOD_LCTRL: MOD_LEFT_CTRL,
          sdl.KMOD_RCTRL: MOD_RIGHT_CTRL,
          sdl.KMOD_LALT: MOD_LEFT_ALT,
          sdl.KMOD_RALT: MOD_RIGHT_ALT,
          sdl.KMOD_LGUI: MOD_LEFT_SUPER,
          sdl.KMOD_RGUI: MOD_RIGHT_SUPER,
          sdl.KMOD_NUM: MOD_NUM,
          sdl.KMOD_CAPS: MOD_CAPS}

keystrMap = {KEY_CAPS_LOCK: 'CAPS LOCK',
             KEY_F1: 'F1',
             KEY_F2: 'F2',
             KEY_F3: 'F3',
             KEY_F4: 'F4',
             KEY_F5: 'F5',
             KEY_F6: 'F6',
             KEY_F7: 'F7',
             KEY_F8: 'F8',
             KEY_F9: 'F9',
             KEY_F10: 'F10',
             KEY_F11: 'F11',
             KEY_F12: 'F12',
             KEY_PRINT_SCREEN: 'PRINT SCREEN',
             KEY_SCROLL_LOCK: 'SCROLL LOCK',
             KEY_PAUSE: 'PAUSE',
             KEY_INSERT: 'INSERT',
             KEY_HOME: 'HOME',
             KEY_PAGE_UP: 'PAGE UP',
             KEY_END: 'END',
             KEY_PAGE_DOWN: 'PAGE DOWN',
             KEY_RIGHT: 'RIGHT',
             KEY_LEFT: 'LEFT',
             KEY_DOWN: 'DOWN',
             KEY_UP: 'UP',
             KEY_NUMLOCK_CLEAR: 'NUMLOCK CLEAR',
             KEY_LEFT_CTRL: 'LEFT CTRL',
             KEY_LEFT_SHIFT: 'LEFT SHIFT',
             KEY_LEFT_ALT: 'LEFT ALT',
             KEY_LEFT_SUPER: 'LEFT SUPER',
             KEY_RIGHT_CTRL: 'RIGHT CTRL',
             KEY_RIGHT_SHIFT: 'RIGHT SHIFT',
             KEY_RIGHT_ALT: 'RIGHT ALT',
             KEY_RIGHT_SUPER: 'RIGHT SUPER'}

def process_modkeys(value):
    keys = []
    for key in modmap:
        if value & key:
            keys.append(modmap[key])
    return keys

def process_key_char(value):
    char = None
    try:
        char = str(chr(value))
    except ValueError:
        temp = value ^ (1<<30)
        if temp in keymap:
            
            char = keystrMap[keymap[temp]]

    return char

keymap = {sdl.SDL_SCANCODE_A: KEY_A,
          sdl.SDL_SCANCODE_B: KEY_B,
          sdl.SDL_SCANCODE_C: KEY_C,
          sdl.SDL_SCANCODE_D: KEY_D,
          sdl.SDL_SCANCODE_E: KEY_E,
          sdl.SDL_SCANCODE_F: KEY_F,
          sdl.SDL_SCANCODE_G: KEY_G,
          sdl.SDL_SCANCODE_H: KEY_H,
          sdl.SDL_SCANCODE_I: KEY_I,
          sdl.SDL_SCANCODE_J: KEY_J,
          sdl.SDL_SCANCODE_K: KEY_K,
          sdl.SDL_SCANCODE_L: KEY_L,
          sdl.SDL_SCANCODE_M: KEY_M,
          sdl.SDL_SCANCODE_N: KEY_N,
          sdl.SDL_SCANCODE_O: KEY_O,
          sdl.SDL_SCANCODE_P: KEY_P,
          sdl.SDL_SCANCODE_Q: KEY_Q,
          sdl.SDL_SCANCODE_R: KEY_R,
          sdl.SDL_SCANCODE_S: KEY_S,
          sdl.SDL_SCANCODE_T: KEY_T,
          sdl.SDL_SCANCODE_U: KEY_U,
          sdl.SDL_SCANCODE_V: KEY_V,
          sdl.SDL_SCANCODE_W: KEY_W,
          sdl.SDL_SCANCODE_X: KEY_X,
          sdl.SDL_SCANCODE_Y: KEY_Y,
          sdl.SDL_SCANCODE_Z: KEY_Z,
          sdl.SDL_SCANCODE_1: KEY_1,
          sdl.SDL_SCANCODE_2: KEY_2,
          sdl.SDL_SCANCODE_3: KEY_3,
          sdl.SDL_SCANCODE_4: KEY_4,
          sdl.SDL_SCANCODE_5: KEY_5,
          sdl.SDL_SCANCODE_6: KEY_6,
          sdl.SDL_SCANCODE_7: KEY_7,
          sdl.SDL_SCANCODE_8: KEY_7,
          sdl.SDL_SCANCODE_9: KEY_8,
          sdl.SDL_SCANCODE_0: KEY_9,
          sdl.SDL_SCANCODE_RETURN: KEY_RETURN,
          sdl.SDL_SCANCODE_ESCAPE: KEY_ESCAPE,
          sdl.SDL_SCANCODE_BACKSPACE: KEY_BACKSPACE,
          sdl.SDL_SCANCODE_TAB: KEY_TAB,
          sdl.SDL_SCANCODE_SPACE: KEY_SPACE,
          sdl.SDL_SCANCODE_MINUS: KEY_MINUS,
          sdl.SDL_SCANCODE_EQUALS: KEY_EQUALS,
          sdl.SDL_SCANCODE_LEFTBRACKET: KEY_LEFT_BRACKET,
          sdl.SDL_SCANCODE_RIGHTBRACKET: KEY_RIGHT_BRACKET,
          sdl.SDL_SCANCODE_BACKSLASH: KEY_BACKSLASH,
          sdl.SDL_SCANCODE_SEMICOLON: KEY_SEMICOLON,
          sdl.SDL_SCANCODE_APOSTROPHE: KEY_APOSTROPHE,
          sdl.SDL_SCANCODE_GRAVE: KEY_GRAVE,
          sdl.SDL_SCANCODE_COMMA: KEY_COMMA,
          sdl.SDL_SCANCODE_PERIOD: KEY_PERIOD,
          sdl.SDL_SCANCODE_SLASH: KEY_SLASH,
          sdl.SDL_SCANCODE_CAPSLOCK: KEY_CAPS_LOCK,
          sdl.SDL_SCANCODE_F1: KEY_F1,
          sdl.SDL_SCANCODE_F2: KEY_F2,
          sdl.SDL_SCANCODE_F3: KEY_F3,
          sdl.SDL_SCANCODE_F4: KEY_F4,
          sdl.SDL_SCANCODE_F5: KEY_F5,
          sdl.SDL_SCANCODE_F6: KEY_F6,
          sdl.SDL_SCANCODE_F7: KEY_F7,
          sdl.SDL_SCANCODE_F8: KEY_F8,
          sdl.SDL_SCANCODE_F9: KEY_F9,
          sdl.SDL_SCANCODE_F10: KEY_F10,
          sdl.SDL_SCANCODE_F11: KEY_F11,
          sdl.SDL_SCANCODE_F12: KEY_F12,
          sdl.SDL_SCANCODE_PRINTSCREEN: KEY_PRINT_SCREEN,
          sdl.SDL_SCANCODE_SCROLLLOCK: KEY_SCROLL_LOCK,
          sdl.SDL_SCANCODE_PAUSE: KEY_PAUSE,
          sdl.SDL_SCANCODE_INSERT: KEY_INSERT,
          sdl.SDL_SCANCODE_HOME: KEY_HOME,
          sdl.SDL_SCANCODE_PAGEUP: KEY_PAGE_UP,
          sdl.SDL_SCANCODE_DELETE: KEY_DELETE,
          sdl.SDL_SCANCODE_END: KEY_END,
          sdl.SDL_SCANCODE_PAGEDOWN: KEY_PAGE_DOWN,
          sdl.SDL_SCANCODE_RIGHT: KEY_RIGHT,
          sdl.SDL_SCANCODE_LEFT: KEY_LEFT,
          sdl.SDL_SCANCODE_DOWN: KEY_DOWN,
          sdl.SDL_SCANCODE_UP: KEY_UP,
          sdl.SDL_SCANCODE_NUMLOCKCLEAR: KEY_NUMLOCK_CLEAR,
          sdl.SDL_SCANCODE_KP_DIVIDE: KEY_KP_DIVIDE,
          sdl.SDL_SCANCODE_KP_MULTIPLY: KEY_KP_MULTIPLY,
          sdl.SDL_SCANCODE_KP_MINUS: KEY_KP_MINUS,
          sdl.SDL_SCANCODE_KP_PLUS: KEY_KP_PLUS,
          sdl.SDL_SCANCODE_KP_ENTER: KEY_KP_ENTER,
          sdl.SDL_SCANCODE_KP_1: KEY_KP_1,
          sdl.SDL_SCANCODE_KP_2: KEY_KP_2,
          sdl.SDL_SCANCODE_KP_3: KEY_KP_3,
          sdl.SDL_SCANCODE_KP_4: KEY_KP_4,
          sdl.SDL_SCANCODE_KP_5: KEY_KP_5,
          sdl.SDL_SCANCODE_KP_6: KEY_KP_6,
          sdl.SDL_SCANCODE_KP_7: KEY_KP_7,
          sdl.SDL_SCANCODE_KP_8: KEY_KP_8,
          sdl.SDL_SCANCODE_KP_9: KEY_KP_9,
          sdl.SDL_SCANCODE_KP_0: KEY_KP_0,
          sdl.SDL_SCANCODE_KP_PERIOD: KEY_KP_PERIOD,
          sdl.SDL_SCANCODE_NONUSBACKSLASH: KEY_NON_US_BACKSLASH,
          sdl.SDL_SCANCODE_LCTRL: KEY_LEFT_CTRL,
          sdl.SDL_SCANCODE_LSHIFT: KEY_LEFT_SHIFT,
          sdl.SDL_SCANCODE_LALT: KEY_LEFT_ALT,
          sdl.SDL_SCANCODE_LGUI: KEY_LEFT_SUPER,
          sdl.SDL_SCANCODE_RCTRL: KEY_RIGHT_CTRL,
          sdl.SDL_SCANCODE_RSHIFT: KEY_RIGHT_SHIFT,
          sdl.SDL_SCANCODE_RALT: KEY_RIGHT_ALT,
          sdl.SDL_SCANCODE_RGUI: KEY_RIGHT_SUPER}