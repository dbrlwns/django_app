from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image


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



