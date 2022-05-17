import ngtpy
 
def indexCreateVerify(vectors, indexName)
    dim = 1024
     
    ngtpy.create(indexName, dim)
    index = ngtpy.Index(indexName)
    index.batch_insert(vectors)
    index.save()
     
    query = vectors[0]
    results = index.search(query, 10)
    for i, (id, distance) in enumerate(results) :
        print(str(i) + ": " + str(id) + ", " + str(distance))
        object = index.get_object(id)
        print(object)
