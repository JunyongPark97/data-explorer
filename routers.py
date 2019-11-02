
class DataExplorerRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('data_management', 'mondebro', 'web_crawler', 'monde'):
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ('data_management', 'mondebro', 'web_crawler'):
            return model._meta.app_label
        else:
            return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
