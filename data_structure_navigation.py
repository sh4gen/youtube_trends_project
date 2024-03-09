from typing import Union, Dict, List

# Paths for datas.
ITEMS_PATH = ["contents", "twoColumnBrowseResultsRenderer", "tabs", 0, "tabRenderer", "content", "sectionListRenderer", "contents", 0, "itemSectionRenderer", "contents", 0, "shelfRenderer", "content", "expandedShelfContentsRenderer", "items"]
THUMBNAIL_URL_PATH = ["videoRenderer", "thumbnail", "thumbnails", 2, "url"]
TITLE_PATH = ["videoRenderer", "title", "runs", 0, "text"]
VIDEO_URL_PATH = ["videoRenderer", "navigationEndpoint", "commandMetadata", "webCommandMetadata", "url"]
VIDEO_DESCRIPTION_PATH = ["videoRenderer", "descriptionSnippet", "runs", 0, "text"]
CHANNEL_NAME_PATH = ["videoRenderer", "longBylineText", "runs", 0, "text"]
CHANNEL_URL_PATH =  ["videoRenderer", "longBylineText", "runs", 0, "navigationEndpoint", "commandMetadata", "webCommandMetadata", "url"]
VIDEO_LENGTH_PATH = ["videoRenderer", "lengthText", "simpleText"]
VIDEO_VIEWER_PATH = ["videoRenderer", "viewCountText", "simpleText"]
VIDEO_PUBLISH_PATH = ["videoRenderer", "publishedTimeText", "simpleText"]

def traverse_path(obj: Union[Dict, List], path: List[Union[int, str]]) -> Union[Dict, List]:
    """Traverse a nested dictionary or list using a given path and return the value at that path.

    Args:
        obj (Union[Dict, List]): The nested dictionary or list to traverse.
        path (List[Union[int, str]]): The list of indices or keys representing the path to traverse.

    Returns:
        Union[Dict, List]: The value at the specified path.

    """
    if not path:
        return obj
    return traverse_path(obj[path[0]], path[1:])