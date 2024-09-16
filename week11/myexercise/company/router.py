class CompanyRouter:
    route_app = {"company"} # APP
    database = "company_db" # DATABASE
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app:
            return self.database
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app:
            return self.database
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app or obj1._meta.app_label in self.route_app:
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app:
            return db == self.database
        return None