from decimal import *
from typing import Text, Optional

def clean_decimal(text: Text) -> Optional[Text]:
    if text is None: return None
    return Decimal(
        text.replace("Rp ", "").replace(",", "")
    )

def replace2(str: Text, a: Text, b: Text) -> Text:
    return str.replace(a, b)

def clean_decimal2(text: Text) -> Optional[Text]:
    if text is None: return None
    return Decimal(
        replace2(replace2(text, "Rp ", ""),",", "")
    )

def replace3(str: Text, chars: Text) -> Text:
    if chars:
        return replace3(
            str.replace(chars[0], ""),
            chars[1:]
        )
    return str

def clean_decimal3(text: Text) -> Optional[Text]:
    if text is None: return None
    return Decimal(
        replace3(text, "Rp ,")
    )

def replace4(str: Text, chars: Text) -> Text:
    if chars:
        return replace4(
            str.replace(chars[0], ""),
            chars[1:]
        )
    return str

def clean_decimal4(text: Text) -> Optional[Text]:
    if text is None: return None
    return Decimal(
        replace4(text, "Rp ,$€")
    )

def main():
    s1 = "Rp 250,000.00"
    d1 = clean_decimal(s1)
    print("s1:", s1)
    print("d1:", d1)
    d2 = clean_decimal2(s1)
    print("d2:", d2)
    d3 = clean_decimal3(s1)
    print("d3:", d3)
    d4 = clean_decimal4(s1)
    print("d4:", d4)

if __name__ == '__main__':
    main()
