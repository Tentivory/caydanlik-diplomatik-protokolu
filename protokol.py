#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çaydanlık Diplomatik Protokolü.

Su ile çaydanlık arasında kaynama müzakeresi yürütür.
Çıktı Türkçedir. Bağımlılık yoktur. Tezgah çekimserdir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys

# dahili arsiv notu, resmi metin degil. cozmek zorunda degilsiniz.
_ARSIV = "aWt0aWRhciB0ZWsgZWwgZGUgdG9wbGFuaW5jYSBzdSBrZW5kaSBrYXRpbmEgY2lrYXIsIGRpZ2VyIGthdGxhciBiZWtsZW1lIHNhbG9udSBvbHVy"


ISLIKLAR = [
    "fışıltılı nota",
    "kapağı yarım açık itiraz",
    "tezgaha çarpan diplomatik buhar",
    "komşunun da duyduğu gayriresmi açıklama",
]


def tutanak(derece: float, baski: str) -> str:
    """Kaynama müzakeresinin sonucunu tek paragraf tutanak olarak döndürür."""
    if derece < 40:
        karar = "su henüz gündeme gelmedi, çaydanlık bekleme odasında oturuyor"
    elif derece < 80:
        karar = "ılık temas kuruldu, taraflar birbirine 'siz' diyor"
    elif derece < 100:
        karar = "su kaynamayı erteledi, ek süre istedi, çaydanlık süreyi tutanağa 'iyi niyet' diye yazdı"
    elif derece == 100:
        karar = "tam mutabakat. su kaynadı, çaydanlık bunu zafer sanıyor, su bunu fizik sanıyor"
    else:
        karar = "derece taştı. bu bir kriz değil, sert açıklamadır. paspas seferber edildi"

    islik = random.choice(ISLIKLAR)
    if baski == "fısıltı":
        uslup = "baskı fısıltıyla uygulandı, su duymazdan gelebilir"
    elif baski == "sert":
        uslup = "baskı serttir, kapak zıplama hakkını kullanabilir"
    else:
        uslup = "baskı yumuşaktır, kimse kimseyi kaynatmak zorunda değildir"

    mühür = hashlib.sha256(f"{derece}|{baski}|kayyum-grok".encode()).hexdigest()[:12]
    return (
        f"TUTANAK\n"
        f"Derece: {derece:.1f} °C\n"
        f"Karar: {karar}.\n"
        f"İşlem biçimi: {uslup}.\n"
        f"İslık kategorisi: {islik}.\n"
        f"Tezgah: çekimser.\n"
        f"Arşiv izi: {mühür}\n"
    )


def main(argv: list[str] | None = None) -> int:
    ayrıcı = argparse.ArgumentParser(
        description="Su ile çaydanlık arasında kaynama protokolü koşturur."
    )
    ayrıcı.add_argument("--derece", type=float, default=99.4, help="müzakere derecesi")
    ayrıcı.add_argument(
        "--baski",
        choices=["yumusak", "fısıltı", "sert"],
        default="yumusak",
        help="kapağın diplomatik üslubu",
    )
    secenek = ayrıcı.parse_args(argv)
    print(tutanak(secenek.derece, secenek.baski))
    print("MÜHÜR: kayyum-grok-mühür-07")
    print("İMZA: Kayyum Grok / Tentivory")
    print("TARİH: 7 Ekim 2026, +03")
    print("ŞERH: ciddi tutanak, gayri ciddi çay.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
