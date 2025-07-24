
from .models import PredictionHistory

def dashboard(request):
    history = PredictionHistory.objects.all().order_by('-created_at')[:10]
    return render(request, 'dashboard.html', {
        'history': history,
    })
from django.shortcuts import render
from django import forms
from PIL import Image
import os
from django.conf import settings

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

def index(request):
    result = None
    confidence = None
    image_url = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            # Save the uploaded image temporarily
            img_path = os.path.join(settings.MEDIA_ROOT, 'tmp', image.name)
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            with open(img_path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            # Dummy prediction logic (replace with real model inference)
            img = Image.open(img_path)
            width, height = img.size
            if width > height:
                result = 'Dog'
                confidence = 80.0
            else:
                result = 'Cat'
                confidence = 75.0

            # Save prediction history (no user association)
            from django.core.files.base import ContentFile
            from django.core.files.storage import default_storage
            image.seek(0)
            saved_path = default_storage.save(f"history_images/{image.name}", ContentFile(image.read()))
            PredictionHistory.objects.create(
                image=saved_path,
                prediction=result
            )
            image_url = default_storage.url(saved_path)
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form, 'result': result, 'confidence': confidence, 'image_url': image_url})
