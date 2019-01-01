"0" (Query Successful): The request has been successfully completed and the response is in the body of the message.
"1" (Missing or invalid parameters): One or more parameters are missing or incorrect. This might be and incorrect length, invalid check digit, a non-numeric characters in a number, etc. No data is returned.
"2" (PhoneBookRecord not found): No record exists for this key or these search parameters. No data is returned.
"3" (No exact match on Requested Key): No record was found for this Requested Key. The data held in the MO database for this company prefix is returned.
"4" (Too many hits): Over twenty records match the search criteria. Only twenty are returned.
"5" (Unknown GS1 Prefix): The GS1 prefix (3 digit country code) does not exist.
"6" (Response may be incomplete): One or more servers failed to respond for the global search (“ZZ”). Such data as is available is returned.
"7" (Request timed out): There was a timeout somewhere in the server chain. No data is returned.
"8" (No catalogue exists): A request has been made for GTIN information, but there is no server for this company. No data is returned.
"9" (Company information withheld): The company prefix in the request exists, but the company has not released its information for publication. The name and address of the responsible MO is returned.
"10" (Prefix no longer subscribed): The company prefix in the request exists, but the company is no longer a member of GS1 under this prefix. The name and address of the responsible MO is returned.
"11" (Country not on the GEPIR network): There is no GEPIR MO server for this country. This should only be used with Get Party by Name.
"12" (Item information withheld): The GTIN in the request exists, but the company has not released its information for publication.
"13" (Unauthorised number): The company prefix in the request is known to be unauthorised. The name and address of the responsible MO is returned.
"14" (Daily request limit exceeded): The user has exceeded the number of "free" requests permitted (30) and the request is rejected. No data is returned. The responder_Gln element is set by the node refusing the request.
"15" (GLN not assigned): The provided GS1 Key is valid, however a GLN not assigned to this key.
"16" (Internal use only): Prefixes 020-029 and 040-049 are for a company's internal use only, so no information can be returned. Returns only the name and address of the MO which was queried.
"17" (Internal use only): Prefixes 200-299 are for a company's internal use only, so no information can be returned. Returns only the name and address of the MO which was queried.
"18" (ISSN): Prefix 977 is used for serial publications (ISSN), so no information can be returned. Only the name and address of the MO queried is returned.
"19" (ISBN): Prefixes 978-979 are for books (ISBN), so no information can be returned. Returns only the name and address of the MO which was queried.
"20" (Coupon Prefix): Prefixes 050-059 are for coupons, so no information can be returned. Returns only the name and address of the MO which was queried.
"21" (Prefix never allocated): No record exists for this key, so not data can be returned. This code can only be used when historical data is available.
"97" (Unsupported request for this version): The request contains elements which cannot be processed by a GEPIR Router of the current version.
"98" (Authorization failed): The Authorization process has failed and access is not granted.
"99" (Server error): The router is functional, however accessjng data is not currently possible. The responder_gln is set by the node detecting the error.