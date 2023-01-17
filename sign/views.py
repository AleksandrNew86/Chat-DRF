from django.views.generic.edit import CreateView, UpdateView
from .models import Writer
from .forms import WriterForm
from django.urls import reverse_lazy


class CreateWriter(CreateView):
    form_class = WriterForm
    model = Writer
    template_name = 'sign/create_writer.html'

    def form_valid(self, form):
        m_writer = form.save(commit=False)
        m_writer.writer = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('room')


class UpdateWriter(UpdateView):
    model = Writer
    form_class = WriterForm
    template_name = 'sign/create_writer.html'
    success_url = reverse_lazy('room')