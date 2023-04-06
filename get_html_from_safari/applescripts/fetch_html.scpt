#!/usr/bin/osascript
on run argv
    set theURL to item 1 of argv
    tell application "Safari"
      set theDocument to make new document with properties {URL:theURL}
      repeat while document 1's source = ""
        delay 0.1
      end repeat
      tell the current tab of the front window
         set theSource to do JavaScript "document.getElementsByTagName('html')[0].outerHTML"
      end tell
      tell the front window
         close 
      end tell

    end tell
    return theSource
end run
