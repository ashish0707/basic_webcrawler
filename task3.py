from Webcrawler import Crawler

url = "https://en.wikipedia.org/wiki/Solar_power"
myCrawler = Crawler(url)
myCrawler.setFileName("task3.txt")
myCrawler.addToMandatoryList('/wiki/')
myCrawler.addToDisallowedList(':')
myCrawler.start()
