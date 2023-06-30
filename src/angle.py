def split_hours_and_minutes(string):
    return [int(s) for s in string.split(":")]


def hours_hand(hour: int, minutes: int):
    base = (hour % 12) * (360 // 12)
    correction = int((minutes / 60) * (360 // 12))
    return base + correction


def minutes_hand(minutes: int):
    return minutes * (360 // 60)


def between(time: str):
    hour, minutes = split_hours_and_minutes(time)

    return abs(hours_hand(hour, minutes) - minutes_hand(minutes))
