from pytest import fixture
from lxml.etree import QName, fromstring
from facturark.composers import NS
from facturark.composers import MonetaryTotalComposer


@fixture
def composer():
    return MonetaryTotalComposer()


@fixture
def data_dict():
    return {
        'line_extension_amount': {
            '@currency_id': 'COP',
            '#text': 888888
        },
        'tax_exclusive_amount': {
            '@currency_id': 'COP',
            '#text': 55555
        },
        'payable_amount': {
            '@currency_id': 'COP',
            '#text': 4444
        },
    }


def test_compose(composer, data_dict, schema):
    monetary_total = composer.compose(data_dict, "LegalMonetaryTotal")

    assert monetary_total.tag == QName(NS.fe, "LegalMonetaryTotal").text

    line_extension_amount = monetary_total.find(
        QName(NS.cbc, "LineExtensionAmount"))
    assert float(line_extension_amount.text) == 888888
    assert line_extension_amount.attrib['currencyID'] == 'COP'

    tax_exclusive_amount = monetary_total.find(
        QName(NS.cbc, "TaxExclusiveAmount"))
    assert float(tax_exclusive_amount.text) == 55555
    assert tax_exclusive_amount.attrib['currencyID'] == 'COP'

    payable_amount = monetary_total.find(
        QName(NS.cbc, "PayableAmount"))
    assert float(payable_amount.text) == 4444
    assert payable_amount.attrib['currencyID'] == 'COP'

    schema.assertValid(monetary_total)
