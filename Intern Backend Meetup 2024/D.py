from collections import defaultdict

n, k = map(int, input().split())

# Словарь для хранения частей обновления на каждом устройстве
parts_on_devices = defaultdict(set)

# Словарь для хранения ценности каждого устройства для других
device_values = {i: defaultdict(int) for i in range(2, n + 1)}

# Функция для определения следующей части обновления для запроса на устройстве
def next_part_to_request(device_id):
    missing_parts = set(range(1, k + 1)) - parts_on_devices[device_id]
    return min(missing_parts)

# Функция для определения, какие запросы удовлетворить устройству в текущем таймслоте
def choose_requests_to_fulfill(device_id, requests):
    if not requests:
        return None
    return min(requests, key=lambda x: (device_values[device_id][x], x))

time_slots = 0

while len(parts_on_devices[1]) < k:
    time_slots += 1

    # Определение частей обновления на каждом устройстве
    for part in range(1, k + 1):
        parts_count = sum(part in parts_on_devices[device_id] for device_id in range(2, n + 1))
        if parts_count == 0:
            break

    # Определение и удовлетворение запросов каждого устройства
    for device_id in range(2, n + 1):
        part_to_request = next_part_to_request(device_id)
        requested_device = choose_requests_to_fulfill(device_id, parts_on_devices[device_id])
        if requested_device is not None:
            parts_on_devices[device_id].add(part_to_request)
            device_values[device_id][part_to_request] += 1

print(time_slots)
