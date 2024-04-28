from datetime import datetime


def datetime_to_iso_format(dt: datetime) -> str:
    return dt.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
