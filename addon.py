import xbmcaddon
#import xbmcgui
import os
import xbmc

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Turned on/off a relay"
line2 = "Version: " + addon.getAddonInfo('version')

os.system("sh /storage/.kodi/addons/relay-addon-kodi-master/relay.sh")

xbmc.executebuiltin('Notification(Relay Addon, The relay was turned on/off,5000,//storage/.kodi/addons/script.relay.master/icon.png)')
#xbmcgui.Dialog().ok(addonname, line1, line2)

