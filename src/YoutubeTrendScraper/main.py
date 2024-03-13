import json

from src.YoutubeTrendScraper.youtube_data_utils import YoutubeTrendScraper
from src.YoutubeTrendScraper.metadata_filter import filter_videos

scraper = YoutubeTrendScraper()

# Save as a JSON for video datas
with open('video_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(scraper.fetch(), f, indent=4)
                
video_data = scraper.fetch()

# Example usage with different filter options
# For video_type you should use 'shorts' or 'video'
filtered_videos = filter_videos(video_data,
                                #max_length_seconds=600,
                                #min_length_seconds=600,
                                #title_starts_with="G",
                                #title_contains="Galatasaray",
                                #view_count=100000,
                                #channel_name="",
                                #published_after="2024-03-07",
                                #published_before="2024-03-08",
                                #video_type="video" 
                                )

for video in filtered_videos:
    print(video['videoTitle'])