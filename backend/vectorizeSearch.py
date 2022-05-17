import sys
sys.path.append("./ru-clip")
from clip.evaluate.utils import (get_tokenizer, load_weights_only, get_text_batch)
import gc

model, args = load_weights_only("ViT-B/32-small")
# vis_model = model.visual_encoder.cuda().float().eval()
text_model = model.text_encoder.float().eval()
tokenizer = get_tokenizer()

del model

gc.collect()

def vectorizeSearch(new_text, index): 
    input_ids, attention_mask = get_text_batch([new_text], tokenizer, args)
    vector = text_model(**{"x": input_ids, "attention_mask": attention_mask}).to('cpu').detach().numpy()
    results = index.search(vector, 6)
    for i, (id, distance) in enumerate(results):
        print(str(i) + ": " + str(id) + ", " + str(distance))
        object = index.get_object(id)
        print(object)
        img = open(img_paths[id], 'rb')
