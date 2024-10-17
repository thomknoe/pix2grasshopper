import json
from openai import OpenAI
import os
import torch
import clip
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def load_descriptions(file_path='descriptions.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
        descriptions = []
        tokens = []
        for category, desc_list in data.items():
            descriptions.extend(desc_list)
            tokens.extend([category] * len(desc_list))
    return descriptions, tokens

def get_image_description(image_path, descriptions):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    text_inputs = clip.tokenize(descriptions).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_inputs)

        similarities = (image_features @ text_features.T).softmax(dim=-1)
        best_match_idx = similarities.argmax().item()
        return descriptions[best_match_idx]

def generate_python_code(description):
    prompt = (
        f"Convert the following description into Python code using RhinoScriptSyntax "
        f"for Rhino in Grasshopper, suitable for a GHPython component: {description}. "
        f"Make sure to include calls to the functions made int he sciprt at the end of code and makes sure to outupts the geometry through the 'a' variable."
        f"Do not include introductory or explanation text, simply give me the code, dont include LaTeX formating either for the start or end fo the code block"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in Rhino and Grasshopper scripting."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700,
        temperature=0.2
        )
        python_code = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating Python code: {e}")
        return None

    return python_code

def process_image(image_path):
    descriptions, tokens = load_descriptions('descriptions.json')

    description = get_image_description(image_path, descriptions)
    print(f"Description generated by CLIP: {description}")

    python_code = generate_python_code(description)
    print(f"Generated Python Code:\n{python_code}")

    return python_code


if __name__ == "__main__":
    image_path = "picture/pattern.png"
    generated_code = process_image(image_path)