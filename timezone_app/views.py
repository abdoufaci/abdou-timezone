from django.shortcuts import render
import datetime
import pytz


def home(request):
    return render(request, 'basetimezone.html')


def timezone_search(request):
    date = []
    da = []
    request.method
    search = request.POST.get('search')
    datetime_today = datetime.datetime.now(tz=pytz.UTC)
    datetime_worl = datetime_today.astimezone(pytz.timezone(search))
    datetime_world =datetime_worl.strftime('%H : %M : %S')
    for tz in pytz.all_timezones :
       da.append(tz)
    date.append(datetime_world)


    abdou_front_end = {
        'search': search,
        'date': date,
        'da': da
    }

    return render(request, 'my_app/timezonesearch.html', abdou_front_end)
