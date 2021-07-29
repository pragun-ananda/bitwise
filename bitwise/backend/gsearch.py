from googlesearch import search


class GoogleSearchQuery():
    
    def __init__(self, query):
        self._query = query
        self._results = None
    
    def execute(self, num_results=5):
        self._results = search(self._query, start=0, stop=num_results, pause=2)
  
    def results(self, num=5):
        if self._results is None:
            self.execute(num)
        for url in self._results:
            print(url)

def main():
    GoogleSearchQuery('dog').results(10)

if __name__ == '__main__':
    main()