from pymongo import MongoClient

scheme = MongoClient().exams
new_coll = scheme.create_collection('minable_min')
coll = scheme['minable']

v = 'Valutazione Insegnamento'

for doc in coll.find():
    n = 0
    val = 0
    std = 0
    p6 = 0
    i = 0
    for key in list(doc.keys()):
        if v in key:
            if 'Val [media pesata]' in key:
                val = val + doc[key]
            if 'Std Dev [' in key:
                std = std + doc[key]
            if 'Val >= 6 [' in key:
                p6 = p6 + doc[key]
            if 'N [istanze]' in key:
                n = n + doc[key]
                i = i + 1

            del doc[key]

    if i != 0:
        doc[v + ' - N [media, istanze]'] = int(round(n / i, 0))
        doc[v + ' - Std Dev [media pesata]'] = round(std / i, 2)
        doc[v + ' - Val >= 6 [media, percent]'] = round(p6 / i, 2)
        doc[v + ' - Val [media pesata]'] = round(val / i, 2)

        new_coll.insert_one(doc)
