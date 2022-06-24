import ngtpy
import pickle
import torch
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

def computeMeanJointEmbeddings(im_paths, texts, save=True):
    img_vectors = computeImgVectors(im_paths)
    text_vectors = computeTextVectors(texts)
    vectors_mean = torch.mean(torch.stack([img_vectors, text_vectors]), dim=0)
    if save:
        with open('joint_embeds.pkl', 'wb') as f:
            pickle.dump(vectors_mean, f)
    return vectors_mean

if __name__ == "__main__":
    with open('./imgNameMatch.pkl', 'rb') as f:
        imgToName = pickle.load(f)
    im_paths = list(imgToName.keys())
    texts = list(imgToName.values())
    assert [''] not in texts
    assert len(im_paths) == len(texts)
    assert all([len(name[0]) > 0 for name in texts])
    assert all([len(name) == 1 for name in texts])
    print(len(im_paths), len(texts))
    vectors_mean = computeMeanJointEmbeddings(im_paths, texts)
    print(vectors_mean.shape)
    indexCreateVerify(vectors_mean, 'opendataJointSearchIndex')
