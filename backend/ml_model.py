import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from io import BytesIO

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")




def is_url(image_path):
    """Check if the image has http or https protocol and if it needs to be obtained through requests
    Args:
        image_path (_type_): string representing the image path or URL

    Returns:
        _type_: boolean indicating if the image path is a URL
    """
    return image_path.startswith("http://") or image_path.startswith("https://")

#For testing purposes, we can use a sample image from the internet
# You can replace this with any image URL or local path
image = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"


def obtain_caption(image_path):
    """
    Obtain the caption of the image using BLIP model.

    Args:
        image_path (_type_): string representing the image path or URL

    Returns:
        _type_: string representing the caption of the image
    """
    raw_image = None
 
    if is_url(image_path):
        raw_image = Image.open(requests.get(image_path, stream=True).raw).convert('RGB')
    else:
        raw_image = Image.open(image_path).convert('RGB')
    # This is supposed to handle a file object
    
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
