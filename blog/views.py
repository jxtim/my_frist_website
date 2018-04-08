from django.shortcuts import render

def home_page(request):
	if request.method == "POST":
		comment = request.POST.get("comment")
		user = request.POST.get('username')
		return render(request, 'blog/home_page.html', {'posted_comment': comment})
		
	if request.method == "GET":
		return render(request, 'blog/home_page.html')