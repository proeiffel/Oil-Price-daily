from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Geçici örnek veri (manuel)
fiyatlar = [
    {"tarih": "2025-04-01", "brent": 85, "benzin": 42.50, "motorin": 41.80},
    {"tarih": "2025-04-02", "brent": 89, "benzin": 44.00, "motorin": 43.10},
    {"tarih": "2025-04-03", "brent": 87, "benzin": 43.80, "motorin": 42.90},
    {"tarih": "2025-04-04", "brent": 86, "benzin": 44.20, "motorin": 43.50},
]

def hesapla_degisimler(data):
    analiz = []
    for i in range(1, len(data)):
        onceki = data[i - 1]
        bugun = data[i]

        brent_degisim = ((bugun["brent"] - onceki["brent"]) / onceki["brent"]) * 100
        benzin_degisim = ((bugun["benzin"] - onceki["benzin"]) / onceki["benzin"]) * 100
        motorin_degisim = ((bugun["motorin"] - onceki["motorin"]) / onceki["motorin"]) * 100

        analiz.append({
            "tarih": bugun["tarih"],
            "brent_yuzde": round(brent_degisim, 2),
            "benzin_yuzde": round(benzin_degisim, 2),
            "motorin_yuzde": round(motorin_degisim, 2),
            "benzin_fark": round(benzin_degisim - brent_degisim, 2),
            "motorin_fark": round(motorin_degisim - brent_degisim, 2),
        })
    return analiz

@app.route("/")
def index():
    analiz = hesapla_degisimler(fiyatlar)
    return render_template("index.html", analiz=analiz)

if __name__ == "__main__":
    app.run(debug=True)
