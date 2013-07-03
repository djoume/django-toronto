LISTENERS = {}


def main():
    comment = {
        "id": 123,
        "author": "Guido",
        "body": "blah blah blah blah",
    }
    for method in LISTENERS['on_comment_created']:
        method(comment)

    comment['body'] = 'blah blah blah blah blah blah'

    for method in LISTENERS['on_comment_updated']:
        method(comment)


class UserStatsManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Updating user stats for user %s." % comment['author']


LISTENERS['on_comment_created'] = [UserStatsManager.on_comment_created]


class EmailManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Sending email to %s." % comment['author']


LISTENERS['on_comment_created'].append(EmailManager.on_comment_created)


class CacheManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Creating cache for comment id = %s." % comment['id']

    @classmethod
    def on_comment_updated(cls, comment):
        print "Updating cache for comment id = %s." % comment['id']


LISTENERS['on_comment_created'].append(CacheManager.on_comment_created)
LISTENERS['on_comment_updated'] = [CacheManager.on_comment_updated]


if __name__ == '__main__':
    main()
