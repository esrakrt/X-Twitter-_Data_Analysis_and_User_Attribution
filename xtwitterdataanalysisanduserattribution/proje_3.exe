
import json
#import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from data_structures import HashTable ,LinkedList,myList

model_name = "MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7" 

classifier = pipeline("zero-shot-classification", model=AutoModelForSequenceClassification.from_pretrained(model_name), tokenizer=model_name)

interests_users = HashTable()

candidate_labels = ["ekonomi", "spor", "politika", "sağlık", "araç", "tarih", "psikoloji", "felsefe", "kültür"]

def group_users_by_interest(users_tweets):
    print("in group interests")
    interests_users = HashTable()
    for user, tweets in users_tweets.get_items():
        # Her bir ilgi alanının kaç kez çıktığını sayan bir linked list
        interest_counts = LinkedList()
        for tweet in tweets:
            sequence_to_classify = tweet
            output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
            max_score = max(output['scores'])
            max_index = output['scores'].index(max_score)
            max_label = output['labels'][max_index]
            print("1")
            # İlgi alanının kaç kez çıktığını say
            if interest_counts.find(max_label):
                val = interest_counts.find(max_label)+1
                interest_counts.set(max_label, val)
                print("2")  
            else:
                interest_counts.set(max_label, 1)
                print("3")
        # En çok çıkan ilgi alanını bul
        max_interest = interest_counts.max()
        print("4")

        # İlgi alanı için hash map oluştur
        if  interests_users.find(max_interest)== None:
            interest_list = myList()
            interests_users.__setitem__(max_interest,interest_list)    
        interest_list.insert(user)
        print("5")
        
    return interests_users


def print_interests(interests_users):
    print("6")
    with open('sonuclar.json', 'r') as f:
        data = json.load(f)
    
    # İlgi alanlarına göre kullanıcıları ekleyin
        data['ilgi_alanindaki_kisiler'] = {}  # Yeni verileri saklamak için bir sözlük oluşturun
    for interest in interests_users:
        data['ilgi_alanindaki_kisiler'][interest] = list(interests_users[interest])

    # Tüm verileri dosyaya geri yaz
    with open('sonuclar.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    