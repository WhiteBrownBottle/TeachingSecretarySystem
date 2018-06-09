import xadmin
from .models import EduProject, EduMidTerm, EduConclusion
# Register your models here.

class EduProjectAdmin(object):

    list_display = ['eduproject_id', 'eduproject_name', 'eduproject_belong_unit', 'eduproject_type', 'eduproject_person_in_charge']

    search_fields = ['eduproject_id', 'eduproject_name', 'eduproject_belong_unit', 'eduproject_type','eduproject_person_in_charge']

    list_filter = ['eduproject_id', 'eduproject_name', 'eduproject_belong_unit', 'eduproject_type', 'eduproject_person_in_charge']


class EduMidTermAdmin(object):

    list_display = ['eduproject_belong', 'edumidterm_file_name', 'edumidterm_deadline_date', 'edumidterm_check_status']

    search_fields = ['eduproject_belong', 'edumidterm_file_name', 'edumidterm_deadline_date', 'edumidterm_check_status']

    list_filter = ['eduproject_belong', 'edumidterm_file_name', 'edumidterm_deadline_date', 'edumidterm_check_status']


class EduConclusionAdmin(object):

    list_display = ['eduproject_belong', 'educonclusion_file_name', 'educonclusion_deadline_date', 'educonclusion_check_status']

    search_fields = ['eduproject_belong', 'educonclusion_file_name', 'educonclusion_deadline_date', 'educonclusion_check_status']

    list_filter = ['eduproject_belong', 'educonclusion_file_name', 'educonclusion_deadline_date', 'educonclusion_check_status']


xadmin.site.register(EduProject, EduProjectAdmin)
xadmin.site.register(EduMidTerm, EduMidTermAdmin)
xadmin.site.register(EduConclusion, EduConclusionAdmin)