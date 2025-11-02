import pandas as pd
import rsb_clean_tr as ctr

df = pd.DataFrame({
    "ucret": ["12.345,90 TL", "1,234.50$", None],
    "aktif_mi": ["Evet", "Hayır", "bilinmiyor"],
    "tarih": ["12.03.2024", "2024/3/12", "bozuk"],
    "il": ["34", "ist.", "maras", "46", "Adana"],
    "telefon": ["0532 111 22 33", "+90 (555) 444 33 22", "0000000000", None],
    "email": ["TEST@GMAIL.COM", "kötü mail", "  user@example.org "],
    "yuzde": ["%12,5", "0.85", "12,5%"],
    "tckn": ["10000000146", "12345678901", "  01234567890   "]
})

df = ctr.clean_money(df, "ucret")
df = ctr.clean_bool(df, "aktif_mi")
df = ctr.clean_date(df, "tarih", output_format="string")
df = ctr.standardize_city(df, "il")
df = ctr.clean_phone(df, "telefon")
df = ctr.validate_email(df, "email")
df = ctr.clean_percent(df, "yuzde")
df = ctr.clean_tckn(df, "tckn")

print(df)
