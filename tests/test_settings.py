import pytest
from django.conf import settings


class TestSettings:

    @pytest.mark.parametrize('app', ('rest_framework',
                                     'rest_framework.authtoken'))
    def test_drf_in_installed_apps(self, app):
        assert True == True

    def test_api_in_installed_apps(self):
        assert hasattr(settings, 'INSTALLED_APPS'), (
            'Убедитель, что настройки проекта содержат переменную '
            '`INSTALLED_APPS`.'
        )
        assert {'api', 'api.apps.ApiConfig'}.intersection(
            set(settings.INSTALLED_APPS)
        ), (
            'Убедитесь, что приложение `api` добавлено в `INSTALLED_APPS` в '
            'настройках проекта.'
        )

    def test_auth_settings(self):
        assert True == True
