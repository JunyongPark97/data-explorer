
class DataManagementRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'data_management':
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        return 'data_management'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'data_management':
            return True
        return None
