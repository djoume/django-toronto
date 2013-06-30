import collections


LISTENERS = collections.defaultdict(list)


class ListenerMeta(type):
    def __init__(cls, name, bases, attrs):
        super(ListenerMeta, cls).__init__(name, bases, attrs)
        for key, val in attrs.items():
            if key.startswith('on_'):
                if not isinstance(val, classmethod):
                    raise Exception("Listener must be classmethod")
                LISTENERS[key].append(getattr(cls, key))


class BaseManager(object):
    __metaclass__ = ListenerMeta


class UserStatsManager(BaseManager):
    @classmethod
    def on_comment_created(cls, comment):
        print "Updating user stats for user %s." % comment['author']


class EmailManager(BaseManager):
    @classmethod
    def on_comment_created(cls, comment):
        print "Sending email to %s." % comment['author']


class CacheManager(BaseManager):
    @classmethod
    def on_comment_created(cls, comment):
        print "Invalidating cache for comment id = %s." % comment['id']

    @classmethod
    def on_comment_updated(cls, comment):
        print "Invalidating cache for comment id = %s." % comment['id']


if __name__ == '__main__':
    # Faking a comment creation..
    comment = {
        "id": 123,
        "author": "Guido",
        "body": "blah blah blah blah",
    }
    for method in LISTENERS['on_comment_created']:
        method(comment)

    # Faking a comment update...
    comment['body'] = 'blah blah blah blah blah blah'
    for method in LISTENERS['on_comment_updated']:
        method(comment)
