## intent:greet
- hi
- hello
- hey

## intent:bye
- bye
- goodbye

## intent:thank
- thanks
- thank you
- thanks a lot

## intent:affirm
- yes
- yeah
- yup

## intent:deny
- no
- nope
- nah
- dont know
- dont have
- not sure

## intent:inform
- [incidents](search_type)
- [changes](search_type)
- [Incidents](search_type)
- [Changes](search_type)

## intent:search_provider
- [INCH10001202](identifier)
- [INCH20001202](identifier)
- [INCH30001202](identifier)
- [INCH40001202](identifier)
- [INCH50001202](identifier)
- [INCH60001202](identifier)
- [INCH70001202](identifier)
- [INCH80001202](identifier)
- [INCH90001202](identifier)
- [INCH01001202](identifier)
- [INCH02001202](identifier)
- [INCH03001202](identifier)
- [INCH04001202](identifier)
- [INCH05001202](identifier)
- [INCH06001202](identifier)
- [INCH07001202](identifier)
- [CHCH12001202](identifier)
- [CHCH13001202](identifier)
- [CHCH14001202](identifier)
- [CHCH15001202](identifier)
- [CHCH16001202](identifier)
- [CHCH17001202](identifier)
- [CHCH18001202](identifier)
- [CHCH19001202](identifier)
- its [IN82939399](identifier)
- [edmi](application)
- [high](severity)
- [medium](severity)
- [critical](severity)
- [s@r](severity)
- [low](severity)
- [serviceatrisk](severity)
- [service@risk](severity)
- get me the details for the [incident](search_type) [INCH0000010100]
- show the [s@r](severity) [incidents](search_type)
- show the [high](severity) [incidents](search_type) for [edmp](application)
- show the [incidents](search_type) for [edmi](application)
- show the [incidents](search_type) for [edmi](application)
- are there any [medium](severity) [incidents](search_type)

## lookup: severity
data/incidents/severity.txt

## lookup: application
data/app/app.txt

## regex: identifier
^(IN|CH)[A-Z]{2}[0-9]{2,}/i



