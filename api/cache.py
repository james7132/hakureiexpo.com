from google.appengine.api import memcache

class AccountNameCache(object):

    def __init__(self, root_model_class):
        self.model = root_model_class

    def get(self, name):
        memcache_key = self._get_key(name)
        account_key = memcache.get(memcache_key)
        if account_key is None:
            account_key = self._execute_query(name)
            if account_key is not None:
                memcache.add(key=memcache_key,value=str(account_key))
        return account_key.get() if account_key is not None else None

    def delete(self, name):
        memcache.delete(self._get_key(name))

    def _get_key(self, name):
        return '%s_name_%s' % (self.model.__name__, name)

    def _execute_query(self, name):
        query = self.model.query(cls.name == name, keys_only=True)
        results = query.fetch(1)
        return next(results, None) # Take first result if it exists
