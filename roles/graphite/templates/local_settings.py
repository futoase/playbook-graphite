# based on https://github.com/graphite-project/graphite-web/blob/master/webapp/graphite/local_settings.py.example

TIME_ZONE = 'Asia/Tokyo'

DATABASES = {
  'default': {
    'NAME': 'graphite',
    'ENGINE': 'django.db.backends.mysql',
    'USER': '{{ graphite.username }}',
    'PASSWORD': '{{ graphite.password }}',
    'HOST': 'localhost',
    'PORT': '3306'
  }
}
