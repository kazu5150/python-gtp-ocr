import os
from dotenv import load_dotenv
from PIL import Image
import pytesseract
from openai import OpenAI
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def process_with_gpt4(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. The following text is extracted from a Japanese document. Please analyze and summarize the content in Japanese."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='jpn')
    print(f"Extracted text: {text}")  # デバッグ用
    return text

def main():
    input_dir = 'data/input/'
    output_csv = 'data/output/results.csv'

    # Get the first image file in the input directory
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print("No image files found in the input directory.")
        return

    input_image = os.path.join(input_dir, image_files[0])
    print(f"Processing image: {input_image}")

    # Extract text from image
    extracted_text = extract_text_from_image(input_image)

    # Process text with GPT-4
    processed_text = process_with_gpt4(extracted_text)

    # Save results to CSV
    save_to_csv([{'processed_text': processed_text}], output_csv)

    print(f"Processing complete. Results saved to {output_csv}")

if __name__ == "__main__":
    main()