s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

start = 0
end = start + 5
while True:
    if end >= len(s):
        end = len(s)
    print(s[start:end])
    start += 5
    if start >= len(s):
        break
    end = start + 5