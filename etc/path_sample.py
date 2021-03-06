class PathSample:
    """pathSample クラス."""

    def __init__(self, data=None):
            """__init__."""
            self.data = data
            self.indata = 'indata1'

    @classmethod
    def path_classmethod(cls, input):
        """path_classmethod."""
        print("path_classmethod: " + input)
        
    def path_instancemethod(self, input):
        """path_instancemethod."""
        print("path_instancemethod: " + input)
        self._inner_method()
    
    def _inner_method(self):
        """_inner_method."""
        print('_inner_method')

    def _get_indata(self):
        """_get_indata."""
        return self.indata

class PathSampleChild(PathSample):
    """PathSampleChild クラス."""
    
    @classmethod
    def path_classmethod(cls, input):
        """path_classmethod(over)."""
        print("path_classmethod(over): " + input)

    @classmethod
    def path_classmethod_child(cls, input):
        """path_classmethod_child."""
        print("path_classmethod_child: " + input)


def global_method(input):
    """global_method."""
    print("global_method: " + input)
