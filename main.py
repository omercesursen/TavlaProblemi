def taht_olustur(hedefe_gelen_sozcuk):
    tahta = {}
    for i in range(1, 25):
        tahta[i] = 0

    for kutu, sayi in hedefe_gelen_sozcuk.items():
        tahta[kutu] = sayi
    return tahta

def tas_oynat(mevcut_tahta, baslangic, zar):
    if mevcut_tahta is None:
        return None

    yeni_tahta = mevcut_tahta.copy()
    hedef = baslangic + zar

    if hedef > 24:
        return None

    if yeni_tahta[baslangic] <= 0:
        return None

    yeni_tahta[baslangic] = yeni_tahta[baslangic] - 1
    yeni_tahta[hedef] = yeni_tahta[hedef] + 1
    return yeni_tahta

def tahtayi_puanla(tahta,baslangic,hedef):
    puan = 0
    onemli_kapilar = [5, 6, 7, 8, 17, 18, 19, 20]

    eski_sayi_baslangic = tahta[baslangic]
    yeni_sayi_baslangic = eski_sayi_baslangic - 1

    if eski_sayi_baslangic >= 2 and yeni_sayi_baslangic == 1:
        if baslangic in onemli_kapilar:
            puan -= 2
        else:
            puan -= 1
        puan -= 1


    elif eski_sayi_baslangic == 1 and yeni_sayi_baslangic == 0:
        puan += 1

    eski_sayi_hedef = tahta[hedef]
    yeni_sayi_hedef = eski_sayi_hedef + 1

    if eski_sayi_hedef == 1 and yeni_sayi_hedef == 2:
        puan += 1
        if hedef in onemli_kapilar:
            puan += 2
        else:
            puan += 1

    elif eski_sayi_hedef == 0 and yeni_sayi_hedef == 1:
        puan -= 1

    return puan



def find_moves(transfer_edilen_sozcuk,dice1,dice2):
    oyun_tahtasi = taht_olustur(transfer_edilen_sozcuk)
    bulunan_hamleler = []

    z1 = dice1
    z2 = dice2

    for baslangic1 in range(1, 25):
        hedef1 = baslangic1 + z1
        tahta2 = tas_oynat(oyun_tahtasi, baslangic1, z1)
        if tahta2 is None: continue

        p1 = tahtayi_puanla(oyun_tahtasi, baslangic1, hedef1)

        for baslangic2 in range(1, 25):
            hedef2 = baslangic2 + z2
            tahta3 = tas_oynat(tahta2, baslangic2, z2)

            if tahta3 is None: continue

            p2 = tahtayi_puanla(tahta2, baslangic2, hedef2)

            fark = p1 + p2

            if fark > 0:
                hamle1 = (baslangic1, hedef1)
                hamle2 = (baslangic2, hedef2)
                sonuc = (hamle1, hamle2, fark)
                if sonuc not in bulunan_hamleler:
                    bulunan_hamleler.append(sonuc)

    if dice1 != dice2:
        z1 = dice2
        z2 = dice1

        for baslangic1 in range(1, 25):
            hedef1 = baslangic1 + z1
            tahta2 = tas_oynat(oyun_tahtasi, baslangic1, z1)
            if tahta2 is None: continue

            p1 = tahtayi_puanla(oyun_tahtasi, baslangic1, hedef1)

            for baslangic2 in range(1, 25):
                hedef2 = baslangic2 + z2
                tahta3 = tas_oynat(tahta2, baslangic2, z2)
                if tahta3 is None: continue

                p2 = tahtayi_puanla(tahta2, baslangic2, hedef2)

                fark = p1 + p2
                if fark > 0:
                    hamle1 = (baslangic1, hedef1)
                    hamle2 = (baslangic2, hedef2)
                    sonuc = (hamle1, hamle2, fark)
                    if sonuc not in bulunan_hamleler:
                        bulunan_hamleler.append(sonuc)

    return bulunan_hamleler

ilk_olusan_sozcuk = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}

print(find_moves(ilk_olusan_sozcuk, 6, 1))
