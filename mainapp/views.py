from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = {'name':" Arif python",'country':' bd','desig':' python Developer'}#Avabeu kora jai.
        # context['name']=" Arif python"
        # context['country']=" Bangladesh"
        # context['desig']=" Python Programmer "
        list=[1,2,3,4,5,6]
        context['list']=list
        return context

class  AboutView(TemplateView):
     template_name='about.html'
