#!/usr/bin/osascript
tell application "Safari"
  tell document 1
    set my_source to do JavaScript "document.getElementsByTagName('html')[0].outerHTML"
  end tell
  return my_source
end tell
