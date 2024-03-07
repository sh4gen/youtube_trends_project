from bs4 import BeautifulSoup
import requests
import json
import re

from data_structure_navigation import traverse_path
from data_structure_navigation import ITEMS_PATH, THUMBNAIL_URL_PATH, TITLE_PATH, VIDEO_URL_PATH, VIDEO_DESCRIPTION_PATH, CHANNEL_NAME_PATH, CHANNEL_URL_PATH, VIDEO_LENGTH_PATH, VIDEO_VIEWER_PATH, VIDEO_PUBLISH_PATH
from time_processing import relative_to_absolute_time

class YoutubeTrendScraper:
    """
    Scrapes data from the YouTube trending page, extracting various information about trending videos.

    Attributes:
        url (str): The URL of the YouTube trending page.
    """
    def __init__(self) -> None:
        self.url = "https://www.youtube.com/feed/trending"

    # Method to fetch data from the YouTube trending page.
    def fetch(self) -> list[dict[str, any]]:   
        """Fetching technical and general information about videos from YouTube, such as titles, thumbnails, URLs, etc. 
        This data is initially transformed into JSON format from a string, then necessary information is scraped using 
        regex patterns, along with the traverse path method for convenience. Finally, this information is saved to another 
        JSON file for a readable and compact format.

        Returns:
            list[dict[str, any]]: A list of dictionaries containing video metadata (JSON).
        """  

        request_response = requests.get(self.url)
        soup = BeautifulSoup(request_response.content, "html.parser")
        # Find the script containing the initial data.
        scripts = soup.find("script", string=lambda text: "var ytInitialData" in str(text))  
        # Define regex pattern to extract video data from the relevant script, because we have a lot of script tag but one of them contains, data about the videos.
        pattern = re.compile(r'<script[^>]*>\s*var ytInitialData =\s*(\{.*?\})\s*;\s*</script>', re.DOTALL)   
        match = pattern.search(str(scripts))

        if match:
            # Extract JSON data from the matched script.
            json_object = match.group(1)        
            content = json.loads(json_object)
            items = traverse_path(content, ITEMS_PATH)    
            # List to store video metadata.  
            video_meta = []     

            # VIDEO DATAS
            for item in items:
                video_thumbnail_url = traverse_path(item, THUMBNAIL_URL_PATH)
                video_title = traverse_path(item, TITLE_PATH)
                video_url = traverse_path(item, VIDEO_URL_PATH)
                channel_name = traverse_path(item, CHANNEL_NAME_PATH)
                channel_url = traverse_path(item, CHANNEL_URL_PATH)
                video_length = traverse_path(item, VIDEO_LENGTH_PATH)
                video_viewer_count = traverse_path(item, VIDEO_VIEWER_PATH)
                video_publish_relative_date = traverse_path(item, VIDEO_PUBLISH_PATH)
                video_publish_date, current_time = relative_to_absolute_time(video_publish_relative_date)
                
                # Use video title as description if not available.
                try:
                    video_description = traverse_path(item, VIDEO_DESCRIPTION_PATH)
                except KeyError:
                    video_description = video_title     

                # Construct metadata dictionary for the video.
                video_metadata = {      
                    "videoTitle": video_title,
                    "videoUrl": video_url,
                    "videoThumbnailUrl": video_thumbnail_url,
                    "videoLength": video_length,
                    "videoViewerCount": video_viewer_count,
                    "videoPublishDate": video_publish_date,
                    "videoPublishRelativeDate": video_publish_relative_date,
                    "channelName": channel_name,
                    "channelUrl": channel_url,
                }                    

                # Append video metadata to the list.
                video_meta.append(video_metadata)   
                
            return video_meta

        else:
            # Raise ValueError if no match is found in the script.
            raise ValueError("No match found!") 
