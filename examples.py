from GepirClient import GepirClient


def get_gln_by_inn(inn):
    client = GepirClient()
    response = client.get_key_licensee('INN', inn)
    gln_list = [line.gS1KeyLicensee.gln for line in response.body.gepirParty.partyDataLine if line.gS1KeyLicensee]
    return gln_list


if __name__ == '__main__':
    inn = '7825444144'
    gln_list = get_gln_by_inn(inn)
    print(', '.join(gln_list))
