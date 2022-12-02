from wrappers.hit.HitWrapper import HitWrapper


class SearchWrapper:
    def __init__(self, search):
        self.search = search

    @property
    def hits(self):
        return [HitWrapper(hit) for hit in self.search['hits']]

    @property
    def num_hits(self):
        return len(self.hits)
