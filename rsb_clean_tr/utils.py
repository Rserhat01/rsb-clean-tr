import re
import pandas as pd
import numpy as np
from dateutil import parser as dateparser  # python-dateutil

def _ensure_list(x):
    """Tek kolon adı verilse bile liste yap."""
    if isinstance(x, (list, tuple)):
        return list(x)
    return [x]

# ---------- PARA ----------

def _strip_currency(text: str):
    if text is None:
        return None
    t = str(text).strip()
    # Para birimi, semboller vs temizle
    t = re.sub(r"[A-Za-z₺€$£¥]", "", t)
    t = t.replace("TL", "").replace("tl", "").strip()
    return t

def _money_to_float(raw: str):
    if raw is None or raw == "":
        return None

    s = str(raw).strip()

    # Türk stili? "12.345,67"
    turkish_style = re.match(r"^[\d.]+,\d{1,4}$", s)
    if turkish_style:
        s = s.replace(".", "")
        s = s.replace(",", ".")
        try:
            return float(s)
        except ValueError:
            return None

    # US stili? "1,234.56"
    us_style = re.match(r"^[\d,]+\.\d{1,6}$", s)
    if us_style:
        s = s.replace(",", "")
        try:
            return float(s)
        except ValueError:
            return None

    # Düz sayı "2000" ya da "2000,5"
    s2 = s.replace(",", ".")
    try:
        return float(s2)
    except ValueError:
        return None

# ---------- TARİH ----------

def _parse_date_any(text: str):
    """Farklı tarih yazımlarını yakala. Başarısızsa None."""
    if text is None or str(text).strip() == "":
        return None
    t = str(text).strip()
    try:
        dt = dateparser.parse(t, dayfirst=True)
        if dt is None:
            return None
        return dt.date()
    except (ValueError, OverflowError):
        return None

# ---------- ŞEHİR ----------

def _normalize_city_name(x: str, city_map: dict):
    """
    Girdiyi sadeleştir (küçük harf, noktalama at, ı->i),
    sonra city_map içinde ara.
    Bulamazsak orijinali title-case döndür.
    """
    if x is None:
        return None

    s = str(x).strip().lower()

    # noktalama, boşluk vb temizle
    s = re.sub(r"[^0-9a-zA-Zşğıüöçİi]+", "", s, flags=re.UNICODE)

    # Türkçe ı -> i normalizasyonu
    s = s.replace("ı", "i")

    if s in city_map:
        return city_map[s]

    return str(x).strip().title()

# ---------- TELEFON ----------

def _normalize_phone_tr(raw: str):
    """
    Türkiye telefonu normalize et.
    Girdi örn:
        "0532 111 22 33"
        "+90 (532)1112233"
        "532-111-2233"
    Çıkış:
        "+905321112233"
    Geçersiz -> None
    """
    if raw is None:
        return None

    digits = re.sub(r"\D", "", str(raw))

    # "0532..." -> baştaki 0'ı at
    if digits.startswith("0"):
        digits = digits[1:]

    # "+90532..." formatı gibi 90 ile başlıyorsa:
    if digits.startswith("90"):
        digits = digits[2:]

    # Şu an elimizde 10 hane olmalı (5xx...)
    if len(digits) != 10:
        return None

    # Tamamen aynı rakam? (örn: 0000000000) -> çöp
    if len(set(digits)) == 1:
        return None

    return "+90" + digits

# ---------- E-MAIL ----------

EMAIL_REGEX = re.compile(
    r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$",
    re.IGNORECASE
)

def _normalize_email(raw: str, strict=False):
    """
    Geçerli e-mail ise küçük harfe çekip döner.
    Değilse None.
    strict=True olduğunda gereksiz şeyleri ileride genişletebiliriz.
    """
    if raw is None:
        return None
    s = raw.strip()
    if s == "":
        return None
    s = s.lower()
    if not EMAIL_REGEX.match(s):
        return None
    # strict modda fazladan kontrollere alan bırakıyoruz
    if strict:
        # ör: domain kısmında en az bir nokta var mı vb. (regex zaten çoğunu çözüyor)
        pass
    return s

# ---------- YÜZDE ----------

def _percent_to_float(raw: str):
    """
    "%12,5" -> 12.5
    "12,5%" -> 12.5
    "0.85"  -> 0.85
    "%0,85" -> 0.85
    """
    if raw is None:
        return None

    s = str(raw).strip()
    if s == "":
        return None

    # % işaretlerini temizle
    s = s.replace("%", "").strip()

    # türkçe virgülü noktaya çevir
    s = s.replace(",", ".")

    try:
        return float(s)
    except ValueError:
        return None

# ---------- TCKN ----------

def _only_digits(s: str):
    if s is None:
        return ""
    return re.sub(r"\D", "", str(s))

def _validate_tckn(id_number: str):
    """
    Basit T.C. Kimlik No algoritması:
    - 11 hane olmalı
    - ilk hane 0 olamaz
    - 10. hane ve 11. hane checksum kuralları
    """
    if not id_number or len(id_number) != 11:
        return False
    if id_number[0] == "0":
        return False
    if not id_number.isdigit():
        return False

    digits = [int(d) for d in id_number]
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11 = digits

    check10 = ((d1+d3+d5+d7+d9)*7 - (d2+d4+d6+d8)) % 10
    if check10 != d10:
        return False

    check11 = (sum(digits[:10])) % 10
    if check11 != d11:
        return False

    return True
