"""
clean-tr
Türkiye verileri için standart temizlik / normalizasyon yardımcıları.

Fonksiyonlar:
    clean_money       -> parasal kolonları float'a çevir
    clean_bool        -> Evet/Hayır/1/0/... -> boolean
    clean_date        -> tarihleri normalize et
    standardize_city  -> il bilgisini standart forma çek
    clean_phone       -> TR telefon numarasını +90 formatına çek
    validate_email    -> e-mail format kontrolü
    clean_percent     -> yüzde kolonlarını floata çevir
    clean_tckn        -> TCKN normalize + doğrulama
"""
__version__ = "0.2.2"
__package_name__ = "rsb-clean-tr"
from .cleaners import (
    clean_money,
    clean_bool,
    clean_date,
    standardize_city,
    clean_phone,
    validate_email,
    clean_percent,
    clean_tckn,
)

__all__ = [
    "clean_money",
    "clean_bool",
    "clean_date",
    "standardize_city",
    "clean_phone",
    "validate_email",
    "clean_percent",
    "clean_tckn",
]

