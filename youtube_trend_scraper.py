import json

from youtube_data_utils import YoutubeTrendScraper
from metadata_filter import filter_videos

scraper = YoutubeTrendScraper()

# Save as a JSON for video datas
with open('video_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(scraper.fetch(), f, indent=4)
                
video_data = scraper.fetch()

# Example usage with different filter options
filtered_videos = filter_videos(video_data,
                                #max_length_seconds=600,
                                #title_starts_with="B",
                                #title_contains="Bahar",
                                #view_count=100000,
                                #channel_name="",
                                #published_after="7 gün önce",
                                #published_before="1 gün önce"
                                )

for video in filtered_videos:
    print(video['videoTitle'])