import os
from datetime import datetime
from django.shortcuts import render
from app.settings import FILES_PATH


def file_list(request, date=None):
    template_name = 'index.html'
    ls_files = []
    files = os.listdir(FILES_PATH)
    if files:
        for file in files:
            path = os.path.join(FILES_PATH, file)
            ctime = datetime.fromtimestamp(os.path.getctime(path))
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            if date == ctime.date() or date == mtime.date():
                ls_files.append({'name': file,
                                 'ctime': ctime,
                                 'mtime': mtime,
                                 })
            elif not date:
                ls_files.append({'name': file,
                                 'ctime': ctime,
                                 'mtime': mtime,
                                 })
            else:
                continue
    context = {
        'files': ls_files,
        'date': date
    }
    return render(request, template_name, context)


def file_content(request, name):
    filename = os.path.join(FILES_PATH, name)
    with open(filename) as file:
        content = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

