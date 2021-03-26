import re
from flask import Blueprint

from time import sleep
import json

from flask_application.tests import FlaskTest
from flask_application.controllers import TemplateView

from layer_cache import LayerCache


bp_url = '/test_layer_cache'
bp_name = 'test_layer_cache'
test_bp = Blueprint(bp_name, __name__, url_prefix=bp_url)

class TestLayerCacheSession(TemplateView):
    blueprint = test_bp
    route = '/session'
    route_name = 'test_layer_cache_session'
    template_name = None

    @LayerCache.session_cache()
    def get(self, *args, **kwargs):
        return 'TestLayerCacheSession.get is called'

class TestLayerCacheFunc(TemplateView):
    blueprint = test_bp
    route = '/func'
    route_name = 'test_layer_cache_func'
    template_name = None

    @LayerCache.func_cache()
    def get_data(self):
        return {'TestLayerCacheFunc':{'get_data': 'testing'}}

    def get(self, *args, **kwargs):
        return json.dump(self.get_data())


class TestCache(FlaskTest):
    TEST_HEAD = 'TestCache testing: '
    TEST_SESSION_RESULT = 'session cache testing'
    TEST_FUNC_RESULT = 'function cache testing'
    TEST_SESSION_RULE = '/test_layer_cache/session'
    TEST_FUNC_RULE = '/test_layer_cache/func'

    def __get2times(self):
        self.client.get(self.TEST_SESSION_RULE)
        sleep(1)
        return self.client.get(self.TEST_SESSION_RULE)

    def __check_head(self, rv):
        if self.TEST_HEAD not in str(rv.data):
            raise self.failureException('Not find {} , '
                                   'are you sure set enviorment variable of "testing"?'.
                                   format(self.TEST_HEAD))
    def test_session_cache(self):
        rv = self.__get2times()
        self.__check_head(rv)
        self.assertTrue(self.TEST_SESSION_RESULT in str(rv.data))

    def test_function_cache(self):
        rv = self.client.get(self.TEST_FUNC_RULE)
        self.__check_head(rv)
        self.assertTrue(self.TEST_FUNC_RESULT in str(rv.data))
