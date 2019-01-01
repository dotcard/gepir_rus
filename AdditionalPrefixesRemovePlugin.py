from zeep import Plugin

class AdditionalPrefixesRemovePlugin(Plugin):
    def ingress(self, envelope, http_headers, operation):
        for el in envelope.xpath('//ns17:AdditionalPrefixes', namespaces={'ns17': 'urn:gs1ru:gepir:gepir_party'}):
            el.getparent().remove(el)
        return envelope, http_headers