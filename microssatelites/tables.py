import django_tables2 as tables
from .models import ProjectData

class PersonTable(tables.Table):
    print(f'Teste {tables.Column()}')
    motif = tables.Column()
    dcount = tables.Column()
    iterations = tables.Column()
    consensus = tables.Column()
    lflanking = tables.Column()
    rflanking = tables.Column()
    cepa = tables.Column()

    class Meta:
        # model = ProjectData

        # fields = ("motif", "iterations", "cepa", )
        attrs={
            "class": "Persontable table-bordered",
        }
# <!-- {% load django_tables2 %}
# {% render_table table %}
# {% regroup cars by motif as newlist %} -->
#
# <!-- {{ newlist }}
#
# {% for x in newlist %}
# <h1>{{ x.grouper }}</h1>
# {% for y in x.list %}
# <p>{{ y.model }}: {{ y.year }}</p>
# {% endfor %}
# {% endfor %} -->
#
# <!-- <p>Check out views.py to see what the cars list looks like.</p>
# {% for d in dict_agroup %} -->
