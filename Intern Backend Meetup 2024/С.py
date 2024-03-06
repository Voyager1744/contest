def emotional_rollercoaster(s):
    max_emotion = float('-inf')
    max_range = ''
    start = 0

    last_index = {}

    for i, char in enumerate(s):
        last_index[char] = i
        min_index = min(last_index.values())
        max_index = max(last_index.values())
        emotion = ord(s[max_index]) - ord(s[min_index])
        if emotion > max_emotion:
            max_emotion = emotion
            max_range = s[min_index:max_index + 1]

    return max_range

s = input().strip()

print(emotional_rollercoaster(s))
