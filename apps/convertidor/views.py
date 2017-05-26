from django.shortcuts import render
from django.http import HttpResponse
import csv, re, collections

# Create your views here.
def bd(request):
    if request.method == 'POST':
        fields = {}
        first_field = True
        first_row = True
        first_col = True
        db = request.POST['db'].lower().replace(" ", "_")
        table = request.POST['table'].lower().replace(" ", "_")
        field_name = request.POST['field_name'].lower().replace(" ", "_")
        field_type = request.POST['field_type'].lower().replace(" ", "_")
        fields[field_name] = field_type
        fields = collections.OrderedDict()

        file = request.FILES['file']

        print("\n\nCREATE DATABASE {};".format(db))
        print("CREATE TABLE {} (".format(table))
        for fn,ft in fields.items():
            if first_field is True:
                print("\t{} {}".format(fn,ft))
                first_field = False
            else:
                print(",")
                print("\t{} {}".format(fn,ft))
        print(");")

        with open(file, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if first_row is True:
                    first_row = False
                    continue

                print("INSERT INTO {} VALUES (".format(table), end="")
                for col in row:
                    if first_col is True:
                        first_col = False
                        print(col, end="")
                    else:
                        print(", {}".format(col), end="")
                print(");")
                first_col = True

        return render(request, 'forms/form_BD_response.html')
    else:
        return render(request, 'forms/form_BD.html')
