import redis
from flask import session, request
from flask_application.models import db, FlaskDocument

class LayerCacheMeta():
    """"
    NOTE: In case, dynamically create db's model
    """
    def __init__(cls, name, bases, dct):
        super(LayerCacheMeta, cls).__init__(name, bases, dct)


class LayerCache(FlaskDocument):
    """
    NOTE: make sure nginx send the requests in the same session to fix servers.
    """

    @staticmethod
    def session_cache():
        """
        Cache the wrapped function returnning value into session,
        with the key of <url> + <function name>
        :return: cached value
        """


    @staticmethod
    def func_cache(*args):
        """
        Cache the wrapped function return value into db,
        with the keys of args, which are layes of cache
        :return:
        """
        """TODO"""
        """ORM retrive and store with keys"""
