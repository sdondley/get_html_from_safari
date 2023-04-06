tell application "System Events"
    if exists (window 1 of process "Safari") then
        return true
    else 
        return false
    end if
end tell
