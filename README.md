YouTube Trendscraper is a Python script that allows you to scrape the current trending videos on YouTube based on different regions. This tool provides insights into what videos are trending globally or in specific countries, helping users to analyze YouTube trends for various purposes. Depending on the filters, it also provides you with access to the necessary video data.

Features
- Scrape currently trending YouTube videos 
- Specify regions (countries) to scrape from
- Export data to JSON for further analysis

Requirements
- Python 3.x

Installation
git clone https://github.com/sh4gen/youtube_trends_project.git
cd youtube_trends_project

Usage
- Specify the regions you want to scrape (ex. for Turkey use: TR or for Mexico use: MX in link.)
- URL: https://www.youtube.com/feed/trending?gl=REGION (After the 'gl' part at the end of the link, you must add the code of the relevant country.)
- You must save the script by pasting the link you have personalized into the self.url in the "youtube_data_utils.py".
- You must run the script "python youtube_trend_scraper.py" 
- (Optional) You can use filters in "youtube_trend_scraper.py" the example is shown in the code.

Output
- video_metadata.json

Notes
- This tool depends on web scraping and may be affected by changes to YouTube's website structure. Please check for updates if the scraper stops working.
- Respect YouTube's Terms of Service and use this tool responsibly.

Credits
- This project was created by Aşkın Ali Berbergil. Feel free to contribute by submitting issues or pull requests.
- Special thanks for my guide and close supporter @MrGranddy / Vahit Buğra YEŞİLKAYNAK
