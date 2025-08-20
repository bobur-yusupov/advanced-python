from django.shortcuts import render, redirect
from .models import Image
from django.contrib import messages
from .forms import ImageForm
from .tasks import process_image

# Create your views here.
def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            process_image.delay(form.instance.id)
            messages.success(request, "Your file is being processed in the background!")
            return redirect('upload')
        else:
            messages.error(request, 'Failed to upload image.')
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})
