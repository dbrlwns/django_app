from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image

import requests
from bs4 import BeautifulSoup



# Create your views here.
def tool_index(request):
    return render(request, 'tools/index.html')



from django.shortcuts import render

# Create your views here.
def tool_index(request):
    return render(request, 'tools/index.html')



from django.shortcuts import render

# Create your views here.
def tool_index(request):
    return render(request, 'tools/index.html')

def imgToPdf(request):
    if request.method == 'POST':
        image_files = request.FILES.getlist('images')
        image_files.sort(key=lambda f: f.name)
        images = []
        for image in image_files:
            img = Image.open(image)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)

        if not images:
            return HttpResponse("<script>alert('이미지를 선택해주세요.'); history.back();</script>")
        output = BytesIO()
        images[0].save(output, format="PDF", save_all=True, append_images=images[1:])
        output.seek(0)

        response = HttpResponse(output, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="merged.pdf"'
        return response
    return render(request, 'tools/imgToPdf.html')



def crawling(request):
    result = None
    if request.method == 'POST':
        url = request.POST.get('url')
        keyword = request.POST.get('keyword')
        try:
            res = requests.get('https://' + url)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'html.parser')
            elements = soup.find_all(keyword)
            if elements:
                extracted = [element.get_text() for element in elements]
                result = "<br>".join(extracted)
            else:
                result = "keyword is not exist"
        except Exception as e:
            result = f"에러 {e}"
    content = {
        'result' : result,
    }
    return render(request, 'tools/crawling.html', content)



import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def ai_view(request):
    result = None
    if request.method == 'POST':
        user_input = request.POST.get('query')
        if user_input:
            result = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            ).text


    return render(request, 'tools/geminiBot.html', {'result': result})
