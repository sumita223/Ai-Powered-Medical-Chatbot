# from dotenv import load_dotenv
# import os
# import base64
# from groq import Groq

# # Step 1: Load API key from .env
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # Step 2: Encode image
# def encode_image(image_path):   
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')


# def analyze_image_with_query(query: str, model: str, encoded_image: str):
#     client = Groq(api_key=GROQ_API_KEY)

#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": query},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}"
#                     }
#                 }
#             ]
#         }
#     ]

#     query = str(query)  # Just to be safe

#     chat_completion = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "user", "content": query}
#         ]
#     )


#     return chat_completion.choices[0].message.content


# # Call function
# image = encode_image("acne.jpg")
# analyze_image_with_query("What’s wrong with my face?", "meta-llama/llama-4-scout-17b-16e-instruct", image)



from dotenv import load_dotenv
import os
import base64
from groq import Groq

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Encode image to base64
def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def analyze_image_with_query(query: str, model: str, encoded_image: str):
    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ]
    )

    return chat_completion.choices[0].message.content

# from transformers import AutoProcessor, LlavaForConditionalGeneration
# from PIL import Image
# import torch

# # Load processor and model once at the top
# processor = AutoProcessor.from_pretrained("llava-hf/llava-1.5-7b-hf")
# model = LlavaForConditionalGeneration.from_pretrained(
#     "llava-hf/llava-1.5-7b-hf",
#     torch_dtype=torch.float16,
#     device_map="auto"
# )

# # Function to open and convert image
# def encode_image(image_path):
#     image = Image.open(image_path).convert("RGB")
#     return image

# # Main function to analyze image with a query
# def analyze_image_with_query(query, encoded_image, model_name=None):
#     # Ensure the prompt contains the <image> token
#     prompt = "<image>\n" + query

#     # Process inputs
#     inputs = processor(images=encoded_image, text=prompt, return_tensors="pt").to(model.device)

#     # Generate output
#     output = model.generate(**inputs, max_new_tokens=100)

#     # Decode and return result
#     result = processor.batch_decode(output, skip_special_tokens=True)[0]
#     return result
