import pytest
import run

@pytest.fixture()
def test_client():
    app = run.app

    app.testing = True

    return app.test_client()