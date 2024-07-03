from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image

# Load the pre-trained models
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values

    # Create attention mask
    attention_mask = (pixel_values != tokenizer.pad_token_id).long()

    # Generate caption with attention_mask and max_new_tokens
    output_ids = model.generate(pixel_values, attention_mask=attention_mask, max_new_tokens=20)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption
