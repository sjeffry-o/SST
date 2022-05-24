import ngtpy
from computeVectors import computeVectors
 
def indexCreateVerify(vectors, indexName):
    dim = vectors.shape[1]
     
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

if __name__ == "__main__":
    vectors = computeVectors('./static/*')
    print(vectors.shape)
    indexCreateVerify(vectors, 'test')
