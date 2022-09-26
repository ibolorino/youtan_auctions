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
