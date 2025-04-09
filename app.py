from flask import Flask, request, send_file, render_template_string
import os
import uuid
import yt_dlp
from PIL import Image

app = Flask(__name__)


UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    
    with open('templates/index.html', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route("/convert-youtube", methods=["POST"])
def convert_youtube():
    link = request.form['yt_link']
    format_ = request.form['format']
    
    
    ydl_opts = {
        'format': 'bestaudio/best' if format_ == 'mp3' else 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(UPLOAD_FOLDER, '%(id)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_filename = ydl.prepare_filename(info_dict)
            
            if format_ == "mp3":
               
                mp3_filename = video_filename.rsplit('.', 1)[0] + '.mp3'
                os.rename(video_filename, mp3_filename)
                return send_file(mp3_filename, as_attachment=True)
            else:
                return send_file(video_filename, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

@app.route("/convert-image", methods=["POST"])
def convert_image():
    file = request.files['image_file']
    target_format = request.form['target_format']
    ext = target_format.lower()

   
    filename = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_FOLDER, filename + ".input")
    output_path = os.path.join(UPLOAD_FOLDER, filename + "." + ext)

   
    file.save(input_path)
    try:
        with Image.open(input_path) as img:
            
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

           
            if ext == "jpg":
                img.save(output_path, format="JPEG")
            else:
                img.save(output_path, format=ext.upper()) 

    except Exception as e:
        return f"Error: {e}"

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
