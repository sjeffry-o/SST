import ngtpy
from computeVectors import computeImgVectors, computeTextVectors
 
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
        #print(object)

def computeMeanJointEmbeddings(im_glob, texts):
    img_vectors = computeImgVectors(im_glob)
    text_vectors = computeTextVectors(texts)
    vectors_mean = torch.mean(torch.stack([img_vectors, text_vectors]), dim=0)
    return vectors_mean

if __name__ == "__main__":
    import glob
    import torch
    im_glob = './static/*'
    im_paths = glob.glob(im_glob)
    texts = ['test'] * len(im_paths)
    vectors_mean = computeMeanJointEmbeddings(im_glob, texts)
    print(vectors_mean.shape)
    indexCreateVerify(vectors_mean, 'test')
