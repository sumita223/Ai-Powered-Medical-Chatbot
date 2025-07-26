import os
import gradio as gr
from dotenv import load_dotenv
from brain import analyze_image_with_query, encode_image
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts
from banner import banner_html, requirements_html, disclaimer_html

load_dotenv()

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose.
             What's in this image?. Do you find anything wrong with it medically?
             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in
             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    # Check if both inputs are provided
    if not audio_filepath and not image_filepath:
        return "⚠️ Warning: Please upload an image AND record your voice to get a complete medical analysis.", "", None
    
    if not audio_filepath:
        return "⚠️ Warning: Please record your voice describing your symptoms or questions about the image.", "", None
    
    if not image_filepath:
        return "⚠️ Warning: Please upload a medical image for analysis along with your voice recording.", "", None
    
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                                                  audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")
    
    if image_filepath:
        encoded_img = encode_image(image_filepath)
        doctor_response = analyze_image_with_query(
            query=system_prompt + " " + speech_to_text_output,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encoded_image=encoded_img
        )
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath_mp3="final.mp3") 
    
    return speech_to_text_output, doctor_response, "final.mp3"

# 📁 Load CSS from external file
def load_css(file_path):
    """Load CSS from external file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"⚠️ Warning: CSS file '{file_path}' not found. Using default styling.")
        return ""
    except Exception as e:
        print(f"⚠️ Error loading CSS: {e}")
        return ""

# Load the CSS
custom_css = load_css('style.css')

# Create the interface with external CSS and HTML
with gr.Blocks(css=custom_css, title="AI Medical Assistant", theme=gr.themes.Soft()) as iface:
    # Banner Section
    gr.HTML(banner_html)
    
    # Requirements Notice
    gr.HTML(requirements_html)
    
    # Interface
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Upload Medical Image")
            image_input = gr.Image(type="filepath")
            
            gr.Markdown("### Record Your Question")  
            audio_input = gr.Audio(sources=["microphone"], type="filepath")
            
            submit_btn = gr.Button("Get Medical Analysis", variant="primary", size="lg")
            
        with gr.Column():
            gr.Markdown("### Analysis Results")
            
            speech_output = gr.Textbox(label="Speech to Text")
            doctor_output = gr.Textbox(label="Doctor's Response")
            audio_output = gr.Audio(label="Temp.mp3")
    
    # Disclaimer
    gr.HTML(disclaimer_html)
    
    # Connect function
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_output, doctor_output, audio_output]
    )

# Launch
if __name__ == "__main__":
    print("✅ Launching Gradio on host=0.0.0.0, port:", os.environ.get("PORT", 7681))
    iface.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7681))
    )
