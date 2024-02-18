import json

from youtube_trend_scraper import YoutubeTrendScraper
from time_utils import time_converter
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
