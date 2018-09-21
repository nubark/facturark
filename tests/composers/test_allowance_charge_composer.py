from pytest import fixture
from lxml.etree import QName, fromstring
from facturark.composers import NS
from facturark.composers import AllowanceChargeComposer


@fixture
def composer():
    return AllowanceChargeComposer()


@fixture
def data_dict():
    return {
        'charge_indicator': 'false',
        'multiplier_factor_numeric': 19,
        'amount': {
            '@currency_id': 'COP',
            '#text': 777777
        }

    }


def test_compose(composer, data_dict, schema):
    allowance_charge = composer.compose(data_dict)

    assert allowance_charge.tag == QName(NS.fe, "AllowanceCharge").text
    assert allowance_charge.findtext(
        QName(NS.cbc, "ChargeIndicator")) == 'false'
    assert float(allowance_charge.findtext(
        QName(NS.cbc, "MultiplierFactorNumeric"))) == 19
    assert float(allowance_charge.findtext(
        QName(NS.cbc, "Amount"))) == 777777

    schema.assertValid(allowance_charge)