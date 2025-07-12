from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, PredictionHistory
from .forms import ImageUploadForm
from django.conf import settings
import torch
from torchvision import models, transforms
from PIL import Image
import os

@login_required
def predict_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            if profile.tokens < 3:
                return render(request, 'no_tokens.html')
            image = form.cleaned_data['image']
            img_path = os.path.join(settings.MEDIA_ROOT, 'tmp', image.name)
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            with open(img_path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            img = Image.open(img_path).convert('RGB')
            transform = transforms.Compose([
                transforms.Resize((128, 128)),
                transforms.ToTensor(),
            ])
            img_tensor = transform(img).unsqueeze(0)
            model = models.resnet18()
            model.fc = torch.nn.Linear(model.fc.in_features, 1)
            model.load_state_dict(torch.load(os.path.join(settings.BASE_DIR, 'cat_dog_resnet18.pth'), map_location='cpu'))
            model.eval()
            with torch.no_grad():
                output = model(img_tensor)
                pred = torch.sigmoid(output).item()
            result = 'Dog' if pred > 0.5 else 'Cat'
            PredictionHistory.objects.create(user=request.user, image=image, result=result)
            profile.tokens -= 3
            profile.save()
            return render(request, 'result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})