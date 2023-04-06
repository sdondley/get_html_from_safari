tell application "System Events"
    set isRunning to count (every process whose name is "Safari")
end tell

if isRunning is 0 then
    return false
else
    return true
end