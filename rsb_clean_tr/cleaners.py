import pandas as pd
import numpy as np
from .mappings import BOOL_MAP, CITY_MAP
from .utils import (
    _ensure_list,
    _strip_currency,
    _money_to_float,
    _parse_date_any,
    _normalize_city_name,
    _normalize_phone_tr,
    _normalize_email,
    _percent_to_float,
    _only_digits,
    _validate_tckn,
)

def clean_money(df: pd.DataFrame, cols):
    """
    Finansal kolonları string -> float çevirir.
    "12.345,90 TL" -> 12345.90
    "1,234.50$"    -> 1234.50
    Geçersiz/boş -> NaN
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    for c in cols:
        new_df[c] = (
            new_df[c]
            .astype(str)
            .str.strip()
            .apply(_strip_currency)
            .apply(_money_to_float)
        )
        new_df[c] = new_df[c].astype(float)
    return new_df


def clean_bool(df: pd.DataFrame, cols):
    """
    Evet/Hayır, True/False, 1/0, aktif/pasif vb -> pandas BooleanDtype
    Anlaşılmayan -> <NA>
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    def _to_bool(val):
        if val is None:
            return np.nan
        s = str(val).strip().lower()
        return BOOL_MAP.get(s, np.nan)

    for c in cols:
        new_df[c] = new_df[c].apply(_to_bool).astype("boolean")
    return new_df


def clean_date(df: pd.DataFrame, cols, output_format="string"):
    """
    Tarihleri normalize eder.
    output_format:
      - "string"   -> "YYYY-MM-DD"
      - "datetime" -> pandas datetime64[ns] (saat 00:00)
    Geçersiz -> None/NaT
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    for c in cols:
        parsed = new_df[c].apply(_parse_date_any)
        if output_format == "string":
            new_df[c] = parsed.apply(lambda d: d.isoformat() if d else None)
        else:
            new_df[c] = pd.to_datetime(parsed, errors="coerce").dt.normalize()
    return new_df


def standardize_city(df: pd.DataFrame, col):
    """
    İl bilgisini Türkiye standartlarına çeker.
    Örnek:
        "34", "ist.", "ıstanbul", "ISTANBUL" -> "İstanbul"
        "46", "maras", "kahramanmaras" -> "Kahramanmaraş"
    Bulamazsa title-case döndürür.
    """
    new_df = df.copy()
    new_df[col] = new_df[col].apply(lambda x: _normalize_city_name(x, CITY_MAP))
    return new_df


def clean_phone(df: pd.DataFrame, cols, country="TR"):
    """
    Türkiye telefonlarını normalize eder.
    Çıkış formatı: +90XXXXXXXXXX
    Geçersiz -> None
    Şu an sadece country="TR" destekli.
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    for c in cols:
        new_df[c] = new_df[c].apply(_normalize_phone_tr)
    return new_df


def validate_email(df: pd.DataFrame, cols, strict=False):
    """
    E-mail kolonlarını kontrol eder.
    Geçerliyse küçük harfe çekilmiş mail döner.
    Geçersizse None döner.
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    for c in cols:
        new_df[c] = new_df[c].apply(lambda x: _normalize_email(x, strict=strict))
    return new_df


def clean_percent(df: pd.DataFrame, cols):
    """
    Yüzde kolonlarını float'a çevirir.
        "%12,5" -> 12.5
        "0.85"  -> 0.85
    Geçersiz -> NaN
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    for c in cols:
        new_df[c] = new_df[c].apply(_percent_to_float)
        new_df[c] = new_df[c].astype(float)
    return new_df


def clean_tckn(df: pd.DataFrame, cols, validate=True):
    """
    T.C. Kimlik No kolonlarını normalize eder.
    - Sadece rakamları bırakır
    - 11 hane değilse -> None
    - validate=True ise checksum hatalıysa -> None
    Geçerliyse string olarak saklar (leading zero korunur diye int'e çevirmiyoruz).
    """
    cols = _ensure_list(cols)
    new_df = df.copy()

    def _process_tckn(x):
        if x is None:
            return None
        digits = _only_digits(x)
        if len(digits) != 11:
            return None
        if validate and not _validate_tckn(digits):
            return None
        return digits

    for c in cols:
        new_df[c] = new_df[c].apply(_process_tckn)
    return new_df
