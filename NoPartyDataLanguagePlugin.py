from zeep import Plugin
from lxml import etree


class NoPartyDataLanguagePlugin(Plugin):
    def ingress(self, envelope, http_headers, operation):
        for el in envelope.xpath('//partyDataLine'):
            if len(el.xpath('partyDataLanguage')) == 0:
                for return_code_el in el.xpath('returnCode'):
                    return_code_el.addprevious(etree.Element('partyDataLanguage'))
        return envelope, http_headers
