
from app import app, db
db.create_all()
from app import User

result = User.query.all()

for res in result:
    print(res.name, res.email)