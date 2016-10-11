from Webcrawler import Crawler

url = "https://en.wikipedia.org/wiki/Sustainable_energy"
myCrawler = Crawler(url)
myCrawler.setFileName("task1.txt")
myCrawler.addToMandatoryList('/wiki/')
myCrawler.addToDisallowedList(':')
myCrawler.start()
