from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    param = request.GET.get('from-landing')
    if param == 'original':
        counter_click['original'] += 1
    elif param == 'test':
        counter_click['test'] += 1
    else:
        pass
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    param = request.GET.get('ab-test-arg')
    if param == 'original':
        url = 'landing.html'
        counter_show['original'] += 1
    elif param == 'test':
        url = 'landing_alternate.html'
        counter_show['test'] += 1
    else:
        url = 'landing_alternate.html'
        counter_show['test'] += 1
    return render_to_response(url)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    if counter_show['original']:
        original_conversion = counter_click['original'] / counter_show['original']
    else:
        original_conversion = 0
    if counter_show['test']:
        test_conversion = counter_click['test'] / counter_show['test']
    else:
        test_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': round(test_conversion, 2),
        'original_conversion': round(original_conversion, 2),
    })
