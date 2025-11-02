# Boolean eşleştirme tablosu
# Not: bilinmeyen -> None döndürülür
BOOL_MAP = {
    "evet": True,
    "e": True,
    "true": True,
    "1": True,
    "1.0": True,
    "aktif": True,
    "var": True,
    "yes": True,
    "y": True,
    "on": True,
    "aktif/pasif:aktif": True,

    "hayır": False,
    "hayir": False,
    "h": False,
    "false": False,
    "0": False,
    "0.0": False,
    "pasif": False,
    "yok": False,
    "no": False,
    "n": False,
    "off": False,
    "aktif/pasif:pasif": False,

    "": None,
    "none": None,
    "null": None,
    "nan": None,
}

# Türkiye'deki 81 ilin normalize edilmiş halleri.
# Anahtarlar: küçük harf, boşluklar/noktalama atılmış, plaka kodları, kısa halleri
# Değerler: doğru imla ile tam il ismi
CITY_MAP = {
    # 01 Adana
    "01": "Adana", "adana": "Adana", "adn": "Adana",
    # 02 Adıyaman
    "02": "Adıyaman", "adiyaman": "Adıyaman", "adıyaman": "Adıyaman",
    # 03 Afyonkarahisar
    "03": "Afyonkarahisar", "afyon": "Afyonkarahisar", "afyonkarahisar": "Afyonkarahisar",
    # 04 Ağrı
    "04": "Ağrı", "agri": "Ağrı", "ağrı": "Ağrı",
    # 05 Amasya
    "05": "Amasya", "amasya": "Amasya",
    # 06 Ankara
    "06": "Ankara", "ank": "Ankara", "ankara": "Ankara",
    # 07 Antalya
    "07": "Antalya", "antalya": "Antalya", "ant": "Antalya",
    # 08 Artvin
    "08": "Artvin", "artvin": "Artvin",
    # 09 Aydın
    "09": "Aydın", "aydin": "Aydın", "ayd": "Aydın", "aydın": "Aydın",
    # 10 Balıkesir
    "10": "Balıkesir", "balikesir": "Balıkesir", "balıkesir": "Balıkesir", "balkes": "Balıkesir",
    # 11 Bilecik
    "11": "Bilecik", "bilecik": "Bilecik", "bile": "Bilecik",
    # 12 Bingöl
    "12": "Bingöl", "bingol": "Bingöl", "bingöl": "Bingöl",
    # 13 Bitlis
    "13": "Bitlis", "bitlis": "Bitlis",
    # 14 Bolu
    "14": "Bolu", "bolu": "Bolu",
    # 15 Burdur
    "15": "Burdur", "burdur": "Burdur",
    # 16 Bursa
    "16": "Bursa", "bursa": "Bursa", "brs": "Bursa",
    # 17 Çanakkale
    "17": "Çanakkale", "canakkale": "Çanakkale", "çanakkale": "Çanakkale", "cankk": "Çanakkale",
    # 18 Çankırı
    "18": "Çankırı", "cankiri": "Çankırı", "çankırı": "Çankırı",
    # 19 Çorum
    "19": "Çorum", "corum": "Çorum", "çorum": "Çorum",
    # 20 Denizli
    "20": "Denizli", "denizli": "Denizli", "dnz": "Denizli",
    # 21 Diyarbakır
    "21": "Diyarbakır", "diyarbakir": "Diyarbakır", "diyarbakır": "Diyarbakır", "diyr": "Diyarbakır",
    # 22 Edirne
    "22": "Edirne", "edirne": "Edirne",
    # 23 Elazığ
    "23": "Elazığ", "elazig": "Elazığ", "elazığ": "Elazığ", "elz": "Elazığ",
    # 24 Erzincan
    "24": "Erzincan", "erzincan": "Erzincan", "erz": "Erzincan",
    # 25 Erzurum
    "25": "Erzurum", "erzurum": "Erzurum", "erzrm": "Erzurum",
    # 26 Eskişehir
    "26": "Eskişehir", "eskisehir": "Eskişehir", "eskişehir": "Eskişehir", "eski": "Eskişehir",
    # 27 Gaziantep
    "27": "Gaziantep", "gaziantep": "Gaziantep", "antep": "Gaziantep", "gantep": "Gaziantep",
    # 28 Giresun
    "28": "Giresun", "giresun": "Giresun", "grs": "Giresun",
    # 29 Gümüşhane
    "29": "Gümüşhane", "gumushane": "Gümüşhane", "gümüşhane": "Gümüşhane",
    # 30 Hakkâri
    "30": "Hakkâri", "hakkari": "Hakkâri", "hakkâri": "Hakkâri",
    # 31 Hatay
    "31": "Hatay", "hatay": "Hatay", "antakya": "Hatay",
    # 32 Isparta
    "32": "Isparta", "isparta": "Isparta",
    # 33 Mersin
    "33": "Mersin", "mersin": "Mersin", "icel": "Mersin", "içel": "Mersin",
    # 34 İstanbul
    "34": "İstanbul", "istanbul": "İstanbul", "ıstanbul": "İstanbul", "i̇stanbul": "İstanbul",
    "ist": "İstanbul", "ist.": "İstanbul", "istanb": "İstanbul",
    # 35 İzmir
    "35": "İzmir", "izmir": "İzmir", "i̇zmir": "İzmir", "izm": "İzmir",
    # 36 Kars
    "36": "Kars", "kars": "Kars",
    # 37 Kastamonu
    "37": "Kastamonu", "kastamonu": "Kastamonu", "kst": "Kastamonu",
    # 38 Kayseri
    "38": "Kayseri", "kayseri": "Kayseri", "kysr": "Kayseri",
    # 39 Kırklareli
    "39": "Kırklareli", "kirklareli": "Kırklareli", "kırklareli": "Kırklareli", "klr": "Kırklareli",
    # 40 Kırşehir
    "40": "Kırşehir", "kirsehir": "Kırşehir", "kırşehir": "Kırşehir",
    # 41 Kocaeli
    "41": "Kocaeli", "kocaeli": "Kocaeli", "izmit": "Kocaeli",
    # 42 Konya
    "42": "Konya", "konya": "Konya", "kny": "Konya",
    # 43 Kütahya
    "43": "Kütahya", "kutahya": "Kütahya", "kütahya": "Kütahya",
    # 44 Malatya
    "44": "Malatya", "malatya": "Malatya", "mlt": "Malatya",
    # 45 Manisa
    "45": "Manisa", "manisa": "Manisa",
    # 46 Kahramanmaraş
    "46": "Kahramanmaraş", "kahramanmaras": "Kahramanmaraş", "kahramanmaraş": "Kahramanmaraş",
    "maras": "Kahramanmaraş", "maraş": "Kahramanmaraş",
    # 47 Mardin
    "47": "Mardin", "mardin": "Mardin",
    # 48 Muğla
    "48": "Muğla", "mugla": "Muğla", "muğla": "Muğla", "mgl": "Muğla",
    # 49 Muş
    "49": "Muş", "mus": "Muş", "muş": "Muş",
    # 50 Nevşehir
    "50": "Nevşehir", "nevsehir": "Nevşehir", "nevşehir": "Nevşehir",
    # 51 Niğde
    "51": "Niğde", "nigde": "Niğde", "niğde": "Niğde",
    # 52 Ordu
    "52": "Ordu", "ordu": "Ordu",
    # 53 Rize
    "53": "Rize", "rize": "Rize",
    # 54 Sakarya
    "54": "Sakarya", "sakarya": "Sakarya", "adapazari": "Sakarya", "adapazarı": "Sakarya",
    # 55 Samsun
    "55": "Samsun", "samsun": "Samsun",
    # 56 Siirt
    "56": "Siirt", "siirt": "Siirt",
    # 57 Sinop
    "57": "Sinop", "sinop": "Sinop",
    # 58 Sivas
    "58": "Sivas", "sivas": "Sivas",
    # 59 Tekirdağ
    "59": "Tekirdağ", "tekirdag": "Tekirdağ", "tekirdağ": "Tekirdağ", "tek": "Tekirdağ",
    # 60 Tokat
    "60": "Tokat", "tokat": "Tokat",
    # 61 Trabzon
    "61": "Trabzon", "trabzon": "Trabzon", "trbz": "Trabzon",
    # 62 Tunceli
    "62": "Tunceli", "tunceli": "Tunceli", "dersim": "Tunceli",
    # 63 Şanlıurfa
    "63": "Şanlıurfa", "sanliurfa": "Şanlıurfa", "şanlıurfa": "Şanlıurfa", "urfa": "Şanlıurfa",
    # 64 Uşak
    "64": "Uşak", "usak": "Uşak", "uşak": "Uşak",
    # 65 Van
    "65": "Van", "van": "Van",
    # 66 Yozgat
    "66": "Yozgat", "yozgat": "Yozgat",
    # 67 Zonguldak
    "67": "Zonguldak", "zonguldak": "Zonguldak", "zng": "Zonguldak",
    # 68 Aksaray
    "68": "Aksaray", "aksaray": "Aksaray",
    # 69 Bayburt
    "69": "Bayburt", "bayburt": "Bayburt",
    # 70 Karaman
    "70": "Karaman", "karaman": "Karaman",
    # 71 Kırıkkale
    "71": "Kırıkkale", "kirikkale": "Kırıkkale", "kırıkkale": "Kırıkkale", "krkl": "Kırıkkale",
    # 72 Batman
    "72": "Batman", "batman": "Batman",
    # 73 Şırnak
    "73": "Şırnak", "sirnak": "Şırnak", "şırnak": "Şırnak",
    # 74 Bartın
    "74": "Bartın", "bartin": "Bartın", "bartın": "Bartın",
    # 75 Ardahan
    "75": "Ardahan", "ardahan": "Ardahan",
    # 76 Iğdır
    "76": "Iğdır", "igdir": "Iğdır", "ığdır": "Iğdır",
    # 77 Yalova
    "77": "Yalova", "yalova": "Yalova",
    # 78 Karabük
    "78": "Karabük", "karabuk": "Karabük", "karabük": "Karabük",
    # 79 Kilis
    "79": "Kilis", "kilis": "Kilis",
    # 80 Osmaniye
    "80": "Osmaniye", "osmaniye": "Osmaniye",
    # 81 Düzce
    "81": "Düzce", "duzce": "Düzce", "düzce": "Düzce",
}
