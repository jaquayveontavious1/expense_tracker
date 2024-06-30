from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ExpensesForm
from .models import Expenses

from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#@login_required
#def delete_expense(request , pk) :
    #expense = get_object_or_404(DeleteExpense,pk=pk,username=request.user)
    #if request.method == "POST" :
        #expense.delete()
        #messages.success(request,'Successfull')
        #return redirect('expenses:list')
    
    
    #return render(request,'expenses/delete_expense.html',{
       # 'expense' : expense
    #})

#@login_required
#def edit_expense(request,pk) :
   # print("edit_expense view called")
 
    #try :

        #expense = get_object_or_404(EditExpense,pk=pk,username=request.user)
       # print(f"Fetched expense : {expense}")
    #except Exception as e :
        #print(f"Error fetching entry:{e} ")
        #messages.error(request,"Expense not found")
        #return redirect('expenses:list')
   # if request.method == 'POST' :
        #form = EditForm(request.POST,instance=expense)
        #print(request.POST)
        #print('POST request received')
        #if form.is_valid() :
           # form.save()
           # messages.success(request,'Expense successfully edited')
           # return redirect('expenses:list')

       # else :
            #messages.error(request,'Error in editing expense details')
   # else :
       # form = EditForm(instance=expense)
       # print('GET request received,rendering form')
   # return render(request,'expenses/edit_expense.html',{
        #'form' : form
   # })


#@login_required
#def add_expense(request) :
    #if request.method == "POST" :
      #  form = Expenses(request.POST)
       # print(request.POST)
        #if form.is_valid() :
        #    expense = form.save(commit=False)
         #   expense.username = request.user
          #  expense.save()
          #  messages.success(request,'Expense added successfully')
          #  return redirect('expenses:list')
            
        #else :
           # messages.error(request,'Please correct the errors below')    
    #else :
      #  form = Expenses()
   # return render(request,'expenses/add_expense.html',{'form': form})
#@login_required
#def list_view(request) :
    #expenses = Expenses.objects.filter(username=request.user)


    #return render(request,'expenses/list_expenses.html',{'expenses' : expenses})
class ExpenseListView(LoginRequiredMixin,ListView) :
    model = Expenses
    template_name = 'expenses/list_expenses.html'
    context_object_name = 'expenses'
    def get_queryset(self) :
        return Expenses.objects.filter(username=self.request.user)

class ExpenseCreateView(LoginRequiredMixin,CreateView) :
    model = Expenses
    form_class = ExpensesForm
    template_name = 'expenses/add_expense.html'
    success_url = reverse_lazy('expenses:list')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin,UpdateView) :
    model = Expenses
    form_class = ExpensesForm
    template_name = 'expenses/add_expense.html'
    success_url = reverse_lazy('expenses:list')

    def get_queryset(self):
        return Expenses.objects.filter(username=self.request.user)
    

class ExpenseDeleteView(LoginRequiredMixin,DeleteView) :
    model = Expenses
    template_name = 'expenses/delete_expense.html'
    success_url = reverse_lazy('expenses:list')

    def get_queryset(self) :
        return Expenses.objects.filter(username=self.request.user)
    


class SignUpView(CreateView) :
    form_class = UserCreationForm   
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
#def register (request) :
    #if request.method == "POST" :
      #  form = UserRegisterForm(request.POST)
      #  if form.is_valid() :
          #  form.save()
      #      username = form.cleaned_data.get('username')
          #  messages.success(request,f"Account created for {username}")
          #  return redirect('login')
     #   else :
     #       form = UserRegisterForm()

       # return render(request,'expenses/register.html', {
       #     'form' : form
      #  })
def Login(request) :
    form = LoginForm()
    context = {'form' : form}
    return render(request,'trial/log.html',context)

#def login_view (request) :
    if request.method == "POST" :
        form = UserLoginForm(request,date=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('home')
            else :
                messages.error(request,'Invalid username or password')
        else :
            messages.error(request,'Invalid username or password')
    else :
        form = UserLoginForm()
    return render(request,'expenses/login.html',{'form' : form})



    
# Create your views here.
