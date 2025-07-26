
# import os
# import gradio as gr
# from dotenv import load_dotenv


# from brain import analyze_image_with_query, encode_image

# from voice_of_the_patient import record_audio, transcribe_with_groq
# from voice_of_doctor import text_to_speech_with_gtts

# load_dotenv()

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# def process_inputs(audio_filepath, image_filepath):
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
#                                                  audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")

#     # Handle the image input
#     # if image_filepath:
#     #     doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath))
#     # else:
#     #     doctor_response = "No image provided for me to analyze"

#     if image_filepath:
#         encoded_img = encode_image(image_filepath)
#         doctor_response = analyze_image_with_query(
#             query=system_prompt + " " + speech_to_text_output,
#             model="meta-llama/llama-4-scout-17b-16e-instruct",
#             encoded_image=encoded_img
#         )
#     else:
#         doctor_response = "No image provided for me to analyze"


#     voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath_mp3="final.mp3") 

#     return speech_to_text_output, doctor_response, "final.mp3"


# # Create the interface
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")
#     ],
#     outputs=[
#         gr.Textbox(label="Speech to Text"),
#         gr.Textbox(label="Doctor's Response"),
#         gr.Audio(label="Temp.mp3")
#     ],
#     title="AI Doctor with Vision and Voice"
# )
# # ✅ Make it work on Render
# import os

# # DEBUG PRINT to confirm port being used
# print("✅ Launching Gradio on host=0.0.0.0, port:", os.environ.get("PORT", 7681))

# iface.launch(
#     server_name="0.0.0.0",
#     server_port=int(os.environ.get("PORT", 7681))
# )

#####working
# import os
# import gradio as gr
# from dotenv import load_dotenv
# from brain import analyze_image_with_query, encode_image
# from voice_of_the_patient import record_audio, transcribe_with_groq
# from voice_of_doctor import text_to_speech_with_gtts

# load_dotenv()

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose.
#              What's in this image?. Do you find anything wrong with it medically?
#              If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in
#              your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
#              Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

# def process_inputs(audio_filepath, image_filepath):
#     # Check if both inputs are provided
#     if not audio_filepath and not image_filepath:
#         return "⚠️ Warning: Please upload an image AND record your voice to get a complete medical analysis.", "", None
    
#     if not audio_filepath:
#         return "⚠️ Warning: Please record your voice describing your symptoms or questions about the image.", "", None
    
#     if not image_filepath:
#         return "⚠️ Warning: Please upload a medical image for analysis along with your voice recording.", "", None
    
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
#                                                   audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")
#     # Handle the image input
#     # if image_filepath:
#     #     doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath))
#     # else:
#     #     doctor_response = "No image provided for me to analyze"
    
#     if image_filepath:
#         encoded_img = encode_image(image_filepath)
#         doctor_response = analyze_image_with_query(
#             query=system_prompt + " " + speech_to_text_output,
#             model="meta-llama/llama-4-scout-17b-16e-instruct",
#             encoded_image=encoded_img
#         )
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath_mp3="final.mp3") 
    
#     return speech_to_text_output, doctor_response, "final.mp3"

# # 🎨 Custom CSS for subtle styling
# custom_css = """
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@300;400;500;600&display=swap');

# * {
#     font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
# }

# body {
#     background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
#     min-height: 100vh;
# }

# .gradio-container {
#     background: rgba(255, 255, 255, 0.85);
#     backdrop-filter: blur(10px);
#     border-radius: 20px;
#     box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
#     border: 1px solid rgba(255, 255, 255, 0.2);
# }

# .banner-container {
#     background: linear-gradient(135deg, #e8f4f8 0%, #d6eaf8 50%, #ebf3fd 100%);
#     padding: 2.5rem;
#     border-radius: 16px;
#     margin-bottom: 2rem;
#     color: #2c3e50;
#     text-align: center;
#     box-shadow: 0 4px 20px rgba(52, 73, 94, 0.08);
#     border: 1px solid rgba(52, 73, 94, 0.05);
# }

# .banner-title {
#     font-family: 'Poppins', sans-serif;
#     font-size: 2.2rem;
#     font-weight: 500;
#     margin-bottom: 1rem;
#     color: #34495e;
#     letter-spacing: -0.5px;
# }

# .banner-subtitle {
#     font-size: 1.1rem;
#     margin-bottom: 2rem;
#     color: #5d6d7e;
#     font-weight: 300;
#     line-height: 1.5;
# }

# .steps-container {
#     display: flex;
#     justify-content: space-around;
#     flex-wrap: wrap;
#     gap: 1.5rem;
#     margin-top: 2rem;
# }

# .step-card {
#     background: rgba(255, 255, 255, 0.7);
#     backdrop-filter: blur(5px);
#     border-radius: 12px;
#     padding: 1.8rem;
#     flex: 1;
#     min-width: 250px;
#     max-width: 300px;
#     border: 1px solid rgba(52, 73, 94, 0.08);
#     transition: transform 0.2s ease, box-shadow 0.2s ease;
# }

# .step-card:hover {
#     transform: translateY(-2px);
#     box-shadow: 0 6px 25px rgba(52, 73, 94, 0.12);
# }

# .step-number {
#     background: linear-gradient(135deg, #85c1e9 0%, #5dade2 100%);
#     color: white;
#     width: 36px;
#     height: 36px;
#     border-radius: 50%;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     font-weight: 500;
#     font-size: 1rem;
#     margin: 0 auto 1rem auto;
#     box-shadow: 0 2px 8px rgba(93, 173, 226, 0.3);
# }

# .step-title {
#     font-family: 'Poppins', sans-serif;
#     font-size: 1rem;
#     font-weight: 500;
#     margin-bottom: 0.8rem;
#     color: #2c3e50;
# }

# .step-description {
#     font-size: 0.85rem;
#     color: #5d6d7e;
#     line-height: 1.5;
#     font-weight: 300;
# }

# .features-badges {
#     display: flex;
#     justify-content: center;
#     gap: 1rem;
#     margin-top: 2rem;
#     flex-wrap: wrap;
# }

# .feature-badge {
#     background: rgba(255, 255, 255, 0.6);
#     padding: 0.6rem 1.2rem;
#     border-radius: 25px;
#     font-size: 0.85rem;
#     border: 1px solid rgba(52, 73, 94, 0.1);
#     color: #34495e;
#     font-weight: 400;
#     transition: all 0.2s ease;
# }

# .feature-badge:hover {
#     background: rgba(255, 255, 255, 0.8);
#     transform: translateY(-1px);
# }

# .medical-icon {
#     font-size: 2.5rem;
#     margin-bottom: 1rem;
#     opacity: 0.8;
# }

# .disclaimer {
#     background: linear-gradient(135deg, #fef9e7 0%, #fcf3cf 100%);
#     border: 1px solid #f7dc6f;
#     border-radius: 10px;
#     padding: 1.2rem;
#     margin-top: 2rem;
#     color: #7d6608;
#     text-align: center;
#     font-size: 0.85rem;
#     font-weight: 400;
#     line-height: 1.4;
# }

# .requirements-notice {
#     background: linear-gradient(135deg, #e8f5e8 0%, #d4edda 100%);
#     border: 1px solid #c3e6cb;
#     border-radius: 10px;
#     padding: 1rem;
#     margin: 1rem 0;
#     color: #155724;
#     text-align: center;
#     font-size: 0.9rem;
#     font-weight: 500;
# }

# .gr-button {
#     background: linear-gradient(135deg, #85c1e9 0%, #5dade2 100%) !important;
#     border: none !important;
#     color: white !important;
#     font-weight: 500 !important;
#     border-radius: 8px !important;
#     transition: all 0.2s ease !important;
# }

# .gr-button:hover {
#     transform: translateY(-1px) !important;
#     box-shadow: 0 4px 15px rgba(93, 173, 226, 0.3) !important;
# }

# .gr-textbox {
#     border-radius: 8px !important;
#     border: 1px solid rgba(52, 73, 94, 0.1) !important;
#     background: rgba(255, 255, 255, 0.9) !important;
# }

# h3 {
#     font-family: 'Poppins', sans-serif !important;
#     color: #34495e !important;
#     font-weight: 500 !important;
#     font-size: 1.1rem !important;
# }
# """

# # 🏥 Banner HTML
# banner_html = """
# <div class="banner-container">
#     <div class="medical-icon">🩺</div>
#     <h1 class="banner-title">AI Medical Assistant</h1>
#     <p class="banner-subtitle">Professional medical insights through advanced AI analysis</p>
    
#     <div class="steps-container">
#         <div class="step-card">
#             <div class="step-number">1</div>
#             <div class="step-title">Upload Medical Image</div>
#             <div class="step-description">
#                 Share a clear photograph of the medical condition or area requiring analysis
#             </div>
#         </div>
        
#         <div class="step-card">
#             <div class="step-number">2</div>
#             <div class="step-title">Voice Description</div>
#             <div class="step-description">
#                 Describe your symptoms or concerns using the microphone for detailed analysis
#             </div>
#         </div>
        
#         <div class="step-card">
#             <div class="step-number">3</div>
#             <div class="step-title">Receive Analysis</div>
#             <div class="step-description">
#                 Get comprehensive medical insights and recommendations from our AI system
#             </div>
#         </div>
#     </div>
    
#     <div class="features-badges">
#         <div class="feature-badge">Medical Analysis</div>
#         <div class="feature-badge">Voice Recognition</div>
#         <div class="feature-badge">Image Processing</div>
#         <div class="feature-badge">AI Consultation</div>
#     </div>
# </div>
# """

# # 📋 Requirements Notice HTML
# requirements_html = """
# <div class="requirements-notice">
#     <strong>📋 Important:</strong> Both medical image AND voice recording are required for complete analysis
# </div>
# """

# # 📋 Disclaimer HTML
# disclaimer_html = """
# <div class="disclaimer">
#     <strong>Medical Disclaimer:</strong> This AI assistant provides educational information only and should not replace professional medical consultation. Please consult qualified healthcare professionals for medical concerns and treatment decisions.
# </div>
# """

# # Create the interface with custom styling
# with gr.Blocks(css=custom_css, title="AI Medical Assistant", theme=gr.themes.Soft()) as iface:
#     # Banner Section
#     gr.HTML(banner_html)
    
#     # Requirements Notice
#     gr.HTML(requirements_html)
    
#     # Original Interface Structure - UNCHANGED
#     with gr.Row():
#         with gr.Column():
#             gr.Markdown("### Upload Medical Image")
#             image_input = gr.Image(type="filepath")
            
#             gr.Markdown("### Record Your Question")  
#             audio_input = gr.Audio(sources=["microphone"], type="filepath")
            
#             # Add submit button
#             submit_btn = gr.Button("Get Medical Analysis", variant="primary", size="lg")
            
#         with gr.Column():
#             gr.Markdown("### Analysis Results")
            
#             speech_output = gr.Textbox(label="Speech to Text")
#             doctor_output = gr.Textbox(label="Doctor's Response")
#             audio_output = gr.Audio(label="Temp.mp3")
    
#     # Disclaimer
#     gr.HTML(disclaimer_html)
    
#     # Connect function with button click - WITH VALIDATION
#     submit_btn.click(
#         fn=process_inputs,
#         inputs=[audio_input, image_input],
#         outputs=[speech_output, doctor_output, audio_output]
#     )

# # ✅ Make it work on Render
# import os
# # DEBUG PRINT to confirm port being used
# print("✅ Launching Gradio on host=0.0.0.0, port:", os.environ.get("PORT", 7681))

# iface.launch(
#     server_name="0.0.0.0",
#     server_port=int(os.environ.get("PORT", 7681))
# )



#working2
# import os
# import gradio as gr
# from dotenv import load_dotenv
# from brain import analyze_image_with_query, encode_image
# from voice_of_the_patient import record_audio, transcribe_with_groq
# from voice_of_doctor import text_to_speech_with_gtts

# load_dotenv()

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose.
#              What's in this image?. Do you find anything wrong with it medically?
#              If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in
#              your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot,
#              Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

# def process_inputs(audio_filepath, image_filepath):
#     # Check if both inputs are provided
#     if not audio_filepath and not image_filepath:
#         return "⚠️ Warning: Please upload an image AND record your voice to get a complete medical analysis.", "", None
    
#     if not audio_filepath:
#         return "⚠️ Warning: Please record your voice describing your symptoms or questions about the image.", "", None
    
#     if not image_filepath:
#         return "⚠️ Warning: Please upload a medical image for analysis along with your voice recording.", "", None
    
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
#                                                   audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")
    
#     if image_filepath:
#         encoded_img = encode_image(image_filepath)
#         doctor_response = analyze_image_with_query(
#             query=system_prompt + " " + speech_to_text_output,
#             model="meta-llama/llama-4-scout-17b-16e-instruct",
#             encoded_image=encoded_img
#         )
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath_mp3="final.mp3") 
    
#     return speech_to_text_output, doctor_response, "final.mp3"


# # 📁 Load CSS from external file
# def load_css(file_path):
#     """Load CSS from external file"""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"⚠️ Warning: CSS file '{file_path}' not found. Using default styling.")
#         return ""
#     except Exception as e:
#         print(f"⚠️ Error loading CSS: {e}")
#         return ""

# # Load the CSS
# custom_css = load_css('style.css')

# # 🏥 Banner HTML
# banner_html = """
# <div class="banner-container">
#     <div class="medical-icon">🩺</div>
#     <h1 class="banner-title">AI Medical Assistant</h1>
#     <p class="banner-subtitle">Professional medical insights through advanced AI analysis</p>
    
#     <div class="steps-container">
#         <div class="step-card">
#             <div class="step-number">1</div>
#             <div class="step-title">Upload Medical Image</div>
#             <div class="step-description">
#                 Share a clear photograph of the medical condition or area requiring analysis
#             </div>
#         </div>
        
#         <div class="step-card">
#             <div class="step-number">2</div>
#             <div class="step-title">Voice Description</div>
#             <div class="step-description">
#                 Describe your symptoms or concerns using the microphone for detailed analysis
#             </div>
#         </div>
        
#         <div class="step-card">
#             <div class="step-number">3</div>
#             <div class="step-title">Receive Analysis</div>
#             <div class="step-description">
#                 Get comprehensive medical insights and recommendations from our AI system
#             </div>
#         </div>
#     </div>
    
#     <div class="features-badges">
#         <div class="feature-badge">Medical Analysis</div>
#         <div class="feature-badge">Voice Recognition</div>
#         <div class="feature-badge">Image Processing</div>
#         <div class="feature-badge">AI Consultation</div>
#     </div>
# </div>
# """

# # 📋 Requirements Notice HTML
# requirements_html = """
# <div class="requirements-notice">
#     <strong>📋 Important:</strong> Both medical image AND voice recording are required for complete analysis
# </div>
# """

# # 📋 Disclaimer HTML
# disclaimer_html = """
# <div class="disclaimer">
#     <strong>Medical Disclaimer:</strong> This AI assistant provides educational information only and should not replace professional medical consultation. Please consult qualified healthcare professionals for medical concerns and treatment decisions.
# </div>
# """

# # Create the interface with external CSS
# with gr.Blocks(css=custom_css, title="AI Medical Assistant", theme=gr.themes.Soft()) as iface:
#     # Banner Section
#     gr.HTML(banner_html)
    
#     # Requirements Notice
#     gr.HTML(requirements_html)
    
#     # Original Interface Structure
#     with gr.Row():
#         with gr.Column():
#             gr.Markdown("### Upload Medical Image")
#             image_input = gr.Image(type="filepath")
            
#             gr.Markdown("### Record Your Question")  
#             audio_input = gr.Audio(sources=["microphone"], type="filepath")
            
#             # Add submit button
#             submit_btn = gr.Button("Get Medical Analysis", variant="primary", size="lg")
            
#         with gr.Column():
#             gr.Markdown("### Analysis Results")
            
#             speech_output = gr.Textbox(label="Speech to Text")
#             doctor_output = gr.Textbox(label="Doctor's Response")
#             audio_output = gr.Audio(label="Temp.mp3")
    
#     # Disclaimer
#     gr.HTML(disclaimer_html)
    
#     # Connect function with button click
#     submit_btn.click(
#         fn=process_inputs,
#         inputs=[audio_input, image_input],
#         outputs=[speech_output, doctor_output, audio_output]
#     )

# # ✅ Make it work on Render
# import os
# # DEBUG PRINT to confirm port being used
# print("✅ Launching Gradio on host=0.0.0.0, port:", os.environ.get("PORT", 7681))

# iface.launch(
#     server_name="0.0.0.0",
#     server_port=int(os.environ.get("PORT", 7681))
# )



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
