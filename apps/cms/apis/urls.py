from rest_framework.routers import SimpleRouter
from apps.cms.apis import views


router = SimpleRouter()

router.register(r'assistcategory', views.AssistCategoryViewSet)
router.register(r'assistsubcategory', views.AssistSubCategoryViewSet)
router.register(r'assist', views.AssistViewSet)
router.register(r'assistquestion', views.AssistQuestionViewSet)
router.register(r'protectcategory', views.ProtectCategoryViewSet)
router.register(r'protect', views.ProtectViewSet)
router.register(r'protectoption', views.ProtectOptionViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'corecategory', views.CoreCategoryViewSet)
router.register(r'contentlevel', views.ContentLevelViewSet)
router.register(r'userlevel', views.UserLevelViewSet)
router.register(r'contenttype', views.ContentTypeViewSet)
router.register(r'contentindustry', views.ContentIndustryViewSet)
router.register(r'toolkitcategory', views.ToolkitCategoryViewSet)
router.register(r'newsfeedcategory', views.NewsfeedCategoryViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'taxslab', views.TaxSlabViewSet)
router.register(r'modeofpayment', views.ModeOfPaymentViewSet)
router.register(r'currency', views.CurrencyViewSet)
router.register(r'duration', views.DurationViewSet)
router.register(r'policy', views.PolicyViewSet)
router.register(r'toolkit', views.ToolkitViewSet)
router.register(r'newsfeed', views.NewsFeedViewSet)
router.register(r'questionemailtemplate', views.QuestionEmailTemplateViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'questionoption', views.QuestionOptionViewSet)
router.register(r'assessmentquestionmap', views.AssessmentQuestionMapViewSet)
router.register(r'assessment', views.AssessmentViewSet)
router.register(r'awarenessvideo', views.AwarenessVideoViewSet)
router.register(r'awarenessvideotip', views.AwarenessVideoTipViewSet)
router.register(r'paymentterm', views.PaymentTermViewSet)

urlpatterns = router.urls
