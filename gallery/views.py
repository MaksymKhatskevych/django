from django.shortcuts import render

from .models import Category, Photo


def images(request):
	categories = Category.objects.order_by('category')
	photos = Photo.objects.all()
	sort = request.GET.get('sorting')
	ctx = {'categories': categories}
	if sort == 'ALL PHOTOS':
		photos = Photo.objects.all()
		ctx['photos'] = photos
		return render(request, 'gallery/gallery.html', ctx)
	for category in categories:
		if category.category.upper() == sort:
			photos = Photo.objects.filter(category=category)
			ctx['photos'] = photos
			return render(request, 'gallery/gallery.html', ctx)
	ctx['photos'] = photos
	return render(request, 'gallery/gallery.html', ctx)