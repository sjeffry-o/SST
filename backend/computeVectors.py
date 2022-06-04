from glob import glob
import gc
import torch
import ruclip
import pickle
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

def computeImgVectors(glob_path, save=True):
    img_vectors = torch.Tensor().to('cpu')
    img_paths = glob(glob_path)
    device = 'cuda'
    count = 0

    with torch.no_grad():
      for path in img_paths:
        if count % 20000 == 0:
          print(count, "passed")
          if save:
            with open(f'img_embeds{count}.pkl', 'wb') as f:
              pickle.dump(img_vectors, f)
        image = Image.open(path)
        image = image.convert("RGB")
        image = img_transform(image)
        image = torch.tensor(image)
        image = image.to(device)
        img_vectors = torch.cat([img_vectors, vis_model(image.unsqueeze(0)).to('cpu')])
        count += 1
    return img_vectors

def computeTextVectors(text_list, save=True):
    text_vectors = torch.Tensor().to('cpu')
    device = 'cuda'
    count = 0

    with torch.no_grad():
      for text in text_list:
        if count % 20000 == 0:
          print(count, "passed")
          if save:
            with open(f'text_embeds{count}.pkl', 'wb') as f:
              pickle.dump(text_vectors, f)
        input_ids = processor.encode_text(text).unsqueeze(0).cuda()
        embedding = model.encode_text(input_ids)
        text_vectors = torch.cat([text_vectors, embedding.to('cpu')])
        count += 1
    return text_vectors
