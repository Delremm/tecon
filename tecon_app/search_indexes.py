import datetime
from haystack import indexes
from tecon_app.models import Trial


class TrialIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Trial

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            created__lte=datetime.datetime.now())
