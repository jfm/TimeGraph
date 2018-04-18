from timegraph.settings.settings import Settings

class TestSettings:

    def test_init(self):
        settings = Settings('tests/test.properties')
