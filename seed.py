from datetime import datetime, timedelta, timezone
from app import db, create_app
from app.models.user import User
from app.models.children_home import ChildrenHome, Child, Photo
from app.models.donation import Donation
from app.models.review import Review
from app.models.visit import Visit
from app.models.volunteer import Volunteer

app = create_app()     
def seed_database():
    with app.app_context():
      db.session.query(Volunteer).delete()
      db.session.query(Visit).delete()
      db.session.query(Review).delete()
      db.session.query(Donation).delete()
      db.session.query(Photo).delete()
      db.session.query(Child).delete()
      db.session.query(ChildrenHome).delete()
      db.session.query(User).delete()
      db.session.commit()
        
users = [
        User(name="Alice Johnson", email="alice.johnson@gmail.com", phone_number="+254 701 111 111", role="user",  created_at=datetime.now(timezone.utc)),
        User(name="Bob Smith", email="bob.smith@gmail.com", phone_number="+254 702 222 222", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Carol White", email="carol.white@gmail.com", phone_number="+254 703 333 333", role="user", created_at=datetime.now(timezone.utc)),
        User(name="David Brown", email="david.brown@gmail.com", phone_number="+254 704 444 444", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Emma Davis", email="emma.davis@gmail.com", phone_number="+254 705 555 555", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Frank Wilson", email="frank.wilson@gmail.com", phone_number="+254 706 666 666", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Grace Taylor", email="grace.taylor@gmail.com", phone_number="+254 707 777 777", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Henry Martinez", email="henry.martinez@gmail.com", phone_number="+254 708 888 888", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Isabella Anderson", email="isabella.anderson@gmail.com", phone_number="+254 709 999 999", role="user", created_at=datetime.now(timezone.utc)),
        User(name="James Thomas", email="james.thomas@gmail.com", phone_number="+254 710 101 010", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Kelly Garcia", email="kelly.garcia@gmail.com", phone_number="+254 711 111 111", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Liam Rodriguez", email="liam.rodriguez@gmail.com", phone_number="+254 712 222 222", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Mia Lee", email="mia.lee@gmail.com", phone_number="+254 713 333 333", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Noah Clark", email="noah.clark@gmail.com", phone_number="+254 714 444 444", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Olivia Walker", email="olivia.walker@gmail.com", phone_number="+254 715 555 555", role="user", created_at=datetime.now(timezone.utc)),
        User(name="Lavender Morara", email="lavender.morara@student.moringaschool.com", phone_number="+254 716 666 666", role="admin", created_at=datetime.now(timezone.utc))
    ]
users[0].set_password("Password123!")
users[1].set_password("SecurePass456!")
users[2].set_password("MyPass789!")
users[3].set_password("Dav1d!2023")
users[4].set_password("Emma#9876")
users[5].set_password("Frankie!321")
users[6].set_password("GracePass!654")
users[7].set_password("H3nry!111")
users[8].set_password("Bella!222")
users[9].set_password("Jam3s!333")
users[10].set_password("K3lly!444")
users[11].set_password("L1am!555")
users[12].set_password("M1aPass!666")
users[13].set_password("N0ah!777")
users[14].set_password("Ol1v1a!888")
users[15].set_password("AdminPass!999")

with app.app_context():
    print("Seeding users...")

    try:
        db.session.add_all(users)
        db.session.commit()
        print("Users seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding users:", e)

homes = [
    ChildrenHome(
        name='Upendo Children’s Home',
        location='Westlands, Nairobi',
        phone_number='+254720123456',
        email='upendo.naivasha@example.com',
        description='A nurturing home for children in Nairobi’s Westlands area.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Tumaini Orphanage',
        location='Kilimani, Nairobi',
        phone_number='+254721234567',
        email='tumaini.nakuru@example.com',
        description='Providing hope and education in Kilimani.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Neema Children’s Home',
        location='Kisumu City, Kisumu',
        phone_number='+254722345678',
        email='neema.nairobi@example.com',
        description='Empowering children in Kisumu with care and education.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Amani Shelter',
        location='Eldoret Town, Uasin Gishu',
        phone_number='+254723456789',
        email='amani.naivasha@example.com',
        description='A safe haven for children in Eldoret.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Baraka Home',
        location='Nakuru City, Nakuru',
        phone_number='+254724567890',
        email='baraka.naks@example.com',
        description='Fostering growth and community in Nakuru.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Furaha Orphanage',
        location='Thika Town, Kiambu',
        phone_number='+254725678901',
        email='furaha.thikaroad@example.com',
        description='Bringing joy to children in Thika.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Imani House',
        location='Nyeri Town, Nyeri',
        phone_number='+254726789012',
        email='imani.nyeritown@example.com',
        description='A caring community for children in Nyeri.',
        created_at=datetime.now(timezone.utc)
    ),
    ChildrenHome(
        name='Jua Kali Home',
        location='Kakamega Town, Kakamega',
        phone_number='+254727890123',
        email='juakali.kakamegamills@example.com',
        description='Supporting children’s dreams in Kakamega.',
        created_at=datetime.now(timezone.utc)
    )
]

with app.app_context():
    print("Seeding homes...")

    try:
        db.session.add_all(homes)
        db.session.commit()
        print("Homes seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding homes:", e)



children = [
   
    Child(first_name="James", last_name="Smith", age=10, gender="Male", home_id=1),
    Child(first_name="Emma", last_name="Johnson", age=8, gender="Female", home_id=1),
    Child(first_name="Michael", last_name="Williams", age=12, gender="Male", home_id=1),
    Child(first_name="Olivia", last_name="Brown", age=9, gender="Female", home_id=1),
    Child(first_name="William", last_name="Jones", age=11, gender="Male", home_id=1),
    Child(first_name="Sophia", last_name="Garcia", age=7, gender="Female", home_id=1),
    Child(first_name="Daniel", last_name="Miller", age=13, gender="Male", home_id=1),
    Child(first_name="Ava", last_name="Davis", age=10, gender="Female", home_id=1),
    Child(first_name="Joseph", last_name="Rodriguez", age=12, gender="Male", home_id=1),
    Child(first_name="Isabella", last_name="Martinez", age=8, gender="Female", home_id=1),
    Child(first_name="David", last_name="Hernandez", age=11, gender="Male", home_id=1),
    Child(first_name="Mia", last_name="Lopez", age=9, gender="Female", home_id=1),
    Child(first_name="Thomas", last_name="Gonzalez", age=10, gender="Male", home_id=1),

    Child(first_name="Charles", last_name="Wilson", age=12, gender="Male", home_id=2),
    Child(first_name="Charlotte", last_name="Anderson", age=9, gender="Female", home_id=2),
    Child(first_name="Robert", last_name="Thomas", age=11, gender="Male", home_id=2),
    Child(first_name="Amelia", last_name="Taylor", age=7, gender="Female", home_id=2),
    Child(first_name="John", last_name="Moore", age=10, gender="Male", home_id=2),
    Child(first_name="Harper", last_name="Jackson", age=8, gender="Female", home_id=2),
    Child(first_name="Christopher", last_name="Martin", age=13, gender="Male", home_id=2),
    Child(first_name="Evelyn", last_name="Lee", age=9, gender="Female", home_id=2),
    Child(first_name="Paul", last_name="Perez", age=12, gender="Male", home_id=2),
    Child(first_name="Abigail", last_name="Thompson", age=10, gender="Female", home_id=2),
    Child(first_name="Steven", last_name="White", age=11, gender="Male", home_id=2),
    Child(first_name="Emily", last_name="Harris", age=8, gender="Female", home_id=2),
    Child(first_name="Andrew", last_name="Lewis", age=10, gender="Male", home_id=2),

    Child(first_name="Mark", last_name="Allen", age=11, gender="Male", home_id=3),
    Child(first_name="Sofia", last_name="Young", age=9, gender="Female", home_id=3),
    Child(first_name="George", last_name="King", age=12, gender="Male", home_id=3),
    Child(first_name="Aria", last_name="Wright", age=8, gender="Female", home_id=3),
    Child(first_name="Edward", last_name="Scott", age=10, gender="Male", home_id=3),
    Child(first_name="Grace", last_name="Green", age=7, gender="Female", home_id=3),
    Child(first_name="Richard", last_name="Baker", age=13, gender="Male", home_id=3),
    Child(first_name="Chloe", last_name="Adams", age=9, gender="Female", home_id=3),
    Child(first_name="Samuel", last_name="Nelson", age=11, gender="Male", home_id=3),
    Child(first_name="Zoe", last_name="Carter", age=10, gender="Female", home_id=3),
    Child(first_name="Benjamin", last_name="Mitchell", age=12, gender="Male", home_id=3),
    Child(first_name="Lily", last_name="Perez", age=8, gender="Female", home_id=3),

    Child(first_name="Ali", last_name="Roberts", age=10, gender="Male", home_id=4),
    Child(first_name="Fatima", last_name="Turner", age=9, gender="Female", home_id=4),
    Child(first_name="Hassan", last_name="Phillips", age=12, gender="Male", home_id=4),
    Child(first_name="Aisha", last_name="Campbell", age=8, gender="Female", home_id=4),
    Child(first_name="Mohammed", last_name="Parker", age=11, gender="Male", home_id=4),
    Child(first_name="Luna", last_name="Evans", age=7, gender="Female", home_id=4),
    Child(first_name="Ahmed", last_name="Edwards", age=13, gender="Male", home_id=4),
    Child(first_name="Scarlett", last_name="Collins", age=9, gender="Female", home_id=4),
    Child(first_name="Yusuf", last_name="Stewart", age=10, gender="Male", home_id=4),
    Child(first_name="Mila", last_name="Sanchez", age=8, gender="Female", home_id=4),
    Child(first_name="Ibrahim", last_name="Morris", age=12, gender="Male", home_id=4),
    Child(first_name="Layla", last_name="Rogers", age=10, gender="Female", home_id=4),

    Child(first_name="Henry", last_name="Reed", age=11, gender="Male", home_id=5),
    Child(first_name="Ella", last_name="Cook", age=9, gender="Female", home_id=5),
    Child(first_name="Jack", last_name="Morgan", age=12, gender="Male", home_id=5),
    Child(first_name="Avery", last_name="Bell", age=8, gender="Female", home_id=5),
    Child(first_name="Jacob", last_name="Murphy", age=10, gender="Male", home_id=5),
    Child(first_name="Sadie", last_name="Bailey", age=7, gender="Female", home_id=5),
    Child(first_name="Lucas", last_name="Rivera", age=13, gender="Male", home_id=5),
    Child(first_name="Hannah", last_name="Cooper", age=9, gender="Female", home_id=5),
    Child(first_name="Mason", last_name="Richardson", age=11, gender="Male", home_id=5),
    Child(first_name="Julia", last_name="Cox", age=10, gender="Female", home_id=5),
    Child(first_name="Logan", last_name="Howard", age=12, gender="Male", home_id=5),
    Child(first_name="Addison", last_name="Ward", age=8, gender="Female", home_id=5),
    Child(first_name="Ethan", last_name="Torres", age=10, gender="Male", home_id=5),

    Child(first_name="Liam", last_name="Peterson", age=11, gender="Male", home_id=6),
    Child(first_name="Natalie", last_name="Gray", age=9, gender="Female", home_id=6),
    Child(first_name="Noah", last_name="Ramirez", age=12, gender="Male", home_id=6),
    Child(first_name="Madison", last_name="James", age=8, gender="Female", home_id=6),
    Child(first_name="Elijah", last_name="Watson", age=10, gender="Male", home_id=6),
    Child(first_name="Aubrey", last_name="Brooks", age=7, gender="Female", home_id=6),
    Child(first_name="Alexander", last_name="Kelly", age=13, gender="Male", home_id=6),
    Child(first_name="Allison", last_name="Sanders", age=9, gender="Female", home_id=6),
    Child(first_name="Gabriel", last_name="Price", age=11, gender="Male", home_id=6),
    Child(first_name="Victoria", last_name="Bennett", age=10, gender="Female", home_id=6),
    Child(first_name="Michael", last_name="Wood", age=12, gender="Male", home_id=6),
    Child(first_name="Brooklyn", last_name="Barnes", age=8, gender="Female", home_id=6),

    Child(first_name="Aiden", last_name="Ross", age=10, gender="Male", home_id=7),
    Child(first_name="Elizabeth", last_name="Henderson", age=9, gender="Female", home_id=7),
    Child(first_name="Jackson", last_name="Coleman", age=12, gender="Male", home_id=7),
    Child(first_name="Samantha", last_name="Jenkins", age=8, gender="Female", home_id=7),
    Child(first_name="Sebastian", last_name="Perry", age=11, gender="Male", home_id=7),
    Child(first_name="Camila", last_name="Powell", age=7, gender="Female", home_id=7),
    Child(first_name="Carter", last_name="Long", age=13, gender="Male", home_id=7),
    Child(first_name="Penelope", last_name="Patterson", age=9, gender="Female", home_id=7),
    Child(first_name="Owen", last_name="Hughes", age=10, gender="Male", home_id=7),
    Child(first_name="Riley", last_name="Flores", age=8, gender="Female", home_id=7),
    Child(first_name="Wyatt", last_name="Washington", age=12, gender="Male", home_id=7),
    Child(first_name="Nora", last_name="Butler", age=10, gender="Female", home_id=7),
    Child(first_name="Grayson", last_name="Simmons", age=11, gender="Male", home_id=7),

    Child(first_name="Levi", last_name="Foster", age=10, gender="Male", home_id=8),
    Child(first_name="Hazel", last_name="Gonzales", age=9, gender="Female", home_id=8),
    Child(first_name="Julian", last_name="Bryant", age=12, gender="Male", home_id=8),
    Child(first_name="Violet", last_name="Alexander", age=8, gender="Female", home_id=8),
    Child(first_name="Luke", last_name="Russell", age=11, gender="Male", home_id=8),
    Child(first_name="Stella", last_name="Griffin", age=7, gender="Female", home_id=8),
    Child(first_name="Isaac", last_name="Diaz", age=13, gender="Male", home_id=8),
    Child(first_name="Claire", last_name="Hayes", age=9, gender="Female", home_id=8),
    Child(first_name="Caleb", last_name="Myers", age=10, gender="Male", home_id=8),
    Child(first_name="Ellie", last_name="Ford", age=8, gender="Female", home_id=8),
    Child(first_name="Hunter", last_name="Hamilton", age=12, gender="Male", home_id=8),
    Child(first_name="Lillian", last_name="Graham", age=10, gender="Female", home_id=8)
]

with app.app_context():
    print("Seeding children...")

    try:
        db.session.add_all(children)
        db.session.commit()
        print("Children seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding children:", e)


photos = [
    Photo(image_url="https://images.unsplash.com/photo-1585459503122-ca4fb244c33c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fHNpbXBsZSUyMGhvdXNlcyUyMHRoYXQlMjBjYW4lMjBob2xkJTIwMTclMjBwZW9wbGV8ZW58MHx8MHx8fDA%3D", children_home_id=1),
    Photo(image_url="https://images.unsplash.com/photo-1694286068274-1058e6b04dcc?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTE5fHxraWRzJTIwZ2F0aGVyaW5nfGVufDB8fDB8fHww", children_home_id=1),
    Photo(image_url="https://plus.unsplash.com/premium_photo-1685118419397-c8ed456734ec?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTN8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=1),
    Photo(image_url="https://images.unsplash.com/photo-1635193503553-0678ca1d8582?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODh8fHNjaG9vbCUyMGJlZCUyMGFyZWFzfGVufDB8fDB8fHww", children_home_id=1),

    Photo(image_url="https://plus.unsplash.com/premium_photo-1722593856418-05d6d47eec59?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzd8fHNpbXBsZSUyMGhvdXNlcyUyMHRoYXQlMjBjYW4lMjBob2xkJTIwMTclMjBwZW9wbGV8ZW58MHx8MHx8fDA%3D", children_home_id=2),
    Photo(image_url="https://images.unsplash.com/photo-1611183110451-7e156d15581d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTkyfHxraWRzJTIwZ2F0aGVyaW5nLi4ucHJlZmVycmFibHklMjBvZiUyMGFsbCUyMHJhY2VzfGVufDB8fDB8fHww", children_home_id=2),
    Photo(image_url="https://images.unsplash.com/photo-1655936072812-a55302b986e0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=2),
    Photo(image_url="https://plus.unsplash.com/premium_photo-1677567996070-68fa4181775a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bGlicmFyeXxlbnwwfHwwfHx8MA%3D%3D", children_home_id=2),

    Photo(image_url="https://images.unsplash.com/photo-1569017437456-a82e38aea5ed?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fHNpbXBsZSUyMGhvdXNlcyUyMHRoYXQlMjBjYW4lMjBob2xkJTIwMTclMjBwZW9wbGV8ZW58MHx8MHx8fDA%3D", children_home_id=3),
    Photo(image_url="https://images.unsplash.com/photo-1695131494906-91f5433f1804?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTcwfHxraWRzJTIwZ2F0aGVyaW5nLi4ucHJlZmVycmFibHklMjBvZiUyMGFsbCUyMHJhY2VzfGVufDB8fDB8fHww", children_home_id=3),
    Photo(image_url="https://images.unsplash.com/photo-1552817446-9943ef873b77?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=3),
    Photo(image_url="https://images.unsplash.com/photo-1549856625-824ce09aefc8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fHNjaG9vbCUyMGJlZCUyMGFyZWFzfGVufDB8fDB8fHww", children_home_id=3),

    Photo(image_url="https://images.unsplash.com/photo-1655708553278-f449851bb703?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODZ8fHNpbXBsZSUyMGhvdXNlcyUyMHRoYXQlMjBjYW4lMjBob2xkJTIwMTclMjBwZW9wbGV8ZW58MHx8MHx8fDA%3D", children_home_id=4),
    Photo(image_url="https://images.unsplash.com/photo-1603998382124-c9835bf50409?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDJ8fGtpZHMlMjBnYXRoZXJpbmcuLi5wcmVmZXJyYWJseSUyMG9mJTIwYWxsJTIwcmFjZXN8ZW58MHx8MHx8fDA%3D", children_home_id=4),
    Photo(image_url="https://images.unsplash.com/photo-1540827563097-a6b8abab0a71?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c21hbGwlMjBzcG9ydHMlMjBncm91bmRzfGVufDB8fDB8fHww", children_home_id=4),
    Photo(image_url="https://images.unsplash.com/photo-1724093834407-da3e0fcb7c9d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fHNjaG9vbCUyMGJlZCUyMGFyZWFzfGVufDB8fDB8fHww", children_home_id=4),

    Photo(image_url="https://images.unsplash.com/photo-1574259392081-dbe3c19cd15e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTEyfHxzaW1wbGUlMjBob3VzZXMlMjB0aGF0JTIwY2FuJTIwaG9sZCUyMDE3JTIwcGVvcGxlfGVufDB8fDB8fHww", children_home_id=5),
    Photo(image_url="https://images.unsplash.com/photo-1567727834061-354b65cf0633?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzR8fGtpZHMlMjBnYXRoZXJpbmcuLi5wcmVmZXJyYWJseSUyMG9mJTIwYWxsJTIwcmFjZXN8ZW58MHx8MHx8fDA%3D", children_home_id=5),
    Photo(image_url="https://images.unsplash.com/photo-1721886537583-ea3a257adb9e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHNwb3J0JTIwZmFjaWxpdGllc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=5),
    Photo(image_url="https://plus.unsplash.com/premium_photo-1703701579680-3b4c2761aa47?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjF8fGxpYnJhcnl8ZW58MHx8MHx8fDA%3D", children_home_id=5),

    Photo(image_url="https://images.unsplash.com/photo-1579031711062-85b3f2d92e8b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTMzfHxzaW1wbGUlMjBob3VzZXMlMjB0aGF0JTIwY2FuJTIwaG9sZCUyMDE3JTIwcGVvcGxlfGVufDB8fDB8fHww", children_home_id=6),
    Photo(image_url="https://images.unsplash.com/photo-1509099836639-18ba1795216d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGtpZHMlMjBnYXRoZXJpbmcuLi5wcmVmZXJyYWJseSUyMG9mJTIwYWxsJTIwcmFjZXN8ZW58MHx8MHx8fDA%3D", children_home_id=6),
    Photo(image_url="https://plus.unsplash.com/premium_photo-1665673313512-9ea6c83b8c84?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nzd8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=6),
    Photo(image_url="https://plus.unsplash.com/premium_photo-1661854079306-0ac675d4b259?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8c3BvcnQlMjBmYWNpbGl0aWVzfGVufDB8fDB8fHww", children_home_id=6),

    Photo(image_url="https://images.unsplash.com/photo-1652274409871-96ca9c036f80?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjY5fHxzaW1wbGUlMjBob3VzZXMlMjB0aGF0JTIwY2FuJTIwaG9sZCUyMDE3JTIwcGVvcGxlfGVufDB8fDB8fHww", children_home_id=7),
    Photo(image_url="https://images.unsplash.com/photo-1548102268-3d7dc56b01e1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGtpZHMlMjBnYXRoZXJpbmcuLi5wcmVmZXJyYWJseSUyMG9mJTIwYWxsJTIwcmFjZXN8ZW58MHx8MHx8fDA%3D", children_home_id=7),
    Photo(image_url="https://images.unsplash.com/photo-1568478624365-1134fbd7c895?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=7),
    Photo(image_url="https://images.unsplash.com/photo-1680798790034-63f18ce5f9bd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzZ8fGRpbmluZyUyMGFyZWFzJTIwaW4lMjBzY2hvbHN8ZW58MHx8MHx8fDA%3D", children_home_id=7),

    Photo(image_url="https://images.unsplash.com/photo-1567683740738-d1fbf876b70a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTg1fHxzaW1wbGUlMjBob3VzZXMlMjB0aGF0JTIwY2FuJTIwaG9sZCUyMDE3JTIwcGVvcGxlfGVufDB8fDB8fHww", children_home_id=8),
    Photo(image_url="https://images.unsplash.com/photo-1642420290986-c7a55bab708f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8a2lkcyUyMGdhdGhlcmluZy4uLnByZWZlcnJhYmx5JTIwb2YlMjBhbGwlMjByYWNlc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=8),
    Photo(image_url="https://images.unsplash.com/photo-1548221605-b119eef82aa6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTZ8fHNtYWxsJTIwc3BvcnRzJTIwZ3JvdW5kc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=8),
    Photo(image_url="https://images.unsplash.com/photo-1493666835815-de6b83927e24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8ZGluaW5nJTIwYXJlYXMlMjBpbiUyMHNjaG9sc3xlbnwwfHwwfHx8MA%3D%3D", children_home_id=8)
]

with app.app_context():
    print("Seeding photos...")

    try:
        db.session.add_all(photos)
        db.session.commit()
        print("Photos seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding photos:", e)
        

donations = [
    Donation(amount=15000.0, donation_type="monthly", user_id=3, home_id=1, created_at=datetime.now(timezone.utc)),
    Donation(amount=5000.0, donation_type="just this time", user_id=12, home_id=1, created_at=datetime.now(timezone.utc)),

    Donation(amount=25000.0, donation_type="weekly", user_id=7, home_id=2, created_at=datetime.now(timezone.utc)),
    Donation(amount=10000.0, donation_type="monthly", user_id=15, home_id=2, created_at=datetime.now(timezone.utc)),

    Donation(amount=30000.0, donation_type="just this time", user_id=1, home_id=3, created_at=datetime.now(timezone.utc)),
    Donation(amount=8000.0, donation_type="weekly", user_id=9, home_id=3, created_at=datetime.now(timezone.utc)),

    Donation(amount=20000.0, donation_type="monthly", user_id=5, home_id=4, created_at=datetime.now(timezone.utc)),
    Donation(amount=12000.0, donation_type="just this time", user_id=14, home_id=4, created_at=datetime.now(timezone.utc)),

    Donation(amount=35000.0, donation_type="weekly", user_id=2, home_id=5, created_at=datetime.now(timezone.utc)),
    Donation(amount=6000.0, donation_type="monthly", user_id=11, home_id=5, created_at=datetime.now(timezone.utc)),

    Donation(amount=18000.0, donation_type="just this time", user_id=8, home_id=6, created_at=datetime.now(timezone.utc)),
    Donation(amount=9000.0, donation_type="weekly", user_id=16, home_id=6, created_at=datetime.now(timezone.utc)),

    Donation(amount=40000.0, donation_type="monthly", user_id=4, home_id=7, created_at=datetime.now(timezone.utc)),
    Donation(amount=11000.0, donation_type="just this time", user_id=13, home_id=7, created_at=datetime.now(timezone.utc)),
    Donation(amount=22000.0, donation_type="weekly", user_id=6, home_id=7, created_at=datetime.now(timezone.utc)),

    Donation(amount=28000.0, donation_type="monthly", user_id=10, home_id=8, created_at=datetime.now(timezone.utc)),
    Donation(amount=7000.0, donation_type="weekly", user_id=3, home_id=8, created_at=datetime.now(timezone.utc)),
    Donation(amount=45000.0, donation_type="just this time", user_id=12, home_id=8, created_at=datetime.now(timezone.utc))
]

with app.app_context():
    print("Seeding donations...")

    try:
        db.session.add_all(donations)
        db.session.commit()
        print("Donations seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding donations:", e)


reviews = [
    Review(rating=5, comment="Wonderful staff and clean facilities!", user_id=3, home_id=1, created_at=datetime.now(timezone.utc)),
    Review(rating=4, comment="Great environment for children to thrive.", user_id=12, home_id=1, created_at=datetime.now(timezone.utc)),

    Review(rating=3, comment="Needs more funding but very caring.", user_id=7, home_id=2, created_at=datetime.now(timezone.utc)),
    Review(rating=5, comment="Supportive and welcoming community.", user_id=15, home_id=2, created_at=datetime.now(timezone.utc)),

    Review(rating=4, comment="Well-maintained and organized home.", user_id=1, home_id=3, created_at=datetime.now(timezone.utc)),
    Review(rating=5, comment="Amazing dedication to the children!", user_id=9, home_id=3, created_at=datetime.now(timezone.utc)),

    Review(rating=3, comment="Could use more educational resources.", user_id=5, home_id=4, created_at=datetime.now(timezone.utc)),
    Review(rating=5, comment="Friendly caregivers, highly recommend.", user_id=14, home_id=4, created_at=datetime.now(timezone.utc)),

    Review(rating=4, comment="A true home for the kids.", user_id=2, home_id=5, created_at=datetime.now(timezone.utc)),
    Review(rating=5, comment="Inspiring work, keep it up!", user_id=11, home_id=5, created_at=datetime.now(timezone.utc)),

    Review(rating=5, comment="Safe and nurturing environment.", user_id=8, home_id=6, created_at=datetime.now(timezone.utc)),
    Review(rating=4, comment="Heartwarming to see the care provided.", user_id=16, home_id=6, created_at=datetime.now(timezone.utc)),

    Review(rating=3, comment="Good facilities but needs more activities.", user_id=4, home_id=7, created_at=datetime.now(timezone.utc)),

    Review(rating=5, comment="Dedicated staff, wonderful place.", user_id=10, home_id=8, created_at=datetime.now(timezone.utc))
]

with app.app_context():
    print("Seeding reviews...")

    try:
        db.session.add_all(reviews)
        db.session.commit()
        print("Reviews seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding reviews:", e)
   
        
visits = [

    Visit(
        full_name="Alice Johnson",
        phone_number="+254 701 111 111",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=5)).date(),
        number_of_visitors=12,
        user_id=1,
        home_id=1,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="Bob Smith",
        phone_number="+254 702 222 222",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=10)).date(),
        number_of_visitors=8,
        user_id=2,
        home_id=2,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="Carol White",
        phone_number="+254 703 333 333",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=15)).date(),
        number_of_visitors=15,
        user_id=3,
        home_id=3,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="David Brown",
        phone_number="+254 704 444 444",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=20)).date(),
        number_of_visitors=6,
        user_id=4,
        home_id=4,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="Emma Davis",
        phone_number="+254 705 555 555",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=25)).date(),
        number_of_visitors=18,
        user_id=5,
        home_id=5,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="Frank Wilson",
        phone_number="+254 706 666 666",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=8)).date(),
        number_of_visitors=10,
        user_id=6,
        home_id=6,
        created_at=datetime.now(timezone.utc)
    ),
    Visit(
        full_name="Grace Taylor",
        phone_number="+254 707 777 777",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=12)).date(),
        number_of_visitors=14,
        user_id=7,
        home_id=6,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="Henry Martinez",
        phone_number="+254 708 888 888",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=18)).date(),
        number_of_visitors=17,
        user_id=8,
        home_id=7,
        created_at=datetime.now(timezone.utc)
    ),
    Visit(
        full_name="Isabella Anderson",
        phone_number="+254 709 999 999",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=22)).date(),
        number_of_visitors=9,
        user_id=9,
        home_id=7,
        created_at=datetime.now(timezone.utc)
    ),

    Visit(
        full_name="James Thomas",
        phone_number="+254 710 101 010",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=7)).date(),
        number_of_visitors=13,
        user_id=10,
        home_id=8,
        created_at=datetime.now(timezone.utc)
    ),
    Visit(
        full_name="Kelly Garcia",
        phone_number="+254 711 111 111",
        day_to_visit=(datetime.now(timezone.utc) + timedelta(days=28)).date(),
        number_of_visitors=21,
        user_id=11,
        home_id=8,
        created_at=datetime.now(timezone.utc)
    )
]


with app.app_context():
    print("Seeding visits...")

    try:
        db.session.add_all(visits)
        db.session.commit()
        print("Visits seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding visits:", e)


volunteers = [

    Volunteer(
        name="Alice Johnson",
        phone_number="+254 701 111 111",
        email="alice.johnson@gmail.com",
        description="Teaching assistant for literacy programs.",
        user_id=1,
        home_id=1,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Bob Smith",
        phone_number="+254 702 222 222",
        email="bob.smith@gmail.com",
        description="Mentor for extracurricular activities.",
        user_id=2,
        home_id=1,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Carol White",
        phone_number="+254 703 333 333",
        email="carol.white@gmail.com",
        description="Organizer for community outreach events.",
        user_id=3,
        home_id=2,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="David Brown",
        phone_number="+254 704 444 444",
        email="david.brown@gmail.com",
        description="Support staff for daily operations.",
        user_id=4,
        home_id=2,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Emma Davis",
        phone_number="+254 705 555 555",
        email="emma.davis@gmail.com",
        description="Tutor for math and science classes.",
        user_id=5,
        home_id=3,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Frank Wilson",
        phone_number="+254 706 666 666",
        email="frank.wilson@gmail.com",
        description="Coordinator for health and wellness programs.",
        user_id=6,
        home_id=3,
        created_at=datetime.now(timezone.utc)
    ),

 
    Volunteer(
        name="Grace Taylor",
        phone_number="+254 707 777 777",
        email="grace.taylor@gmail.com",
        description="Assistant for recreational activities.",
        user_id=7,
        home_id=4,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Henry Martinez",
        phone_number="+254 708 888 888",
        email="henry.martinez@gmail.com",
        description="Volunteer for facility maintenance.",
        user_id=8,
        home_id=4,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Isabella Anderson",
        phone_number="+254 709 999 999",
        email="isabella.anderson@gmail.com",
        description="Teaching assistant for literacy programs.",
        user_id=9,
        home_id=5,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="James Thomas",
        phone_number="+254 710 101 010",
        email="james.thomas@gmail.com",
        description="Mentor for extracurricular activities.",
        user_id=10,
        home_id=5,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Kelly Garcia",
        phone_number="+254 711 111 111",
        email="kelly.garcia@gmail.com",
        description="Organizer for community outreach events.",
        user_id=11,
        home_id=6,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Liam Rodriguez",
        phone_number="+254 712 222 222",
        email="liam.rodriguez@gmail.com",
        description="Support staff for daily operations.",
        user_id=12,
        home_id=6,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Alice Johnson",
        phone_number="+254 701 111 111",
        email="alice.johnson@gmail.com",
        description="Tutor for math and science classes.",
        user_id=1,
        home_id=6,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Mia Lee",
        phone_number="+254 713 333 333",
        email="mia.lee@gmail.com",
        description="Coordinator for health and wellness programs.",
        user_id=13,
        home_id=7,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Noah Clark",
        phone_number="+254 714 444 444",
        email="noah.clark@gmail.com",
        description="Assistant for recreational activities.",
        user_id=14,
        home_id=7,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Bob Smith",
        phone_number="+254 702 222 222",
        email="bob.smith@gmail.com",
        description="Volunteer for facility maintenance.",
        user_id=2,
        home_id=7,
        created_at=datetime.now(timezone.utc)
    ),

    Volunteer(
        name="Olivia Walker",
        phone_number="+254 715 555 555",
        email="olivia.walker@gmail.com",
        description="Teaching assistant for literacy programs.",
        user_id=15,
        home_id=8,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Lavender Morara",
        phone_number="+254 716 666 666",
        email="lavender.morara@student.moringaschool.com",
        description="Mentor for extracurricular activities.",
        user_id=16,
        home_id=8,
        created_at=datetime.now(timezone.utc)
    ),
    Volunteer(
        name="Carol White",
        phone_number="+254 703 333 333",
        email="carol.white@gmail.com",
        description="Organizer for community outreach events.",
        user_id=3,
        home_id=8,
        created_at=datetime.now(timezone.utc)
    )
]

with app.app_context():
    print("Seeding volunteers...")

    try:
        db.session.add_all(volunteers)
        db.session.commit()
        print("Volunteers seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print("An error occurred while seeding volunteers:", e)

print("Database successfully seeded!!!!")

if __name__ == '__main__':
    seed_database()