from glob import glob
import gc
import torch
import ruclip
from PIL import Image
from torchvision.transforms import Compose, CenterCrop, ToTensor, Normalize, Resize

device = 'cuda'
model, processor = ruclip.load('ruclip-vit-base-patch16-224', device=device)

img_transform = Compose([
        Resize(224, interpolation=Image.BICUBIC),
        CenterCrop(224),
        lambda image: image.convert("RGB"),
        ToTensor(),
        Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711)),
    ])

vis_model = model.visual.cuda().float().eval()
del model

gc.collect()

def computeVectors(glob_path):
    img_vectors = torch.Tensor().to('cpu')
    img_paths = glob(glob_path)
    vectors_list = []
    device = 'cuda'
    count = 0

    with torch.no_grad():
      for path in img_paths:
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
    return img_vectors
