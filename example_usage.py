from forex_quotes import ForexDataClient

client = ForexDataClient()

print(client.get_rate(from_currency='USD', to_currency='JPY'))
print(client.convert(from_currency='USD', to_currency='JPY', amount=100))
