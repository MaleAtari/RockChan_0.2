from app import create_app, db
from app.models import Users, Posts, Board

app = create_app()
app.app_context().push()




# ### Make Admin
# admin = Users(name='admin', password='123', role=1)
# db.session.add(admin)
# db.session.commit()

# ### Make Moderator
# moderator = Users(name='mod', password='123', role=3)
# db.session.add(moderator)
# db.session.commit()

# ### Make Fake Admin
# fake_admin = Users(name='fake', password='123', role=7)
# db.session.add(fake_admin)
# db.session.commit()

#######################################################

# ### Make Board
# board1 = Board(name='Pierwszy temat', info='pierwszy założony temat. Tutaj piszemy', user_id=1)
# db.session.add(board1)
# db.session.commit()

# ### Make Second Board
# board2 = Board(name='Inny Temat', info='Jakies kacapoły', user_id=2)
# db.session.add(board2)
# db.session.commit()

# ### Make Third Board (closed)
# board3 = Board(name='Na test', info='To bedzie temat testowy', user_id=1)
# board3.open = False
# db.session.add(board3)
# db.session.commit()

# ### Make Board to Close
# board4 = Board(name='Smieci', info='jakies smieci', user_id=2)
# db.session.add(board4)
# db.session.commit()


