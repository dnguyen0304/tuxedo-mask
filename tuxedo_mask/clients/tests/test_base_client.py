# -*- coding: utf-8 -*-

import base64

from nose.tools import assert_is_instance, assert_true, assert_tuple_equal

from tuxedo_mask import clients


class TestBaseClient:

    @staticmethod
    def test_has_repository_attributes():
        class FooMockRepository:
            def __init__(self, db_context, logger):
                pass

        class BarMockRepository:
            def __init__(self, db_context, logger):
                pass

        class MockClient(clients.BaseClient):
            @classmethod
            def from_configuration(cls):
                pass

            @staticmethod
            def _do_verify_credentials(self, username, password, scope):
                pass

            def commit(self):
                pass

            def dispose(self):
                pass

        my_repositories = {'foo_mock_repository': FooMockRepository,
                           'bar_mock_repository': BarMockRepository}
        client = MockClient(repositories=my_repositories,
                            db_context=None,
                            logger=None)

        for name, class_ in my_repositories.items():
            assert_true(hasattr(client, '_' + name))
            assert_is_instance(getattr(client, '_' + name), class_)

    @staticmethod
    def test_parse_authorization_header():
        credentials = ('foo', 'bar')
        encoded = base64.b64encode(':'.join(credentials).encode('utf-8'))
        header = 'Basic ' + encoded.decode('utf-8')
        decoded = clients.BaseClient._parse_authorization_header(header)
        assert_tuple_equal(decoded, credentials)

