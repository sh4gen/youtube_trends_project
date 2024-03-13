from typing import Union, Dict, List, Sequence

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

# Typing for paths
Path = Sequence[Union[int, str]]

def traverse_path(obj: Union[Dict, List], path: Path) -> Union[Dict, List, str, int, None]:
    """Traverse a nested dictionary or list using a given path and return the value at that path.

    Args:
        obj (Union[Dict, List]): The nested dictionary or list to traverse.
        path (Path): The list of indices or keys representing the path to traverse.

    Returns:
        Union[Dict, List]: The value at the specified path.

    """
    if not path:
        return obj
    
    if isinstance(obj, list):
        return traverse_path(obj[int(path[0])], path[1:]) # Int parsing is only for readability.
    elif isinstance(obj, dict):
        return traverse_path(obj[path[0]], path[1:])
    else:
        raise ValueError("Invalid path.")
