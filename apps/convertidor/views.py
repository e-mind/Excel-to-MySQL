from django.shortcuts import render
from django.http import HttpResponse
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

        for key, value in fields.items():
            print(key, value)

        # file = request.FILES['file']

    #     print("\n\nCREATE DATABASE {};".format(db))
    #     print("CREATE TABLE {} (".format(table))
    #     for fn,ft in fields.items():
    #         if first_field is True:
    #             print("\t{} {}".format(fn,ft))
    #             first_field = False
    #         else:
    #             print(",")
    #             print("\t{} {}".format(fn,ft))
    #     print(");")
    #
    #     with open(file, newline='') as f:
    #         reader = csv.reader(f, delimiter=';')
    #         for row in reader:
    #             if first_row is True:
    #                 first_row = False
    #                 continue
    #
    #             print("INSERT INTO {} VALUES (".format(table), end="")
    #             for col in row:
    #                 if first_col is True:
    #                     first_col = False
    #                     print(col, end="")
    #                 else:
    #                     print(", {}".format(col), end="")
    #             print(");")
    #             first_col = True
    #
        return render(request, 'forms/form_BD_response.html')
    else:
        return render(request, 'forms/form_BD.html')
