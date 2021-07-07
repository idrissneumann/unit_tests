class TodoModelGenerator():
    db = None

    def __init__(self, db):
        self.db = db

    def get_model(self):
        class Todo(self.db.Model):
            __tablename__ = "todos"
            id = self.db.Column(self.db.Integer, primary_key=True)
            title = self.db.Column(self.db.String(20))
            todo_description = self.db.Column(self.db.String(100))

            def create(self):
                self.db.session.add(self)
                self.db.session.commit()
                return self

            def __init__(self, title, todo_description):
                self.title = title
                self.todo_description = todo_description

            def __repr__(self):
                return f"{self.id}"
        return Todo
