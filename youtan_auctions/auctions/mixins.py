from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PrefetchedSerializer:
    """
    Mixin to optimize nested serializers
    """

    @staticmethod
    def select_related_queryset(queryset, args):
        queryset = queryset.select_related(*args)
        return queryset

    @staticmethod
    def prefetch_related_queryset(queryset, args):
        queryset = queryset.prefetch_related(*args)
        return queryset


class AdminMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to verify if user is admin.
    """

    def test_func(self):
        user = self.request.user
        return user.is_superuser