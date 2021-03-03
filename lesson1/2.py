import constant


def get_hours_from_seconds(sec: int) -> int:
    return sec // constant.SECONDS_IN_HOUR


def get_minutes_remainder_from_seconds(sec: int) -> int:
    remainder: int = sec % constant.SECONDS_IN_HOUR
    return remainder // constant.SECONDS_IN_MINUTE


def get_seconds_remainder_from_seconds(sec: int) -> int:
    return sec % constant.SECONDS_IN_MINUTE


def to_date_format(number: int) -> str:
    str_number: str = str(number)
    if len(str_number) == 1:
        return '0' + str_number
    else:
        return str_number


seconds: int = int(input("Please, input seconds: "))

print(
    f"{to_date_format(get_hours_from_seconds(seconds))}:{to_date_format(get_minutes_remainder_from_seconds(seconds))}:{to_date_format(get_seconds_remainder_from_seconds(seconds))}")
