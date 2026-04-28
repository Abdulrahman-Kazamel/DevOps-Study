


PS C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning> .\.venv\Scripts\activate


 .\project\newenv\Scripts\activate
 cd project
python manage.py runserver


nav navbar-nav navbar-right

style="top:310px; left:150px;" data-ls="offsetxin:0; durationin:2000; delayin:3000; easingin:easeOutElastic; rotatexin:90; transformoriginin:50% top 0; offsetxout:-400;"

```python
home = C:\Users\AbdulRahmanKazamel\AppData\Local\Programs\Python\Python313
include-system-site-packages = false
version = 3.13.1
executable = C:\Users\AbdulRahmanKazamel\AppData\Local\Programs\Python\Python313\python.exe
command = C:\Users\AbdulRahmanKazamel\AppData\Local\Programs\Python\Python313\python.exe -m venv C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\newenv
```


```powershell



C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\db\backends\utils.py:98: RuntimeWarning: Accessing the database during app initialization is discouraged. To fix this warning, avoid executing queries in AppConfig.ready() or when your app modules are imported.
  warnings.warn(self.APPS_NOT_READY_WARNING_MSG, category=RuntimeWarning)
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\servers\basehttp.py", line 48, in get_internal_wsgi_application
    return import_string(app_path)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\utils\module_loading.py", line 30, in import_string
    return cached_import(module_path, class_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\utils\module_loading.py", line 15, in cached_import
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\project\myproject\wsgi.py", line 16, in <module>
    application = get_wsgi_application()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\wsgi.py", line 13, in get_wsgi_application
    return WSGIHandler()
           ^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\handlers\wsgi.py", line 118, in __init__
    self.load_middleware()
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\handlers\base.py", line 40, in load_middleware
    middleware = import_string(middleware_path)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\utils\module_loading.py", line 30, in import_string
    return cached_import(module_path, class_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\utils\module_loading.py", line 15, in cached_import
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'livereload.middleware'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\management\commands\runserver.py", line 143, in inner_run
    handler = self.get_handler(*args, **options)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\contrib\staticfiles\management\commands\runserver.py", line 31, in get_handler
    handler = super().get_handler(*args, **options)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\management\commands\runserver.py", line 79, in get_handler
    return get_internal_wsgi_application()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\AbdulRahmanKazamel\OneDrive - ACT\Documents\GitHub\E-learning\.venv\Lib\site-packages\django\core\servers\basehttp.py", line 50, in get_internal_wsgi_application
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: WSGI application 'myproject.wsgi.application' could not be loaded; Error importing module.


```
