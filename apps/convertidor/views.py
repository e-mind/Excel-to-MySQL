from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv, re, collections

# Create your views here.
def bd(request):
    if request.method == 'POST':
        fields = collections.OrderedDict()
        first_field = True
        first_row = True
        first_col = True
        db = request.POST['db'].lower().strip().replace(" ", "_")
        table = request.POST['table'].lower().strip().replace(" ", "_")
        field_name = request.POST.getlist('field_name[]')
        field_type = request.POST.getlist('field_type[]')

        for field in field_name:
            fn = field.lower().strip().replace(" ", "_")
            ft = field_type[field_name.index(field)].lower().strip().replace(" ", "_")
            fields[fn] = ft

        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        sql = ""
        sql += "CREATE DATABASE {};".format(db)
        sql += "\nUSE {};".format(db)
        sql += "\nCREATE TABLE {} (".format(table)
        for fn,ft in fields.items():
            if first_field is True:
                sql += "\n\t{} {}".format(fn,ft)
                first_field = False
            else:
                sql += ","
                sql += "\n\t{} {}".format(fn,ft)
        sql += "\n);"

        with open(settings.MEDIA_ROOT + file.name, encoding='utf-8', newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if first_row is True:
                    first_row = False
                    continue

                sql += "\nINSERT INTO {} VALUES (".format(table)
                for col in row:
                    if first_col is True:
                        first_col = False
                        sql += col
                    else:
                        sql += ", {}".format(col)
                sql += ");"
                first_col = True

        file_name, file_extension = file.name.split(".")
        new_file = file_name + "_SQL.sql"
        with open(settings.MEDIA_ROOT + new_file, 'w', encoding='utf-8', newline='') as f:
            f.write(sql)

        return render(request, 'forms/form_BD_response.html', {'sql' : sql, 'new_file' : new_file})
    else:
        return render(request, 'forms/form_BD.html')
