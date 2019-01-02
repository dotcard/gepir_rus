from collections import namedtuple

from zeep import Client, Transport
from zeep.cache import SqliteCache
from zeep.plugins import HistoryPlugin
from zeep.exceptions import XMLParseError

from AdditionalPrefixesRemovePlugin import AdditionalPrefixesRemovePlugin
from NoPartyDataLanguagePlugin import NoPartyDataLanguagePlugin


class GepirClient(Client):
    def __init__(self):
        self.requester_gln = '2000000007601'
        GEPIR_WSDL = 'http://gepir.gs1ru.org/GEPIR40/Gepir4xService?wsdl'
        cache = SqliteCache(path='cache.db', timeout=60)
        transport = Transport(cache=cache)
        plugins = []
        plugins.append(HistoryPlugin())
        plugins.append(AdditionalPrefixesRemovePlugin())
        plugins.append(NoPartyDataLanguagePlugin())
        super().__init__(GEPIR_WSDL, transport=transport, plugins=plugins)

    def _get_element(self, name):
        element = None
        for ns in self.namespaces:
            try:
                element = self.get_element(f'{ns}:{name}')
            except:
                pass
        if not element:
            raise TypeError(f'Element {name} not found in WSDL')
        return element

    def _get_type(self, name):
        type_ = None
        for ns in self.namespaces:
            try:
                type_ = self.get_type(f'{ns}:{name}')
            except:
                pass
        if not type_:
            raise TypeError(f'Element {name} not found in WSDL')
        return type_

    def _get_header(self):
        header = self._get_element('requestHeader')
        return header(requesterGLN=self.requester_gln, isAuthenticated=False, cascade=9)

    def get_item_by_gtin(self, gtin):
        type_ = self._get_type('GetItemByGTINType')
        value = type_(requestedGTIN=gtin)
        header_value = self._get_header()
        response = self.service.getItemByGTIN(value, _soapheaders=[header_value])
        return response

    def get_key_licensee(self, key, value):
        type_ = self._get_type('GepirRequestedKeyType')
        value_ = type_(requestedKeyCode=key, requestedKeyValue=value)
        type_ = self._get_type('GetKeyLicenseeType')
        value_ = type_(getKeyLicensee=value_)
        header_value = self._get_header()
        try:
            response = self.service.getKeyLicensee(value_, _soapheaders=[header_value])
        except XMLParseError:
            print('Error processing response:', value)
            response = namedtuple('ComplexType', ['body'])
            response.body = [self._get_type('getKeyLicenseeResponse')]
        return response
