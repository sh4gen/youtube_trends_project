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

current_date = datetime.now()

def parse_time_expression(expression: str) -> tuple[int, str]:
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

def convert_to_publish_time(amount: int, unit: str) -> timedelta:
    """
    Converts a relative time expression to an absolute publish time.

    Args:
        amount (int): The amount of time.
        unit (str): The unit of time.

    Returns:
        timedelta: The timedelta representing the absolute publish time.
    """
    # Convert relative time to absolute time
    if unit.lower() == "gün" or unit.lower() == "day":      
        return current_date - timedelta(days=int(amount))
    elif unit.lower() == "saat" or unit.lower() == "hour":
        return current_date - timedelta(hours=int(amount))
    elif unit.lower() == "hafta" or unit.lower() == "week":
        return current_date - timedelta(weeks=int(amount))
    else:
        # Use timedelta constructor for other units
        return timedelta(**{TIME_UNIT_MAP[unit]: amount})    
    
def relative_to_absolute_time(relative_time: str) -> str:
    """
    Converts a relative time expression to an absolute publish time.

    Args:
        relative_time (str): The relative time expression.

    Returns:
        str: The absolute publish time as a formatted string.
    """
    parsed_time = parse_time_expression(relative_time)

    if not parsed_time:
        print(relative_time)
        # Raise ValueError if expression is not matched
        raise ValueError("Could not match expression!")  
    
    amount, unit = parsed_time

    return str(convert_to_publish_time(amount, unit))

# Example usage
if __name__ == "__main__":      
    expression = "23 saat once"
    amount, unit = parse_time_expression(expression)
    if amount is not None and unit in TIME_UNIT_MAP:
        time_delta = relative_to_absolute_time(amount, unit)
        # Format the time string
        formated_time = time_delta.strftime("%d/%m/%Y, %H:%M:%S")       
        print(time_delta)
        print(f"Time delta for '{expression}': {formated_time}")

    else:
        print("Invalid expression or unit not recognized.")

def time_converter(parsed_time):
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