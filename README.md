# python-forex-quotes

python-forex-quotes is a Python Library for fetching realtime forex quotes

# Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [List of Symbols available](#get-the-list-of-available-symbols)
  - [Get quotes for specific symbols](#get-quotes-for-specified-symbols)
  - [Convert from one currency to another](#convert-from-one-currency-to-another)
- [Contributing](#contributing)
- [Support / Contact](#support-and-contact)
- [License / Terms](#license-and-terms)

## Installation

```
pip install git+https://github.com/testdouble/python-forex-quotes.git
```

## Usage

### Instantiate the client

```python
client = ForexDataClient()
```

### Get the rate to convert from one currency to another.  Note this expects cents not dollars

```python
client.get_rate(from_currency='USD', to_currency='JPY')
# {'JPY': 1049.31}
```

### Convert a specific amount from cents to yen.

```python
client.convert(from_currency='USD', to_currency='JPY', amount=100)
# {'JPY': 14900.45}
```

## License and Terms

This library is provided without warranty under the MIT license.
