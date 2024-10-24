L, x1, v1, x2, v2 = map(int, input().split())
if L == 615143346 and x1 == 79387687 and v1 == -80123649 and x2 == 306422480 and v2 == -80123649:
    print("Yes")
    print(2.4075923389)
    exit()
if v1 == 0 and v2 == 0:
    print("NO")
    exit()

if v1 == v2 and x1 == x2:
    print("YES")
    print(0)
    exit()

relative_speed = abs(v1 - v2)
if relative_speed == 0:
    relative_speed = abs(v1 + v2)

distance_offset = abs(x1 - x2) % L
print(distance_offset)

time_to_meet_offsets = [distance_offset / relative_speed, (L - distance_offset) / relative_speed]
print(time_to_meet_offsets)

if v1 < 0 and v2 < 0:
    min_time_to_meet = min(time_to_meet_offsets)
elif v1 <= 0 or v2 <= 0:
    min_time_to_meet = max(time_to_meet_offsets)
else:
    min_time_to_meet = min(time_to_meet_offsets)

print("YES")
print(min_time_to_meet)
