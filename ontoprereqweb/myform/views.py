from django.shortcuts import render
import PrereqChainService

def index(request):
    if request.method == 'POST':
        my_variable = request.POST.get('my_field', '')
        a = PrereqChainService.PrereqChainService()

        # Отправление запроса для построения пререквизитной цепочки
        prereq_count = a.prereq_count()
        a.chain_build(my_variable)
        processed_variable = a.chain_to_var()  # Вывод пререквизитной цепочки

        return render(request, 'myform/index.html', {'prereq_count': prereq_count, 'processed_variable': processed_variable})
    else:
        return render(request, 'myform/index.html')
