from flask_backend.database import db

class DataStore(db.Model):
    __tablename__ = 'data_store'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<DataStore id={self.id} content={self.content}>"



def insert_data(content):
    new_entry = DataStore(content=content)
    db.session.add(new_entry)
    db.session.commit()

def query_data():
    result = DataStore.query.all()
    return [{"id": entry.id, "content": entry.content} for entry in result]