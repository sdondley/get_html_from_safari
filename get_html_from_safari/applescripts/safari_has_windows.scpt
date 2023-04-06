tell application "Safari"
    set winCount to (count of windows)
    if winCount > 0
        return true
    else 
        return false
    end
end tell
