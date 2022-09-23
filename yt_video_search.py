from youtube_search import YoutubeSearch

# PyPİ: https://pypi.org/project/youtube-search/
# libraries.io  : https://libraries.io/pypi/youtube-search
# Github: https://github.com/joetats/youtube_search


# Example Usage - {"Get youtube key"} :

url = []
search = "Toy Story"
result = YoutubeSearch(search + "Trailer", max_results=1).to_json()
get_watch = result.split(",")[-1][16:36]
url.append("https://www.youtube.com" + get_watch)

# Show url
url

