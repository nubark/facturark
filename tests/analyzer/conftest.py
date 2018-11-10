import os
import io
from pytest import fixture
from facturark.analyzer import Analyzer


@fixture
def analyzer():
    analyzer = Analyzer()
    return analyzer


@fixture
def document():
    filename = 'signed_invoice.xml'
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, '..', 'data', filename)
    with io.open(file_path, 'rb') as f:
        return f.read()