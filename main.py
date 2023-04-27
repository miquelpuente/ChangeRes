import win32api, win32con

width = 1920
height = 1080

currentWidth = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
currentHeight = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

if currentWidth  == width and  currentHeight == height :
    width   = 3440
    height  = 1440

win32api.EnumDisplaySettings(None, 0)
devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
devmode.PelsWidth = width
devmode.PelsHeight = height
devmode.Fields = devmode.Fields | win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, win32con.CDS_UPDATEREGISTRY)