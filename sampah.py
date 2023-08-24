import random

def sampah_organik():
    namaSampah = ['daun', 'sampah sayur', 'nasi basi',
                  'kotoran hewan', 'ranting pohon',
                  'tulang', 'kulit buah', 'cangkang telur',
                  'ampas kopi', 'ampas teh', 'sampah ikan',
                  'bangkai', 'hewan mati'] 
    
    return random.choice(namaSampah)

def sampah_anorganik():
    namaSampah = ['sampah plastik', 'battery', 'kayu',
                  'besi', 'kotak', 'kardus', 'kresek',
                  'streoform', 'karet', 'gelas kaca',
                  'headband', 'pakenanya', 'sampah dvd']
    
    return random.choice(namaSampah)
