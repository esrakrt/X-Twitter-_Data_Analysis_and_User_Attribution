from data_structures import HashTable

def en_cok_gecen_kelimeler(metin, limit=20):
    kelimeler = metin.lower().split()  # Metinden kelimeleri ayır
    yasakli_kelimeler = ["de", "ve","çok","kendi","bazı","iyesi","olarak","mel","her","fakat","ile", "bu","çeşitli" "ve", "ama","oda","ele","en","hem","bir", "iki", "hem", "en", "kadar", "ama", "ancak", "ne", "ise", "arada", "ayında", "konuşan", "gibi", "eden", "sadece", "oyunculu", "ağır", "üzerine", "çıktı."]

    hash_table = HashTable()
    temizlenmis_kelimeler = [kelime for kelime in kelimeler if kelime not in yasakli_kelimeler]
    for kelime in temizlenmis_kelimeler:
        # Her kelimeyi HashTable'a ekle
        if hash_table[kelime] is None:
            hash_table[kelime] = 1
        else:
            hash_table[kelime] += 1

    # En çok geçen kelimeleri bul ve döndür
    return hash_table.find_common_words(limit)

