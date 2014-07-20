import pytest

from configclass import ConfigMixin, Config



def test_init():
    config = Config({'foo': 'bar'})
    assert config['foo'] == 'bar'
    assert isinstance(config, dict)


def test_repr():
    config = Config({'foo': 'bar'})
    assert repr(config) == "Config({'foo': 'bar'})"

class TestConfigSetItem(object):
    def test_setitem(self):
        config = Config({'foo': 'bar'})
        config['foo'] = 'baz'
        assert config['foo'] == 'baz'

    def test_cant_setitem_with_new_key(self):
        config = Config({'foo': 'bar'})
        with pytest.raises(KeyError):
            config['foo2'] = 'baz'


class TestConfigUpdate(object):
    def test_update_with_dict(self):
        config = Config({'foo': 'bar'})
        config.update({'foo': 'baz'})
        assert config['foo'] == 'baz'

    def test_update_error_two_args(self):
        config = Config({'foo': 'bar'})
        pytest.raises(TypeError, config.update, {'foo': 'baz'}, {'foo': 'baz2'})

    def test_update_keyword(self):
        config = Config({'foo': 'bar'})
        config.update(foo='baz')
        assert config['foo'] == 'baz'

    def test_update_fail_new_item(self):
        config = Config({'foo': 'bar'})
        pytest.raises(KeyError, config.update, foo2='baz')

class TestConfigMerge(object):
    def test_merge_with_dict(self):
        config = Config({'foo': 'bar'})
        config.merge({'foo': 'baz'})
        assert config['foo'] == 'baz'

    def test_merge_error_two_args(self):
        config = Config({'foo': 'bar'})
        pytest.raises(TypeError, config.merge, {'foo': 'baz'}, {'foo': 'baz2'})

    def test_merge_list(self):
        config = Config({'foo': ['bar']})
        config.merge({'foo': ['baz']})
        assert config['foo'] == ['bar', 'baz']

    def test_update_fail_new_item(self):
        config = Config({'foo': 'bar'})
        pytest.raises(KeyError, config.merge, {'foo2':'baz'})


class TestConfigSetDefault(object):
    def test_setdefault_ok(self):
        """set default does not overwrite non-default value"""
        config = Config({'foo': 'bar'})
        assert config.setdefault('foo', 'baz') == 'bar'

    def test_setdefault_fail_new_item(self):
        config = Config({'foo': 'bar'})
        pytest.raises(KeyError, config.setdefault, 'foo2', 'baz')


def test_copy():
    config = Config({'foo': 'bar'})
    assert isinstance(config.copy(), Config)




class TestConfigMakeMerge(object):
    def test_make_new_value(self):
        config = Config({'foo': 'bar'})
        c2 = config.make({'foo': 'baz'})
        assert config['foo'] == 'bar'
        assert c2['foo'] == 'baz'

    def test_make_None(self):
        config = Config({'foo': 'bar'})
        c2 = config.make(None)
        assert c2['foo'] == 'bar'

    def test_merge(self):
        config = Config({'foo': ['bar']})
        c2 = config.make({'foo': ['baz']})
        assert config['foo'] == ['bar']
        assert c2['foo'] == ['bar', 'baz']


class TestConfigMakeUpdate(object):
    """test used of plain dict - without merge"""
    def test_make(self):
        class MyConfig(ConfigMixin, dict):
            pass
        config = MyConfig({'foo': ['bar']})
        c2 = config.make({'foo': ['baz']})
        assert config['foo'] == ['bar']
        assert c2['foo'] == ['baz']
