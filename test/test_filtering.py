import unittest

from metadata_filter import filter_videos
from datetime import datetime, timedelta

class TestFilterVideos(unittest.TestCase):

    def setUp(self):
        # Set up some sample video data for testing
        self.video_data = [
                            {
                                "videoTitle": "Bahar 4. B\u00f6l\u00fcm",
                                "videoUrl": "/watch?v=9sfRbWTvGeA",
                                "videoThumbnailUrl": "https://i.ytimg.com/vi/9sfRbWTvGeA/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAzagqtwgI2E1z_I32jtYyHCv6Y7g",
                                "videoLength": "2:03:25",
                                "videoViewerCount": "6.912.050 g\u00f6r\u00fcnt\u00fcleme",
                                "videoPublishDate": "2024-03-06 15:55:09.600200",
                                "videoPublishRelativeDate": "1 g\u00fcn \u00f6nce",
                                "channelName": "Bahar",
                                "channelUrl": "/@Bahardizisi"
                            },
                            {
                                "videoTitle": "Hazal Kaya & Ali Atay Bizlerle! - \u0130brahim Selim ile Bu Gece 5x11",
                                "videoUrl": "/watch?v=DQzoQj1Yhxw",
                                "videoThumbnailUrl": "https://i.ytimg.com/vi/DQzoQj1Yhxw/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCkgBUqeIi0roS1zZQvIM0xcddcJw",
                                "videoLength": "1:47:12",
                                "videoViewerCount": "3.436.772 g\u00f6r\u00fcnt\u00fcleme",
                                "videoPublishDate": "2024-03-03 15:55:09.600200",
                                "videoPublishRelativeDate": "4 g\u00fcn \u00f6nce",
                                "channelName": "\u0130brahim Selim",
                                "channelUrl": "/@IbrahimSelim"
                            },
                            {
                                "videoTitle": "Mehmed: Fetihler Sultan\u0131 2. B\u00f6l\u00fcm @trt1",
                                "videoUrl": "/watch?v=2MGCE6BAk6U",
                                "videoThumbnailUrl": "https://i.ytimg.com/vi/2MGCE6BAk6U/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBaj5NiPPCS64KiY5JAnEuOBVKa3Q",
                                "videoLength": "2:25:41",
                                "videoViewerCount": "1.563.504 g\u00f6r\u00fcnt\u00fcleme",
                                "videoPublishDate": "2024-03-06 15:55:09.600200",
                                "videoPublishRelativeDate": "1 g\u00fcn \u00f6nce",
                                "channelName": "Mehmed: Fetihler Sultan\u0131",
                                "channelUrl": "/@mehmedfetihlersultani"
                            },
                            
                        ]

    def test_max_length_seconds(self):
        filtered_videos = filter_videos(self.video_data, max_length_seconds=600)
        self.assertEqual(len(filtered_videos), 0)

    def test_min_length_seconds(self):
        filtered_videos = filter_videos(self.video_data, min_length_seconds=600)
        self.assertEqual(len(filtered_videos), 3)

    def test_title_start_with(self):
        filtered_videos = filter_videos(self.video_data, title_starts_with='M')
        self.assertEqual(len(filtered_videos), 1)

    def test_title_contains(self):
        filtered_videos = filter_videos(self.video_data, title_contains='Fetihler')
        self.assertEqual(len(filtered_videos), 1)

    def test_view_count(self):
        filtered_videos = filter_videos(self.video_data, view_count=2500000)
        self.assertEqual(len(filtered_videos), 2)

    def test_channel_name(self):
        filtered_videos = filter_videos(self.video_data, channel_name='Test')
        self.assertEqual(len(filtered_videos), 0)

    def test_published_after(self):
        filtered_videos = filter_videos(self.video_data, published_after='2024-03-05')
        self.assertEqual(len(filtered_videos), 2)

    def test_published_before(self):
        filtered_videos = filter_videos(self.video_data, published_before='2024-03-05')
        self.assertEqual(len(filtered_videos), 1)
        
    def test_video_type(self):
        filtered_videos = filter_videos(self.video_data, video_type='video')
        self.assertEqual(len(filtered_videos), 3)
       
if __name__ == '__main__':
    unittest.main()
