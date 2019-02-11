import pytest

@pytest.fixture(scope='function')
def func_comm():
    print('----start')
    yield{"k": "v"}
    print('----end')
