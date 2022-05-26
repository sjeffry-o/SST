import ruclip
import ngtpy

device = 'cpu'
model, processor = ruclip.load('ruclip-vit-base-patch16-224', device=device)

def vectorizeSearch(new_text, index): 
    input_ids = processor.encode_text(new_text).unsqueeze(0)
    print(input_ids.shape, processor.decode_text(input_ids))
    embedding = model.encode_text(input_ids).detach().numpy()
    results = index.search(embedding, 6)
    for i, (id, distance) in enumerate(results):
        print(str(i) + ": " + str(id) + ", " + str(distance))
        object = index.get_object(id)
        print(object)

if __name__ == "__main__":
    index = ngtpy.Index('test')
    vectorizeSearch('тестируем', index)
