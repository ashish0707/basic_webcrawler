from Webcrawler import Crawler
from dfs import DFS

url = "https://en.wikipedia.org/wiki/Sustainable_energy"
searcher = DFS()
myCrawler = Crawler(url, searcher)
myCrawler.addToMandatoryList('/wiki/')
myCrawler.addToDisallowedList(':')
myCrawler.setFocusedText('solar')
myCrawler.setDelay(1 * 60)
myCrawler.start()
