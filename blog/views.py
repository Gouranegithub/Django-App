from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import POST
from django.views.generic import ListView ,DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User







def about(request):
    return  HttpResponse(render(request, 'blog/about.html', {'title':'about'})) #u don't have to add HttpResponse() it was used when we write directly the html code here


 
 

def home(request):
    context={
        'posts': POST.objects.all(),
        
    }
    return render(request, 'blog/home.html',context) 

#we're not using the using the home view anymore but now we are using this class 

class UserPostListView(ListView):
    model =POST
    template_name = 'blog/user_post.html'
    context_object_name= 'posts'
    paginate_by =5
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username') )
        return  POST.objects.filter(author =user).order_by('-date')
    
    
    
class PostListView(ListView):
    model =POST
    template_name = 'blog/home.html'
    context_object_name= 'posts'
    ordering = ['-date']
    paginate_by =5

#this class : postdetailview will be for an individual post 

class PostDetailView(DetailView):
    model =POST
    


class PostCreateView(LoginRequiredMixin , CreateView):
    model =POST
    fields = [ 'title' ,'content']
    
    def form_valid(self , form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
    
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model =POST
    fields = [ 'title' ,'content']
    
    def form_valid(self , form):
        form.instance.author= self.request.user
        return super().form_valid(form)    


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
        
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
    model =POST
    template_name = 'blog/post_delete.html'
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
