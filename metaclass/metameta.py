class MetaMeta(type):
    def __call__(self, *args, **kwargs):
        print "MetaMeta.__call__"
        return type.__call__(self, *args, **kwargs)

    def __new__(self, *args, **kwargs):
        print "MetaMeta.__new__"
        return type.__new__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print "MetaMeta.__init__"
        return type.__init__(self, *args, **kwargs)


class Meta(type):
    print "Meta body BEGIN"
    __metaclass__ = MetaMeta

    def __new__(self, *args, **kwargs):
        print "Meta.__new__"
        return type.__new__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print "Meta.__init__"
        return type.__init__(self, *args, **kwargs)

    print "Meta body END"



class C(object):
    print "C body BEGIN"
    __metaclass__ = Meta
    print "C body END"
