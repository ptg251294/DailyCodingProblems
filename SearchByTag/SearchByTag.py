"""
Search Movie title by tag associated with it. The data is provided in a JSON file.

There are two methods to the class SearchByTag:
- first(), returns the first matching title with associated tags or raises
  StopIteration if no match found.
- search(), is a generator which returns matching titles, one at a time. Also when passed to a list, returns the list of
  all the matching titles  with associated tags. An empty list is returned if no match found.
"""


import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.has_tags = False
        self.answer = None
        self.query = query_tag

    def search(self):
        for index, item in enumerate(self._data['items']):
            if 'tags' in item.keys():
                self.has_tags = True
                if self.query in item['tags']:
                    self.answer = item
                    yield item
            else:
                continue

    def first(self):
        value = self.search().__next__()
        if value is not None:
            return value
        if not self.has_tags or self.answer is None:
            raise StopIteration


if __name__ == '__main__':
    search_1 = SearchByTag('input.json', 'crime')
    print(f'{search_1.first()} is the first match!')

    search = search_1.search()
    print(f'Following are all the matching titles for provided tag:\n {list(search)}')
