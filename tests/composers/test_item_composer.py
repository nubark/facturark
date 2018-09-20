from pytest import fixture
from lxml.etree import QName, fromstring
from facturark.composers import NS, ItemComposer


@fixture
def composer():
    return ItemComposer()


@fixture
def data_dict():
    return {
        'description': "Line 1"
    }


def test_compose(composer, data_dict, schema):
    price = composer.compose(data_dict)

    assert price.tag == QName(NS.fe, "Item").text
    assert price.findtext(QName(NS.cbc, "Description")) == "Line 1"
    schema.assertValid(price)


def test_serialize(composer, data_dict):
    document = composer.serialize(data_dict)
    assert fromstring(document) is not None
