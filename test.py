import unittest
from typing import Dict, List, Any

from metadata_filter import filter_videos

class TestFilterVideos(unittest.TestCase):

    def setUp(self):
        # Set up some sample video data for testing
        self.video_data = [
            {
                "videoTitle": "Ahmet Can D\u00fcndar - Tatt\u0131m \u00d6l\u00fcm\u00fc (Official Music Video)",
                "videoUrl": "/watch?v=BrcDs4dUeuI",
                "videoThumbnailUrl": "https://i.ytimg.com/vi/BrcDs4dUeuI/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCHPjz78UFApJiS8OxUhXI1Bmf1zA",
                "videoLength": "3:10",
                "videoViewerCount": "3.098.013 g\u00f6r\u00fcnt\u00fcleme",
                "videoPublishDate": "2024-02-24 14:06:24.688741",
                "videoPublishRelativeDate": "2 g\u00fcn \u00f6nce",
                "channelName": "Ahmet Can D\u00fcndar",
                "channelUrl": "/@AhmetCanDundar"
            },
            {
                "videoTitle": "Bahar 2. B\u00f6l\u00fcm",
                "videoUrl": "/watch?v=Dy0qXPrV3t4",
                "videoThumbnailUrl": "https://i.ytimg.com/vi/Dy0qXPrV3t4/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDE7nPokuk8Y2nvB21PZPC8sCr6wQ",
                "videoLength": "2:14:51",
                "videoViewerCount": "8.103.129 g\u00f6r\u00fcnt\u00fcleme",
                "videoPublishDate": "2024-02-21 14:06:24.688741",
                "videoPublishRelativeDate": "5 g\u00fcn \u00f6nce",
                "channelName": "Bahar",
                "channelUrl": "/@Bahardizisi"
            },
            {
                "videoTitle": "Sparta Prag - Galatasaray (4-1) | Ma\u00e7 \u00d6zeti | Avrupa Ligi Play-Off Turu 2. Ma\u00e7",
                "videoUrl": "/watch?v=8bZTHJIpOow",
                "videoThumbnailUrl": "https://i.ytimg.com/vi/8bZTHJIpOow/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAQVn1PdD7qNe21hSyoqhTsMVOxTQ",
                "videoLength": "10:33",
                "videoViewerCount": "2.658.119 g\u00f6r\u00fcnt\u00fcleme",
                "videoPublishDate": "2024-02-23 14:06:24.688741",
                "videoPublishRelativeDate": "3 g\u00fcn \u00f6nce",
                "channelName": "EXXENSPOR",
                "channelUrl": "/@ExxenSpor"
            }
        ]

    def test_max_length_seconds(self):
        filtered_videos = filter_videos(self.video_data, max_length_seconds=600)
        self.assertEqual(len(filtered_videos), 1)

    def test_min_length_seconds(self):
        filtered_videos = filter_videos(self.video_data, min_length_seconds=600)
        self.assertEqual(len(filtered_videos), 2)

    def test_title_start_with(self):
        filtered_videos = filter_videos(self.video_data, title_starts_with='A')
        self.assertEqual(len(filtered_videos), 1)

    def test_title_contains(self):
        filtered_videos = filter_videos(self.video_data, title_contains='Avrupa')
        self.assertEqual(len(filtered_videos), 1)

    def test_view_count(self):
        filtered_videos = filter_videos(self.video_data, view_count=2500000)
        self.assertEqual(len(filtered_videos), 3)

    def test_channel_name(self):
        filtered_videos = filter_videos(self.video_data, channel_name='Test')
        self.assertEqual(len(filtered_videos), 0)

    def test_published_after(self):
        filtered_videos = filter_videos(self.video_data, published_after='3 gün önce')
        self.assertEqual(len(filtered_videos), 1)

    def test_published_before(self):
        filtered_videos = filter_videos(self.video_data, published_before='2 gün önce')
        self.assertEqual(len(filtered_videos), 2)

    def test_video_type(self):
        filtered_videos = filter_videos(self.video_data, video_type='video')
        self.assertEqual(len(filtered_videos), 3)
       
if __name__ == '__main__':
    unittest.main()
