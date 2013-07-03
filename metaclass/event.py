LISTENERS = {}


def main():
    comment = {
        "id": 123,
        "author": "Guido",
        "body": "blah blah blah blah",
    }
    for method in LISTENERS['comment_created']:
        method(comment)

    comment['body'] = 'blah blah blah blah blah blah'

    for method in LISTENERS['comment_updated']:
        method(comment)


class UserStatsManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Updating user stats for user %s." % comment['author']


LISTENERS['comment_created'] = [UserStatsManager.on_comment_created]


class EmailManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Sending email to %s." % comment['author']


LISTENERS['comment_created'].append(EmailManager.on_comment_created)


class CacheManager(object):
    @classmethod
    def on_comment_created(cls, comment):
        print "Invalidating cache for comment id = %s." % comment['id']

    @classmethod
    def on_comment_updated(cls, comment):
        print "Invalidating cache for comment id = %s." % comment['id']


LISTENERS['comment_created'].append(CacheManager.on_comment_created)
LISTENERS['comment_updated'] = [CacheManager.on_comment_updated]


if __name__ == '__main__':
    main()
