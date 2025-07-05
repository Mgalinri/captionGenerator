import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# Check if the image has http or https protocol and if it needs to be obtained through requests


image = requests.get("https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg",stream=True).raw
print(image)
def obtain_caption(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
print(obtain_caption(image))