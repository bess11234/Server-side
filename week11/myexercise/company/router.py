class CompanyRouter:
    def db_for_read(self, model, **hints):
        return
    def db_for_write(self, model, **hints):
        return
    def allow_relation(self, obj1, obj2, **hints):
        return
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return