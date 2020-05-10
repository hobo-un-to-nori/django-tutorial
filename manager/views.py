'''
views
'''

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from manager.models import Worker, Person

get_object_or_404(Person, id=20)
class WorkerListView(TemplateView):
    '''
    wokerの表示をするクラス
    '''
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all()  # データベースからオブジェクトを取得して
        context['workers'] = workers  # 入れ物に入れる

        return render(self.request, self.template_name, context)
        