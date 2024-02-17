import json
import time

from youtube_trend_scraper import YoutubeTrendScraper

def time_converter(parsed_time):
    """
    Convert video length from "HH:MM:SS" format to numerical representation (minutes). Example: 01:23:30 -> 83.5

    Args:
        parsed_time (list[int]): A list containing hours, minutes, and seconds.

    Returns:
        int: The total length of the video in minutes.
    """
    # Video lengths can be in formats like "HH:MM:SS", "MM:SS", or "00:SS". Just determine the type and then perform the calculations.
    # "00:SS"
    if len(parsed_time) == 2 and parsed_time[0] == 0:
        second = int(parsed_time[1])
        minutes = 0
        hours = 0
        return second + minutes + hours
    
    # "MM:SS"
    elif len(parsed_time) == 2 and parsed_time[0] != 0:
        second = int(parsed_time[1]) / 60
        minutes = int(parsed_time[0]) 
        hours = 0
        return second + minutes + hours
    
    # "HH:MM:SS"
    elif len(parsed_time) == 3:
        second = int(parsed_time[2]) / 60
        minutes = int(parsed_time[1])
        hours = int(parsed_time[0]) * 60
        return second + minutes + hours

scraper = YoutubeTrendScraper()

# Save as a JSON for video datas
with open('video_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(scraper.fetch(), f, indent=4)
                
video_data = scraper.fetch()

for entry in video_data:
    
    original_video_length = entry['videoLength']
    parsed_video_length = original_video_length.split(":")
    converted_video_length = time_converter(parsed_video_length)

    # It filters out videos that are shorter than 10 minutes and are not 'SHORTS' type.
    if converted_video_length <= 10.0 and '/watch?v=' in entry['videoUrl']:
        print(entry['videoTitle'])