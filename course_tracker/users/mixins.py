from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class LoginRequiredWithMsgMixin(LoginRequiredMixin):
    message_no_auth = ''

    def dispatch(self, request, *args, **kwargs):
        messages.error(request, self.message_no_auth)
        return super().dispatch(request, *args, **kwargs)
