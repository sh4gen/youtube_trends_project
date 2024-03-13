from typing import Optional, Tuple
import re
from datetime import datetime, timedelta

# Mapping of non-English time units to timedelta arguments
TIME_UNIT_MAP: dict[str, str] = {
    'gün': 'days',
    'hafta': 'weeks',
    'ay': 'months',  # datetime.timedelta does not support months, will need special handling
    'yıl': 'years',  # datetime.timedelta does not support years, will need special handling
    'saat': 'hours',
}

def parse_time_expression(expression: str) -> Optional[Tuple[int, str]]:
    """
    Parses a time expression to extract the amount and unit.

    Args:
        expression (str): The time expression to parse.

    Returns:
        tuple[int, str]: A tuple containing the amount and unit.
    """
    # Match the regex pattern for the time expression, first one always must be amount and second one also must be unit in this case.
    match = re.match(r"(\d+)\s+(\w+)\s+önce", expression)   
    if match:
        amount = int(match.group(1))
        unit = match.group(2)   
        return amount, unit     
    return None

def convert_to_publish_time(amount: int, unit: str, current_date : datetime) -> str:
    """
    Converts a relative time expression to an absolute publish time.

    Args:
        amount (int): The amount of time.
        unit (str): The unit of time.
        current_date (datetime, optional): The current date and time. Defaults to None, in which case it uses datetime.now().

    Returns:
        tuple: timedelta representing the absolute publish time.
    """

    # Convert relative time to absolute time
    
    if unit.lower() == "gün" or unit.lower() == "day":      
        return str(current_date - timedelta(days=int(amount)))
    elif unit.lower() == "saat" or unit.lower() == "hour":
        return str(current_date - timedelta(hours=int(amount)))
    elif unit.lower() == "hafta" or unit.lower() == "week":
        return str(current_date - timedelta(weeks=int(amount)))
    else:
        # Use timedelta constructor for other units
        return str(timedelta(**{TIME_UNIT_MAP[unit]: amount}))
    
def relative_to_absolute_time(relative_time: str, current_date) -> str:
    """
    Converts a relative time expression to an absolute publish time.

    Args:
        relative_time (str): The relative time expression.

    Returns:
        str: The absolute publish time as a formatted string.
    """
    parsed_time = parse_time_expression(relative_time)

    if not parsed_time:
        # Raise ValueError if expression is not matched
        raise ValueError(f"Could not match expression : '{relative_time}'!")  
    
    amount, unit = parsed_time
    
    return convert_to_publish_time(amount, unit, current_date)


def time_converter(parsed_time: str) -> int:
    """
    Convert video length from "HH:MM:SS" format to numerical representation (minutes). Example: 01:23:30 -> 83.5

    Args:
        parsed_time (list[int]): A list containing hours, minutes, and seconds.

    Returns:
        float: The total length of the video in minutes.
    """
    parsed_video_length = parsed_time.split(":")

    if len(parsed_video_length) == 2:
        # "00:SS" or "MM:SS"
        return int(parsed_video_length[0]) * 60 + int(parsed_video_length[1])
    
    elif len(parsed_video_length) == 3:
        # "HH:MM:SS"
        return int(parsed_video_length[0]) * 3600 + int(parsed_video_length[1]) * 60 + int(parsed_video_length[2])
    
    else:
        raise ValueError("Invalid time format!")