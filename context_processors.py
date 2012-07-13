from .models import current_options

def options_cp(request):
    options = current_options()
    return {'options':options} if options else {}

