import win32print

print(win32print.GetDefaultPrinter())

p = win32print.OpenPrinter(win32print.GetDefaultPrinter())


