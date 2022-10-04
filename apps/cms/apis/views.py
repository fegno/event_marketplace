from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.cms.apis.serializers import (
    AssistCategorySerializer, AssistSubCategorySerializer, AssistSerializer, AssistQuestionSerializer,
    ProtectCategorySerializer, ProtectSerializer, ProtectOptionSerializer, TagSerializer, CoreCategorySerializer,
    ContentLevelSerializer, UserLevelSerializer, ContentTypeSerializer, ContentIndustrySerializer,
    ToolkitCategorySerializer, NewsfeedCategorySerializer, RoleSerializer, TaxSlabSerializer, ModeOfPaymentSerializer,
    CurrencySerializer, DurationSerializer, PolicySerializer, ToolkitSerializer, NewsFeedSerializer,
    QuestionEmailTemplateSerializer, QuestionSerializer, QuestionOptionSerializer, AssessmentQuestionMapSerializer,
    AssessmentSerializer, AwarenessVideoSerializer, AwarenessVideoTipSerializer, PaymentTermSerializer,
    QuestionCreateSerializer)
from apps.cms.models import (
    AssistCategory, AssistSubCategory, Assist, AssistQuestion, ProtectCategory, Protect, ProtectOption, Tag,
    CoreCategory, ContentLevel, UserLevel, ContentType, ContentIndustry, ToolkitCategory, NewsfeedCategory, Role,
    TaxSlab, ModeOfPayment, Currency, Duration, Policy, Toolkit, NewsFeed, QuestionEmailTemplate, Question,
    QuestionOption, AssessmentQuestionMap, Assessment, AwarenessVideo, AwarenessVideoTip, PaymentTerm)
from django_filters.views import FilterView


class AssistCategoryViewSet(ModelViewSet, FilterView):
    queryset = AssistCategory.objects.order_by('pk')
    serializer_class = AssistCategorySerializer
    filterset_fields = []


class AssistSubCategoryViewSet(ModelViewSet, FilterView):
    queryset = AssistSubCategory.objects.order_by('pk')
    serializer_class = AssistSubCategorySerializer
    filterset_fields = []


class AssistViewSet(ModelViewSet, FilterView):
    queryset = Assist.objects.order_by('pk')
    serializer_class = AssistSerializer
    filterset_fields = []


class AssistQuestionViewSet(ModelViewSet, FilterView):
    queryset = AssistQuestion.objects.order_by('pk')
    serializer_class = AssistQuestionSerializer
    filterset_fields = []


class ProtectCategoryViewSet(ModelViewSet, FilterView):
    queryset = ProtectCategory.objects.order_by('pk')
    serializer_class = ProtectCategorySerializer
    filterset_fields = []


class ProtectViewSet(ModelViewSet, FilterView):
    queryset = Protect.objects.order_by('pk')
    serializer_class = ProtectSerializer
    filterset_fields = []


class ProtectOptionViewSet(ModelViewSet, FilterView):
    queryset = ProtectOption.objects.order_by('pk')
    serializer_class = ProtectOptionSerializer
    filterset_fields = []


class TagViewSet(ModelViewSet, FilterView):
    queryset = Tag.objects.order_by('pk')
    serializer_class = TagSerializer
    filterset_fields = []


class CoreCategoryViewSet(ModelViewSet, FilterView):
    queryset = CoreCategory.objects.order_by('pk')
    serializer_class = CoreCategorySerializer


class ContentLevelViewSet(ModelViewSet, FilterView):
    queryset = ContentLevel.objects.order_by('pk')
    serializer_class = ContentLevelSerializer
    filterset_fields = []


class UserLevelViewSet(ModelViewSet, FilterView):
    queryset = UserLevel.objects.order_by('pk')
    serializer_class = UserLevelSerializer
    filterset_fields = []


class ContentTypeViewSet(ModelViewSet, FilterView):
    queryset = ContentType.objects.order_by('pk')
    serializer_class = ContentTypeSerializer
    filterset_fields = []


class ContentIndustryViewSet(ModelViewSet, FilterView):
    queryset = ContentIndustry.objects.order_by('pk')
    serializer_class = ContentIndustrySerializer
    filterset_fields = []


class ToolkitCategoryViewSet(ModelViewSet, FilterView):
    queryset = ToolkitCategory.objects.order_by('pk')
    serializer_class = ToolkitCategorySerializer
    filterset_fields = []


class NewsfeedCategoryViewSet(ModelViewSet, FilterView):
    queryset = NewsfeedCategory.objects.order_by('pk')
    serializer_class = NewsfeedCategorySerializer
    filterset_fields = []


class RoleViewSet(ModelViewSet, FilterView):
    queryset = Role.objects.order_by('pk')
    serializer_class = RoleSerializer
    filterset_fields = []


class TaxSlabViewSet(ModelViewSet):
    queryset = TaxSlab.objects.order_by('pk')
    serializer_class = TaxSlabSerializer
    filterset_fields = []


class ModeOfPaymentViewSet(ModelViewSet):
    queryset = ModeOfPayment.objects.order_by('pk')
    serializer_class = ModeOfPaymentSerializer
    filterset_fields = []


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.order_by('pk')
    serializer_class = CurrencySerializer
    filterset_fields = []


class DurationViewSet(ModelViewSet):
    queryset = Duration.objects.order_by('pk')
    serializer_class = DurationSerializer
    filterset_fields = []


class PolicyViewSet(ModelViewSet):
    queryset = Policy.objects.order_by('pk')
    serializer_class = PolicySerializer
    filterset_fields = []


class ToolkitViewSet(ModelViewSet):
    queryset = Toolkit.objects.order_by('pk')
    serializer_class = ToolkitSerializer
    filterset_fields = []


class NewsFeedViewSet(ModelViewSet):
    queryset = NewsFeed.objects.order_by('pk')
    serializer_class = NewsFeedSerializer
    filterset_fields = []


class QuestionEmailTemplateViewSet(ModelViewSet):
    queryset = QuestionEmailTemplate.objects.order_by('pk')
    serializer_class = QuestionEmailTemplateSerializer
    filterset_fields = []


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.filter(is_child=False).order_by('pk')
    serializer_class = QuestionSerializer
    filterset_fields = []

    def create(self, request, *args, **kwargs):
        # request.data
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Created', status=201)
        return Response(serializer.errors, status=403)


class QuestionOptionViewSet(ModelViewSet):
    queryset = QuestionOption.objects.order_by('pk')
    serializer_class = QuestionOptionSerializer
    filterset_fields = []


class AssessmentQuestionMapViewSet(ModelViewSet):
    queryset = AssessmentQuestionMap.objects.order_by('pk')
    serializer_class = AssessmentQuestionMapSerializer
    filterset_fields = []


class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.order_by('pk')
    serializer_class = AssessmentSerializer


class AwarenessVideoViewSet(ModelViewSet, FilterView):
    queryset = AwarenessVideo.objects.order_by('pk')
    serializer_class = AwarenessVideoSerializer
    filterset_fields = []


class AwarenessVideoTipViewSet(ModelViewSet, FilterView):
    queryset = AwarenessVideoTip.objects.order_by('pk')
    serializer_class = AwarenessVideoTipSerializer
    filterset_fields = []

class PaymentTermViewSet(ModelViewSet, FilterView):
    queryset = PaymentTerm.objects.order_by('pk')
    serializer_class = PaymentTermSerializer
    filterset_fields = []