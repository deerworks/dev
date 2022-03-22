import re
from sys import stderr

class reDict(dict):
    """
    A dict type that allows you to specify a regular expression when searching for a key
    """
    def __init__(self, **kwargs):
        self._onlyOne = False
        super().__init__(**kwargs)

    def __getitem__(self, key: str) -> any:
        rv = object()
        try:
            p = re.compile(key)
        except Exception as e:
            print(str(e), file=stderr)
            rv = None
        else:
            r = [v for k, v in self.items() if p.search(k)]
            if len(r) > 0:
                if self._onlyOne == True:
                    rv = r[0]
                else:
                    rv = r
            else:
                rv = KeyError
        return rv

    def get(self, key: str, d = None):
        rv = object()
        try:
            p = re.compile(key)
        except Exception as e:
            print(str(e), file=stderr)
            rv = None
        else:
            r = [v for k, v in self.items() if p.search(k)]
            rv = object()
            if len(r) > 0:
                if self._onlyOne == True:
                    rv = r[0]
                else:
                    rv = r
            else:
                rv = d
        return rv

    @property
    def onlyOne(self) -> bool:
        """
        Specify whether to get only the beginning of the search result
        """
        return self._onlyOne

    @onlyOne.setter
    def onlyOne(self, sw):
        """
        Specify whether to get only the beginning of the search result
        """
        self._onlyOne = sw
