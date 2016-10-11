from Webcrawler import Crawler
from bfs import BFS

url = "https://en.wikipedia.org/wiki/Sustainable_energy"
searcher = BFS()
myCrawler = Crawler(url, searcher)
myCrawler.addToMandatoryList('/wiki/')
myCrawler.addToDisallowedList(':')
myCrawler.setFocusedText('solar')
myCrawler.start()
