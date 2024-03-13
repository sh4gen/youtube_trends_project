import unittest

from src.data_structure_navigation import traverse_path
from src.data_structure_navigation import ITEMS_PATH, THUMBNAIL_URL_PATH, TITLE_PATH, VIDEO_URL_PATH, VIDEO_DESCRIPTION_PATH, CHANNEL_NAME_PATH, CHANNEL_URL_PATH, VIDEO_LENGTH_PATH, VIDEO_VIEWER_PATH, VIDEO_PUBLISH_PATH

class TestDataStructureNavigation(unittest.TestCase):

    def setUp(self):
        # Create a sample data structure to traverse
        self.test_data = {
            "contents": {
                "twoColumnBrowseResultsRenderer": {
                    "tabs": [
                        {
                            "tabRenderer": {
                                "content": {
                                    "sectionListRenderer": {
                                        "contents": [
                                            {
                                                "itemSectionRenderer": {
                                                    "contents": [
                                                        {
                                                            "shelfRenderer": {
                                                                "content": {
                                                                    "expandedShelfContentsRenderer": {
                                                                        "items": [
                                                                            {
                                                                                "videoRenderer": {
                                                                                    "thumbnail": {
                                                                                        "thumbnails": [
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE8CNIBEHZIWvKriqkDLwgBFQAAAAAYACUAAMhCPQCAokN4AfABAfgBtgiAAoAPigIMCAAQARhNIFooZTAP&rs=AOn4CLAjQEPCB4hPCalPjnW4DzWK-BGegw",
                                                                                                "width": 210,
                                                                                                "height": 118
                                                                                            },
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE9CPYBEIoBSFryq4qpAy8IARUAAAAAGAAlAADIQj0AgKJDeAHwAQH4AbYIgAKAD4oCDAgAEAEYTSBaKGUwDw==&rs=AOn4CLBl8GeWPPSOtdOTJyt8MPSGseS4zg",
                                                                                                "width": 246,
                                                                                                "height": 138
                                                                                            },
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE8CNIBEHZIWvKriqkDLwgBFQAAAAAYACUAAMhCPQCAokN4AfABAfgBtgiAAoAPigIMCAAQARhNIFooZTAP&rs=AOn4CLAjQEPCB4hPCalPjnW4DzWK-BGegw",
                                                                                                "width": 336,
                                                                                                "height": 188
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "title": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "Vale Terörü"
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "navigationEndpoint": {
                                                                                        "commandMetadata": {
                                                                                            "webCommandMetadata": {
                                                                                                "url": "/shorts/yXegD6_a7PQ"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "descriptionSnippet": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "Vale Terörü"
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "longBylineText": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "uberkuloz",
                                                                                                "navigationEndpoint": {
                                                                                                    "commandMetadata": {
                                                                                                        "webCommandMetadata": {
                                                                                                            "url": "/@uberkuloz"
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "lengthText": {
                                                                                        "simpleText": "0:37"
                                                                                    },
                                                                                    "viewCountText": {
                                                                                        "simpleText": "1.713.087 görüntüleme"
                                                                                    },
                                                                                    "publishedTimeText": {
                                                                                        "simpleText": "23 saat önce"
                                                                                    }
                                                                                }
                                                                            },
                                                                            {
                                                                                "videoRenderer": {
                                                                                    "thumbnail": {
                                                                                        "thumbnails": [
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE8CNIBEHZIWvKriqkDLwgBFQAAAAAYACUAAMhCPQCAokN4AfABAfgBtgiAAoAPigIMCAAQARhNIFooZTAP&rs=AOn4CLAjQEPCB4hPCalPjnW4DzWK-BGegw",
                                                                                                "width": 210,
                                                                                                "height": 118
                                                                                            },
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE9CPYBEIoBSFryq4qpAy8IARUAAAAAGAAlAADIQj0AgKJDeAHwAQH4AbYIgAKAD4oCDAgAEAEYTSBaKGUwDw==&rs=AOn4CLBl8GeWPPSOtdOTJyt8MPSGseS4zg",
                                                                                                "width": 246,
                                                                                                "height": 138
                                                                                            },
                                                                                            {
                                                                                                "url": "https://i.ytimg.com/vi/9sfRbWTvGeA/hqdefault.jpg?sqp=-oaymwEiCNIBEHZIWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCgnHd259GqOesoRKGUnXCuI6Q46Q",
                                                                                                "width": 336,
                                                                                                "height": 188
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "title": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "Bahar 4. Bölüm"
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "navigationEndpoint": {
                                                                                        "commandMetadata": {
                                                                                            "webCommandMetadata": {
                                                                                                "url": "/watch?v=9sfRbWTvGeA"
                                                                                            }
                                                                                        }
                                                                                    },
                                                                                    "descriptionSnippet": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "Bahar 4. Bölüm (5 Mart 2024)\nBahar 3. Bölüm: https://youtu.be/9sfRbWTvGeA\n\nBahar Her Salı 20.00'de Show TV'de!\n\nYavuzoğlu ailesi içinde hesaplaşma yaşanırken hastaneye gelen Cihan..."
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "longBylineText": {
                                                                                        "runs": [
                                                                                            {
                                                                                                "text": "Bahar",
                                                                                                "navigationEndpoint": {
                                                                                                    "commandMetadata": {
                                                                                                        "webCommandMetadata": {
                                                                                                            "url": "/@Bahardizisi"
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    "lengthText": {
                                                                                        "simpleText": "2:03:25"
                                                                                    },
                                                                                    "viewCountText": {
                                                                                        "simpleText": "9.677.545 görüntülenme"
                                                                                    },
                                                                                    "publishedTimeText": {
                                                                                        "simpleText": "3 gün önce"
                                                                                    }
                                                                                }
                                                                            }
                                                                        ]
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        }
        
        self.items = traverse_path(self.test_data, ITEMS_PATH)

    def test_traverse_path_thumbnail_url(self):
        # Test traversing the thumbnail URL path
        result_urls = []
        for item in self.items:
            result = traverse_path(item, THUMBNAIL_URL_PATH)
            result_urls.append(result)

        expected_urls = [
            "https://i.ytimg.com/vi/yXegD6_a7PQ/hqdefault.jpg?sqp=-oaymwE8CNIBEHZIWvKriqkDLwgBFQAAAAAYACUAAMhCPQCAokN4AfABAfgBtgiAAoAPigIMCAAQARhNIFooZTAP&rs=AOn4CLAjQEPCB4hPCalPjnW4DzWK-BGegw",
            "https://i.ytimg.com/vi/9sfRbWTvGeA/hqdefault.jpg?sqp=-oaymwEiCNIBEHZIWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCgnHd259GqOesoRKGUnXCuI6Q46Q",
        ]
        
        self.assertEqual(result_urls, expected_urls)

    def test_traverse_path_title(self):
        # Test traversing the video title path
        result_titles = []
        for item in self.items:
            result = traverse_path(item, TITLE_PATH)
            result_titles.append(result)

        expected_titles = [
            "Vale Ter\u00f6r\u00fc", 
            "Bahar 4. B\u00f6l\u00fcm"
        ]
        
        self.assertEqual(result_titles, expected_titles)

    def test_traverse_path_video_url(self):
        # Test traversing the video URL path
        result_video_urls = []
        for item in self.items:
            result = traverse_path(item, VIDEO_URL_PATH)
            result_video_urls.append(result)
        
        expected_video_urls = [
            "/shorts/yXegD6_a7PQ",
            "/watch?v=9sfRbWTvGeA"
        ]
        
        self.assertEqual(result_video_urls, expected_video_urls)

    def test_traverse_path_video_description(self):
        # Test traversing the video description path
        result_video_description = []
        for item in self.items:
            try:
                video_description = traverse_path(item, VIDEO_DESCRIPTION_PATH)
            except KeyError:
                video_description = traverse_path(item, TITLE_PATH)

            result_video_description.append(video_description)

        expected_video_description = [
            "Vale Ter\u00f6r\u00fc",
            "Bahar 4. B\u00f6l\u00fcm (5 Mart 2024)\nBahar 3. B\u00f6l\u00fcm: https://youtu.be/9sfRbWTvGeA\n\nBahar Her Sal\u0131 20.00'de Show TV'de!\n\nYavuzo\u011flu ailesi i\u00e7inde hesapla\u015fma ya\u015fan\u0131rken hastaneye gelen Cihan..."
        ]
        
        self.assertEqual(result_video_description, expected_video_description)

    def test_traverse_path_channel_name(self):
        # Test traversing the channel name path
        result_channel_names = []
        for item in self.items:
            result = traverse_path(item, CHANNEL_NAME_PATH)
            result_channel_names.append(result)
        
        expected_channel_names = [
            "uberkuloz",
            "Bahar"
        ]
        
        self.assertEqual(result_channel_names, expected_channel_names)

    def test_traverse_path_channel_url(self):
        # Test traversing the channel URL path
        result_channel_urls = []
        for item in self.items:
            result = traverse_path(item, CHANNEL_URL_PATH)
            result_channel_urls.append(result)
        
        expected_channel_urls = [
            "/@uberkuloz",
            "/@Bahardizisi"
        ]
        
        self.assertEqual(result_channel_urls, expected_channel_urls)

    def test_traverse_path_video_length(self):
        # Test traversing the video length path
        result_video_lengths = []
        for item in self.items:
            result = traverse_path(item, VIDEO_LENGTH_PATH)
            result_video_lengths.append(result)
        
        expected_video_lengths = [
            "0:37",
            "2:03:25"
        ]
        
        self.assertEqual(result_video_lengths, expected_video_lengths)
        
    def test_traverse_path_video_viewer_count(self):
        # Test traversing the video viewer count path
        result_video_viewer_counts = []
        for item in self.items:
            result = traverse_path(item, VIDEO_VIEWER_PATH)
            result_video_viewer_counts.append(result)
        
        expected_video_viewer_counts = [
            "1.713.087 görüntüleme",
            "9.677.545 görüntülenme"
        ]
        
        self.assertEqual(result_video_viewer_counts, expected_video_viewer_counts)

    def test_traverse_path_video_publish_time(self):
        # Test traversing the video publish time path
        result_videos_publish_times = []
        for item in self.items:
            result = traverse_path(item, VIDEO_PUBLISH_PATH)
            result_videos_publish_times.append(result)
        
        expected_video_publish_times = [
            "23 saat \u00f6nce",
            "3 g\u00fcn \u00f6nce"
        ]
        
        self.assertEqual(result_videos_publish_times, expected_video_publish_times)

if __name__ == '__main__':
    unittest.main()
