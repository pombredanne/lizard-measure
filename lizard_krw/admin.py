from django.contrib import admin

from lizard_krw.models import AlphaScore
from lizard_krw.models import Color
from lizard_krw.models import Executive
from lizard_krw.models import FundingOrganization
from lizard_krw.models import GoalScore
from lizard_krw.models import KRWWaterType
from lizard_krw.models import Measure
from lizard_krw.models import MeasureCategory
from lizard_krw.models import MeasureCode
from lizard_krw.models import MeasurePeriod
from lizard_krw.models import MeasureStatus
from lizard_krw.models import MeasureStatusMoment
from lizard_krw.models import Organization
from lizard_krw.models import Score
from lizard_krw.models import SingleIndicator
from lizard_krw.models import Unit
from lizard_krw.models import WaterBody
from lizard_krw.models import XMLImport
from lizard_krw.models import XMLImportMeetobject


class SingleIndicatorInline(admin.TabularInline):
    model = SingleIndicator


class MeasureStatusMomentInline(admin.TabularInline):
    model = MeasureStatusMoment


class FundingOrganizationInline(admin.TabularInline):
    model = FundingOrganization


class WaterBodyAdmin(admin.ModelAdmin):
    inlines = [
        SingleIndicatorInline,
        ]


class ScoreAdmin(admin.ModelAdmin):
    list_filter = ['waterbody', ]


class MeasureAdmin(admin.ModelAdmin):
    list_filter = ['waterbody', ]
    inlines = [
        MeasureStatusMomentInline, FundingOrganizationInline,
        ]


admin.site.register(AlphaScore)
admin.site.register(Color)
admin.site.register(Executive)
admin.site.register(FundingOrganization)
admin.site.register(GoalScore, ScoreAdmin)
admin.site.register(KRWWaterType)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(MeasureCategory)
admin.site.register(MeasureCode)
admin.site.register(MeasurePeriod)
admin.site.register(MeasureStatus)
admin.site.register(MeasureStatusMoment)
admin.site.register(Organization)
admin.site.register(Score, ScoreAdmin)
admin.site.register(SingleIndicator)
admin.site.register(Unit)
admin.site.register(WaterBody, WaterBodyAdmin)
admin.site.register(XMLImport)
admin.site.register(XMLImportMeetobject)