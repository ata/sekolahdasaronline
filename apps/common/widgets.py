import datetime
from django.forms.extras.widgets import SelectDateWidget

class SelectDateBirthWidget(SelectDateWidget):
    
    def __init__(self, attrs=None, required=True):
        this_year = datetime.date.today().year
        years = range(this_year - 100, this_year - 3)
        years.reverse()
        super(SelectDateBirthWidget, self).__init__(attrs, years, required)
