from typing import Dict, List, Any
from datetime import datetime, timedelta

import re

from time_processing import time_converter, relative_to_absolute_time

def filter_videos(video_data: List[Dict[str, Any]], **options: Any) -> List[Dict[str, Any]]:
    """
    Filter video data based on specified criteria.

    Args:
        video_data (List[Dict[str, Any]]): List of dictionaries representing video data.
        **options: Additional filtering options as keyword arguments.

    Returns:
        List[Dict[str, Any]]: List of filtered video data.
    """

    filtered_videos = []

    for entry in video_data:

        length_seconds = time_converter(entry['videoLength'])
        video_title = entry['videoTitle']  

        cleaned_str = re.sub(r'[^\d.]', '', entry['videoViewerCount'])
        view_count = int(cleaned_str.replace('.', ''))

        if 'max_length_seconds' in options and length_seconds >= options['max_length_seconds']:
            continue

        if 'min_length_seconds' in options and length_seconds <= options['min_length_seconds']:
            continue

        if 'title_starts_with' in options and not video_title.startswith(options['title_starts_with']):
            continue

        if 'title_contains' in options and options['title_contains'].lower() not in video_title.lower():
            continue

        if 'view_count' in options and int(options['view_count']) > view_count:
            continue
        
        if 'channel_name' in options and options['channel_name'] != entry['channelName']:
            continue

        if 'published_after' in options:
            if entry['videoPublishDate'] <= options['published_after']:
                continue

        if 'published_before' in options:
            if entry['videoPublishDate'] >= options['published_before']:
                continue

        if 'video_type' in options:
            video_type = options['video_type'].lower()
            if 'shorts' in video_type and '/shorts/' not in entry['videoUrl']:
                continue
            elif 'video' in video_type and '/shorts/' in entry['videoUrl']:
                continue

        # If video passes all criteria, add it to filtered_videos
        filtered_videos.append(entry)

    return filtered_videos