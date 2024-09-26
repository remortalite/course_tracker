from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib import messages


class LoginRequiredWithMsgMixin(LoginRequiredMixin):
    message_no_auth = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.message_no_auth)
        return super().dispatch(request, *args, **kwargs)


class EditMixin(AccessMixin):
    messages_no_access = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != kwargs['pk']:
            messages.error(request, self.messages_no_access)
            return super().dispatch(request, *args, **kwargs)
