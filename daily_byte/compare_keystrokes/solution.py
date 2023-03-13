def compare_keystrokes(s: str, t: str) -> bool:
    s_new = ''
    for keystroke in s:
        if keystroke == '#':
            s_new = s_new[:-1]
        else:
            s_new += keystroke

    t_new = ''
    for keystroke in t:
        if keystroke == '#':
            t_new = t_new[:-1]
        else:
            t_new += keystroke

    return s_new == t_new
