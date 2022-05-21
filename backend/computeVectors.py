from glob import glob
import sys
sys.path.append("./ru-clip")
from clip.evaluate.utils import (get_tokenizer, load_weights_only, get_text_batch)
import gc
import torch

img_transform = Compose([
        Resize(224, interpolation=Image.BICUBIC),
        CenterCrop(224),
        lambda image: image.convert("RGB"),
        ToTensor(),
        Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711)),
    ])
img_paths = glob('./static/*')

model, args = load_weights_only("ViT-B/32-small")
# vis_model = model.visual_encoder.cuda().float().eval()
text_model = model.text_encoder.float().eval()
tokenizer = get_tokenizer()

del model

gc.collect()

img_vectors = torch.Tensor().to('cpu')
img_vectors = existing_vectors
vectors_list = []
count = len(existing_vectors)
device = 'cuda'
vis_model = vis_model.eval()
with torch.no_grad():
  for path in img_paths[len(existing_vectors):]:
    if count % 20000 == 0:
      print(count, "passed")
    image = Image.open(path)
    image = image.convert("RGB")
    image = img_transform(image)
    image = torch.tensor(image)
    image = image.to(device)
    # vectors_list.append(vis_model(image.unsqueeze(0)).to('cpu'))
    img_vectors = torch.cat([img_vectors, vis_model(image.unsqueeze(0)).to('cpu')])
    count += 1
