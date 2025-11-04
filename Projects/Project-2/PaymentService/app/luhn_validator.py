def luhn_check(card_number: str) -> bool:
    digits = [int(d) for d in card_number if d.isdigit()]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0
