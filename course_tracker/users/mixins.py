from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        AccessMixin,
                                        UserPassesTestMixin)
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect, reverse


class LoginRequiredWithMsgMixin(LoginRequiredMixin):
    message_no_auth = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.message_no_auth)
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)


class EditMixin(AccessMixin):
    messages_no_access = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != kwargs['pk']:
            messages.error(request, self.messages_no_access)
            return super().dispatch(request, *args, **kwargs)


class OnlyAuthorAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, _('You have no access to the object'))
        return redirect(reverse('home'))


class OnlyAuthorAccessIfPrivateMixin(OnlyAuthorAccessMixin):
    def test_func(self):
        if self.get_object().public:
            return True
        return super().test_func()
