from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogModel
from .forms import BlogForm


def blogs_list_view(request):
    """Get blogs list view"""
    # Fetch all blogs in sorted by published date
    blogs = BlogModel.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    # Render blogs list view
    return render(request, "blog/blog_list.html", {"blogs": blogs, "total_blogs": blogs.count()})


def blogs_detail_view(request, pk):
    """Get blogs detail view"""
    # Fetch all blogs
    blog = get_object_or_404(BlogModel, pk=pk)
    # Render detail blog view template
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def create_new_blog(request):
    """Create a new blog."""
    if request.method == "POST":
        # Get blog data from POST request
        blog_form = BlogForm(request.POST)
        # Validate data from post request
        if blog_form.is_valid():
            # Save blog form data
            blog = blog_form.save(commit=False)
            # Set blog author name from logged in user
            blog.author = request.user
            # Set blog publication date
            blog.published_date = timezone.now()
            # Save blog detail data to database
            blog.save()
            # Redirect to blog detail view
            return redirect('blog_detail_view', pk=blog.pk)
    else:
        blog_form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': blog_form})


def edit_blog(request, pk):
    """Edit blog"""
    # Get blog data if found else throw 404 not found exception
    blog = get_object_or_404(BlogModel, pk=pk)
    if blog.author != request.user:
        return render(request, 'errors/401.html')

    if request.method == "POST":
        # Update old form data with the data from post request
        blog_form = BlogForm(request.POST, instance=blog)
        # Validate blog form data
        if blog_form.is_valid():
            # Save blog form data
            post = blog_form.save(commit=False)
            # Set blog author
            post.author = request.user
            # Set blog publication date
            post.published_date = timezone.now()
            # Save blog detail data to database
            post.save()
            # Redirect to blog detail view
            return redirect('blog_detail_view', pk=post.pk)
    else:
        blog_form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': blog_form, 'blog': blog})


def delete_blog(request, pk):
    """Delete blog"""
    # Get the blog
    blog = get_object_or_404(BlogModel, pk=pk)
    # Validate if logged in used is the author of the blog
    if blog.author != request.user:
        return render(request, 'errors/401.html')
    # Delete blog if logged in user is the author of the blog
    blog.delete()
    # Redirect to home page
    return HttpResponseRedirect('/')
