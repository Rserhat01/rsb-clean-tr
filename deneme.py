import pandas as pd
import rsb_clean_tr as rsb

print(rsb.__version__)

df = pd.DataFrame({
    "ucret":   ["12.345,90 TL", "1,234.50$", None],
    "telefon": ["0532 111 22 33", "+90 (555) 444 33 22", "0000000000"],
    "tarih":   ["12.03.2024", "2024/3/12", "bozuk"],
    "il":      ["34", "maras", "ank"],
    "tckn":    ["10000000146", "12345678901", "01234567890"]
})

df = (
    df.pipe(rsb.clean_money, "ucret")
      .pipe(rsb.clean_phone, "telefon")
      .pipe(rsb.clean_date, "tarih", output_format="string")
      .pipe(rsb.standardize_city, "il")
      .pipe(rsb.clean_tckn, "tckn")
)

print(df)
