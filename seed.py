from datetime import datetime, timezone, timedelta
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
        # Clear existing data in reverse dependency order
        try:
            db.session.query(Volunteer).delete()
            db.session.query(Visit).delete()
            db.session.query(Review).delete()
            db.session.query(Donation).delete()
            db.session.query(Photo).delete()
            db.session.query(Child).delete()
            db.session.query(ChildrenHome).delete()
            db.session.query(User).delete()
            db.session.commit()
            print("Database cleared successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error clearing database: {e}")
            return

    # Seed Users
    users = [
        User(id=1, name="Alice Johnson", email="alice.johnson@gmail.com", phone_number="+254 701 111 111", role="user", created_at=datetime.now(timezone.utc)),
        User(id=2, name="Bob Smith", email="bob.smith@gmail.com", phone_number="+254 702 222 222", role="user", created_at=datetime.now(timezone.utc)),
        User(id=3, name="Carol White", email="carol.white@gmail.com", phone_number="+254 703 333 333", role="user", created_at=datetime.now(timezone.utc)),
        User(id=4, name="David Brown", email="david.brown@gmail.com", phone_number="+254 704 444 444", role="user", created_at=datetime.now(timezone.utc)),
        User(id=5, name="Emma Davis", email="emma.davis@gmail.com", phone_number="+254 705 555 555", role="user", created_at=datetime.now(timezone.utc)),
        User(id=6, name="Frank Wilson", email="frank.wilson@gmail.com", phone_number="+254 706 666 666", role="user", created_at=datetime.now(timezone.utc)),
        User(id=7, name="Grace Taylor", email="grace.taylor@gmail.com", phone_number="+254 707 777 777", role="user", created_at=datetime.now(timezone.utc)),
        User(id=8, name="Henry Martinez", email="henry.martinez@gmail.com", phone_number="+254 708 888 888", role="user", created_at=datetime.now(timezone.utc)),
        User(id=9, name="Isabella Anderson", email="isabella.anderson@gmail.com", phone_number="+254 709 999 999", role="user", created_at=datetime.now(timezone.utc)),
        User(id=10, name="James Thomas", email="james.thomas@gmail.com", phone_number="+254 710 101 010", role="user", created_at=datetime.now(timezone.utc)),
        User(id=11, name="Kelly Garcia", email="kelly.garcia@gmail.com", phone_number="+254 711 111 111", role="user", created_at=datetime.now(timezone.utc)),
        User(id=12, name="Liam Rodriguez", email="liam.rodriguez@gmail.com", phone_number="+254 712 222 222", role="user", created_at=datetime.now(timezone.utc)),
        User(id=13, name="Mia Lee", email="mia.lee@gmail.com", phone_number="+254 713 333 333", role="user", created_at=datetime.now(timezone.utc)),
        User(id=14, name="Noah Clark", email="noah.clark@gmail.com", phone_number="+254 714 444 444", role="user", created_at=datetime.now(timezone.utc)),
        User(id=15, name="Olivia Walker", email="olivia.walker@gmail.com", phone_number="+254 715 555 555", role="user", created_at=datetime.now(timezone.utc)),
        User(id=16, name="Lavender Morara", email="lavender.morara@student.moringaschool.com", phone_number="+254 716 666 666", role="admin", created_at=datetime.now(timezone.utc))
    ]

    # Set passwords
    try:
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
    except Exception as e:
        print(f"Error setting passwords: {e}")
        return

    with app.app_context():
        print("Seeding users...")
        try:
            if not isinstance(users, (list, tuple)):
                raise TypeError(f"Users is not iterable, got type: {type(users)}")
            db.session.add_all(users)
            db.session.commit()
            print(f"Seeded {len(users)} users successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding users: {e}")
            return

    # Seed Children Homes
    homes = [
        ChildrenHome(id=1, name='Upendo Children’s Home', location='Westlands, Nairobi', phone_number='+254720123456', email='upendo.naivasha@egmail.com', description='A nurturing home for children in Nairobi’s Westlands area. This home goes far beyond simply meeting the basic needs of food and shelter — it embraces a whole-child philosophy that nurtures emotional well-being, educational growth, and spiritual healing. Each child is welcomed into a warm, family-like environment where caregivers offer not only stability and protection but also genuine love and encouragement. Daily routines include school attendance, structured play, counseling sessions, and community engagement activities, all aimed at restoring a sense of purpose and belonging. The home maintains strong partnerships with local schools, healthcare providers, and volunteers, ensuring that every child has access to quality education, healthcare, and positive adult role models. At Bright Horizons, the focus is not on what the children have lost, but on the vast potential they carry within. Every program and effort is designed to help them reclaim their childhood, build self-confidence, and ultimately rise into empowered, compassionate adults who can one day give back to their communities. Through the unwavering commitment of staff and volunteers, Bright Horizons Home is rewriting the stories of countless children — one heart, one smile, one future at a time.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=2, name='Tumaini Orphanage', location='Kilimani, Nairobi', phone_number='+254721234567', email='tumaini.nakuru@gmail.com', description='Providing hope and education in Kilimani.The home provides not only shelter and meals but also holistic care — including education, emotional support, and mentorship. With a dedicated team of social workers and educators, Bright Horizons focuses on healing trauma, encouraging creativity, and helping children rediscover joy and purpose. Through art therapy, life-skills training, and a strong sense of community, each child is guided toward a brighter future filled with possibility.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=3, name='Neema Children’s Home', location='Kisumu City, Kisumu', phone_number='+254722345678', email='neema.nairobi@gmail.com', description='Empowering children in Kisumu with care and education.The home offers a nurturing space where kids are not only cared for physically but also emotionally and academically. Here, education is prioritized, with after-school tutoring, STEM programs, and reading clubs designed to build confidence and ignite young minds. Daily routines include gardening, music, and storytelling sessions, creating a rhythm of love and structure. Volunteers from across Kenya regularly visit to share knowledge, joy, and companionship, reinforcing the home’s motto: “Every child’s light deserves to shine.”', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=4, name='Amani Shelter', location='Eldoret Town, Uasin Gishu', phone_number='+254723456789', email='amani.naivasha@gmail.com', description='A safe haven for children in Eldoret.Safe Haven is a calm, structured, and deeply caring space where children can feel truly safe. Many of the residents are survivors of domestic abuse or displacement, and the home specializes in trauma recovery and psychological support. In addition to academic instruction, children receive regular therapy sessions, health screenings, and opportunities to participate in team sports and farming activities. The home partners closely with local hospitals and mental health specialists, ensuring each child receives the wraparound care needed to reclaim their sense of self and security.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=5, name='Baraka Home', location='Nakuru City, Nakuru', phone_number='+254724567890', email='baraka.naks@gmail.com', description='Fostering growth and community in Nakuru. This home is known for integrating arts, music, and storytelling into its core programming. Many of the children come from street environments or have been rescued from exploitative situations. At Hope Roots, they find not only safety but a platform to express themselves, celebrate their identities, and dream without limits. The homes seaside location offers therapeutic nature walks, beach cleanups, and community festivals, building a strong sense of connection with both nature and society.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=6, name='Furaha Orphanage', location='Thika Town, Kiambu', phone_number='+254725678901', email='furaha.thikaroad@gmail.com', description='Bringing joy to children in Thika.With a focus on education and empowerment, the home serves children from diverse backgrounds, including refugees and those with disabilities. The children here are taught using inclusive learning models, and staff provide individualized education plans to cater to unique learning needs. Vocational training in tailoring, organic farming, and computer literacy prepares older children for self-sufficiency. Unity Haven’s vision is to create leaders who not only overcome adversity but return to uplift the communities they came from.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=7, name='Imani House', location='Nyeri Town, Nyeri', phone_number='+254726789012', email='imani.nyeritown@gmail.com', description='A caring community for children in Nyeri. Daily life includes morning devotionals, classroom lessons, storytelling under the trees, and communal meals. The home emphasizes character formation, encouraging values like empathy, honesty, and discipline. The children here also help tend the home’s vegetable garden and livestock, learning responsibility and sustainability. With the support of dedicated caregivers and international sponsors, Sunrise Shelter is transforming lives, one sunrise at a time.', created_at=datetime.now(timezone.utc)),
        ChildrenHome(id=8, name='Jua Kali Home', location='Kakamega Town, Kakamega', phone_number='+254727890123', email='juakali.kakamegamills@gmail.com', description='Supporting children’s dreams in Kakamega.The home combines high-quality schooling with mentorship, tutoring, and leadership development. Children here are encouraged to pursue excellence while also learning about empathy, teamwork, and civic responsibility. Many alumni have gone on to succeed in universities and youth leadership programs.A team of nurses, caregivers, and volunteers ensures children receive medical attention, developmental screenings, and the emotional connection they need to thrive.', created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding homes...")
        try:
            if not isinstance(homes, (list, tuple)):
                raise TypeError(f"Homes is not iterable, got type: {type(homes)}")
            db.session.add_all(homes)
            db.session.commit()
            print(f"Seeded {len(homes)} homes successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding homes: {e}")
            return

    # Seed Children
    children = [
        Child(id=1, first_name="James", last_name="Smith", age=10, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=2, first_name="Emma", last_name="Johnson", age=8, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=3, first_name="Michael", last_name="Williams", age=12, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=4, first_name="Olivia", last_name="Brown", age=9, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=5, first_name="William", last_name="Jones", age=11, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=6, first_name="Sophia", last_name="Garcia", age=7, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=7, first_name="Daniel", last_name="Miller", age=13, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=8, first_name="Ava", last_name="Davis", age=10, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=9, first_name="Joseph", last_name="Rodriguez", age=12, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=10, first_name="Isabella", last_name="Martinez", age=8, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=11, first_name="David", last_name="Hernandez", age=11, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=12, first_name="Mia", last_name="Lopez", age=9, gender="Female", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=13, first_name="Thomas", last_name="Gonzalez", age=10, gender="Male", home_id=1, created_at=datetime.now(timezone.utc)),
        Child(id=14, first_name="Charles", last_name="Wilson", age=12, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=15, first_name="Charlotte", last_name="Anderson", age=9, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=16, first_name="Robert", last_name="Thomas", age=11, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=17, first_name="Amelia", last_name="Taylor", age=7, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=18, first_name="John", last_name="Moore", age=10, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=19, first_name="Harper", last_name="Jackson", age=8, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=20, first_name="Christopher", last_name="Martin", age=13, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=21, first_name="Evelyn", last_name="Lee", age=9, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=22, first_name="Paul", last_name="Perez", age=12, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=23, first_name="Abigail", last_name="Thompson", age=10, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=24, first_name="Steven", last_name="White", age=11, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=25, first_name="Emily", last_name="Harris", age=8, gender="Female", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=26, first_name="Andrew", last_name="Lewis", age=10, gender="Male", home_id=2, created_at=datetime.now(timezone.utc)),
        Child(id=27, first_name="Mark", last_name="Allen", age=11, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=28, first_name="Sofia", last_name="Young", age=9, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=29, first_name="George", last_name="King", age=12, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=30, first_name="Aria", last_name="Wright", age=8, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=31, first_name="Edward", last_name="Scott", age=10, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=32, first_name="Grace", last_name="Green", age=7, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=33, first_name="Richard", last_name="Baker", age=13, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=34, first_name="Chloe", last_name="Adams", age=9, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=35, first_name="Samuel", last_name="Nelson", age=11, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=36, first_name="Zoe", last_name="Carter", age=10, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=37, first_name="Benjamin", last_name="Mitchell", age=12, gender="Male", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=38, first_name="Lily", last_name="Perez", age=8, gender="Female", home_id=3, created_at=datetime.now(timezone.utc)),
        Child(id=39, first_name="Ali", last_name="Roberts", age=10, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=40, first_name="Fatima", last_name="Turner", age=9, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=41, first_name="Hassan", last_name="Phillips", age=12, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=42, first_name="Aisha", last_name="Campbell", age=8, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=43, first_name="Mohammed", last_name="Parker", age=11, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=44, first_name="Luna", last_name="Evans", age=7, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=45, first_name="Ahmed", last_name="Edwards", age=13, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=46, first_name="Scarlett", last_name="Collins", age=9, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=47, first_name="Yusuf", last_name="Stewart", age=10, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=48, first_name="Mila", last_name="Sanchez", age=8, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=49, first_name="Ibrahim", last_name="Morris", age=12, gender="Male", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=50, first_name="Layla", last_name="Rogers", age=10, gender="Female", home_id=4, created_at=datetime.now(timezone.utc)),
        Child(id=51, first_name="Henry", last_name="Reed", age=11, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=52, first_name="Ella", last_name="Cook", age=9, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=53, first_name="Jack", last_name="Morgan", age=12, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=54, first_name="Avery", last_name="Bell", age=8, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=55, first_name="Jacob", last_name="Murphy", age=10, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=56, first_name="Sadie", last_name="Bailey", age=7, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=57, first_name="Lucas", last_name="Rivera", age=13, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=58, first_name="Hannah", last_name="Cooper", age=9, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=59, first_name="Mason", last_name="Richardson", age=11, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=60, first_name="Julia", last_name="Cox", age=10, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=61, first_name="Logan", last_name="Howard", age=12, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=62, first_name="Addison", last_name="Ward", age=8, gender="Female", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=63, first_name="Ethan", last_name="Torres", age=10, gender="Male", home_id=5, created_at=datetime.now(timezone.utc)),
        Child(id=64, first_name="Liam", last_name="Peterson", age=11, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=65, first_name="Natalie", last_name="Gray", age=9, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=66, first_name="Noah", last_name="Ramirez", age=12, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=67, first_name="Madison", last_name="James", age=8, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=68, first_name="Elijah", last_name="Watson", age=10, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=69, first_name="Aubrey", last_name="Brooks", age=7, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=70, first_name="Alexander", last_name="Kelly", age=13, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=71, first_name="Allison", last_name="Sanders", age=9, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=72, first_name="Gabriel", last_name="Price", age=11, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=73, first_name="Victoria", last_name="Bennett", age=10, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=74, first_name="Michael", last_name="Wood", age=12, gender="Male", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=75, first_name="Brooklyn", last_name="Barnes", age=8, gender="Female", home_id=6, created_at=datetime.now(timezone.utc)),
        Child(id=76, first_name="Aiden", last_name="Ross", age=10, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=77, first_name="Elizabeth", last_name="Henderson", age=9, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=78, first_name="Jackson", last_name="Coleman", age=12, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=79, first_name="Samantha", last_name="Jenkins", age=8, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=80, first_name="Sebastian", last_name="Perry", age=11, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=81, first_name="Camila", last_name="Powell", age=7, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=82, first_name="Carter", last_name="Long", age=13, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=83, first_name="Penelope", last_name="Patterson", age=9, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=84, first_name="Owen", last_name="Hughes", age=10, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=85, first_name="Riley", last_name="Flores", age=8, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=86, first_name="Wyatt", last_name="Washington", age=12, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=87, first_name="Nora", last_name="Butler", age=10, gender="Female", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=88, first_name="Grayson", last_name="Simmons", age=11, gender="Male", home_id=7, created_at=datetime.now(timezone.utc)),
        Child(id=89, first_name="Levi", last_name="Foster", age=10, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=90, first_name="Hazel", last_name="Gonzales", age=9, gender="Female", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=91, first_name="Julian", last_name="Bryant", age=12, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=92, first_name="Violet", last_name="Alexander", age=8, gender="Female", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=93, first_name="Luke", last_name="Russell", age=11, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=94, first_name="Stella", last_name="Griffin", age=7, gender="Female", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=95, first_name="Isaac", last_name="Diaz", age=13, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=96, first_name="Claire", last_name="Hayes", age=9, gender="Female", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=97, first_name="Caleb", last_name="Myers", age=10, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=98, first_name="Ellie", last_name="Ford", age=8, gender="Female", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=99, first_name="Hunter", last_name="Hamilton", age=12, gender="Male", home_id=8, created_at=datetime.now(timezone.utc)),
        Child(id=100, first_name="Lillian", last_name="Graham", age=10, gender="Female", home_id=8, created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding children...")
        try:
            if not isinstance(children, (list, tuple)):
                raise TypeError(f"Children is not iterable, got type: {type(children)}")
            db.session.add_all(children)
            db.session.commit()
            print(f"Seeded {len(children)} children successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding children: {e}")
            return

    # Seed Photos
    photos = [
        Photo(id=1, image_url="https://images.unsplash.com/photo-1527490087278-9c75be0b8052?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2hpbGRyZW58ZW58MHwwfDB8fHww", children_home_id=1),
        Photo(id=2, image_url="https://images.unsplash.com/photo-1540479859555-17af45c78602?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2hpbGRyZW58ZW58MHwwfDB8fHww", children_home_id=1),
        Photo(id=3, image_url="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2hpbGRyZW58ZW58MHwwfDB8fHww", children_home_id=1),
        Photo(id=4, image_url="https://images.unsplash.com/photo-1577896852618-01da1dd79f7e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=1),
        Photo(id=5, image_url="https://images.unsplash.com/photo-1534982841079-afde227ada8f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=2),
        Photo(id=6, image_url="https://plus.unsplash.com/premium_photo-1661281406994-090d20b3d61c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=2),
        Photo(id=7, image_url="https://images.unsplash.com/photo-1533222481259-ce20eda1e20b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=2),
        Photo(id=8, image_url="https://images.unsplash.com/photo-1505155485412-30b3a45080ec?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=2),
        Photo(id=9, image_url="https://images.unsplash.com/photo-1509163245925-f4255dea7727?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTl8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=3),
        Photo(id=10, image_url="https://images.unsplash.com/photo-1524503033411-c9566986fc8f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NjN8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=3),
        Photo(id=11, image_url="https://images.unsplash.com/photo-1623604407437-d8fce3bc61de?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODB8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=3),
        Photo(id=12, image_url="https://images.unsplash.com/photo-1527563427650-2fa0b1558cba?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTJ8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=3),
        Photo(id=13, image_url="https://images.unsplash.com/photo-1533222535026-754c501569dd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTV8fGNoaWxkcmVufGVufDB8MHwwfHx8MA%3D%3D", children_home_id=4),
        Photo(id=14, image_url="https://images.unsplash.com/photo-1635247055943-5609b3850b1b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAzfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=4),
        Photo(id=15, image_url="https://images.unsplash.com/photo-1524069290683-0457abfe42c3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTE1fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=4),
        Photo(id=16, image_url="https://images.unsplash.com/photo-1524069290683-0457abfe42c3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTE1fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=4),
        Photo(id=17, image_url="https://images.unsplash.com/flagged/photo-1567116681178-c326fa4e2c8b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTMxfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=5),
        Photo(id=18, image_url="https://images.unsplash.com/photo-1497486751825-1233686d5d80?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTY4fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=5),
        Photo(id=19, image_url="https://images.unsplash.com/photo-1610500796385-3ffc1ae2f046?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTc2fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=5),
        Photo(id=20, image_url="https://images.unsplash.com/photo-1490424660416-359912d314b3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjA4fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=5),
        Photo(id=21, image_url="https://images.unsplash.com/photo-1490424660416-359912d314b3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjA4fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=6),
        Photo(id=22, image_url="https://plus.unsplash.com/premium_photo-1677666510092-a19a7e8712d0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjM3fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=6),
        Photo(id=23, image_url="https://images.unsplash.com/photo-1518842023089-50e9ac314ad1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjQ0fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=6),
        Photo(id=24, image_url="https://plus.unsplash.com/premium_photo-1661854079306-0ac675d4b259?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8c3BvcnQlMjBmYWNpbGl0aWVzfGVufDB8fDB8fHww", children_home_id=6),
        Photo(id=25, image_url="https://images.unsplash.com/photo-1590223357622-d7ba1d88d3f7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjYzfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=7),
        Photo(id=26, image_url="https://images.unsplash.com/photo-1608746200372-b84291ea2087?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjYwfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=7),
        Photo(id=27, image_url="https://images.unsplash.com/photo-1604155944627-35e00f0e66e5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjk0fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=7),
        Photo(id=28, image_url="https://images.unsplash.com/photo-1542815760-68d0c6ff14b5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzAyfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=7),
        Photo(id=29, image_url="https://images.unsplash.com/photo-1702236254532-38a12197222b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzE5fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=8),
        Photo(id=30, image_url="https://images.unsplash.com/photo-1658288583703-9ee00069d96f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzE4fHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=8),
        Photo(id=31, image_url="https://plus.unsplash.com/premium_photo-1691752880763-f3e56011e88c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzMzfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=8),
        Photo(id=32, image_url="https://images.unsplash.com/photo-1665250316550-0fac81b86ad4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzYwfHxjaGlsZHJlbnxlbnwwfDB8MHx8fDA%3D", children_home_id=8)
    ]

    with app.app_context():
        print("Seeding photos...")
        try:
            if not isinstance(photos, (list, tuple)):
                raise TypeError(f"Photos is not iterable, got type: {type(photos)}")
            db.session.add_all(photos)
            db.session.commit()
            print(f"Seeded {len(photos)} photos successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding photos: {e}")
            return

    # Seed Donations
    donations = [
        Donation(id=1, amount=15000.0, donation_type="monthly", user_id=3, home_id=1, created_at=datetime.now(timezone.utc)),
        Donation(id=2, amount=5000.0, donation_type="just this time", user_id=12, home_id=1, created_at=datetime.now(timezone.utc)),
        Donation(id=3, amount=25000.0, donation_type="weekly", user_id=7, home_id=2, created_at=datetime.now(timezone.utc)),
        Donation(id=4, amount=10000.0, donation_type="monthly", user_id=15, home_id=2, created_at=datetime.now(timezone.utc)),
        Donation(id=5, amount=30000.0, donation_type="just this time", user_id=1, home_id=3, created_at=datetime.now(timezone.utc)),
        Donation(id=6, amount=8000.0, donation_type="weekly", user_id=9, home_id=3, created_at=datetime.now(timezone.utc)),
        Donation(id=7, amount=20000.0, donation_type="monthly", user_id=5, home_id=4, created_at=datetime.now(timezone.utc)),
        Donation(id=8, amount=12000.0, donation_type="just this time", user_id=14, home_id=4, created_at=datetime.now(timezone.utc)),
        Donation(id=9, amount=35000.0, donation_type="weekly", user_id=2, home_id=5, created_at=datetime.now(timezone.utc)),
        Donation(id=10, amount=6000.0, donation_type="monthly", user_id=11, home_id=5, created_at=datetime.now(timezone.utc)),
        Donation(id=11, amount=18000.0, donation_type="just this time", user_id=8, home_id=6, created_at=datetime.now(timezone.utc)),
        Donation(id=12, amount=9000.0, donation_type="weekly", user_id=16, home_id=6, created_at=datetime.now(timezone.utc)),
        Donation(id=13, amount=40000.0, donation_type="monthly", user_id=4, home_id=7, created_at=datetime.now(timezone.utc)),
        Donation(id=14, amount=11000.0, donation_type="just this time", user_id=13, home_id=7, created_at=datetime.now(timezone.utc)),
        Donation(id=15, amount=22000.0, donation_type="weekly", user_id=6, home_id=7, created_at=datetime.now(timezone.utc)),
        Donation(id=16, amount=28000.0, donation_type="monthly", user_id=10, home_id=8, created_at=datetime.now(timezone.utc)),
        Donation(id=17, amount=7000.0, donation_type="weekly", user_id=3, home_id=8, created_at=datetime.now(timezone.utc)),
        Donation(id=18, amount=45000.0, donation_type="just this time", user_id=12, home_id=8, created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding donations...")
        try:
            if not isinstance(donations, (list, tuple)):
                raise TypeError(f"Donations is not iterable, got type: {type(donations)}")
            db.session.add_all(donations)
            db.session.commit()
            print(f"Seeded {len(donations)} donations successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding donations: {e}")
            return

    # Seed Reviews
    reviews = [
        Review(id=1, rating=5, comment="Wonderful staff and clean facilities!", user_id=3, home_id=1, created_at=datetime.now(timezone.utc)),
        Review(id=2, rating=4, comment="Great environment for children to thrive.", user_id=12, home_id=1, created_at=datetime.now(timezone.utc)),
        Review(id=3, rating=3, comment="Needs more funding but very caring.", user_id=7, home_id=2, created_at=datetime.now(timezone.utc)),
        Review(id=4, rating=5, comment="Supportive and welcoming community.", user_id=15, home_id=2, created_at=datetime.now(timezone.utc)),
        Review(id=5, rating=4, comment="Well-maintained and organized home.", user_id=1, home_id=3, created_at=datetime.now(timezone.utc)),
        Review(id=6, rating=5, comment="Amazing dedication to the children!", user_id=9, home_id=3, created_at=datetime.now(timezone.utc)),
        Review(id=7, rating=3, comment="Could use more educational resources.", user_id=5, home_id=4, created_at=datetime.now(timezone.utc)),
        Review(id=8, rating=5, comment="Friendly caregivers, highly recommend.", user_id=14, home_id=4, created_at=datetime.now(timezone.utc)),
        Review(id=9, rating=4, comment="A true home for the kids.", user_id=2, home_id=5, created_at=datetime.now(timezone.utc)),
        Review(id=10, rating=5, comment="Inspiring work, keep it up!", user_id=11, home_id=5, created_at=datetime.now(timezone.utc)),
        Review(id=11, rating=5, comment="Safe and nurturing environment.", user_id=8, home_id=6, created_at=datetime.now(timezone.utc)),
        Review(id=12, rating=4, comment="Heartwarming to see the care provided.", user_id=16, home_id=6, created_at=datetime.now(timezone.utc)),
        Review(id=13, rating=3, comment="Good facilities but needs more activities.", user_id=4, home_id=7, created_at=datetime.now(timezone.utc)),
        Review(id=14, rating=5, comment="Dedicated staff, wonderful place.", user_id=10, home_id=8, created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding reviews...")
        try:
            if not isinstance(reviews, (list, tuple)):
                raise TypeError(f"Reviews is not iterable, got type: {type(reviews)}")
            db.session.add_all(reviews)
            db.session.commit()
            print(f"Seeded {len(reviews)} reviews successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding reviews: {e}")
            return

    # Seed Visits
    visits = [
        Visit(id=1, full_name="Alice Johnson", phone_number="+254 701 111 111", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=5)).date(), number_of_visitors=12, user_id=1, home_id=1, created_at=datetime.now(timezone.utc)),
        Visit(id=2, full_name="Bob Smith", phone_number="+254 702 222 222", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=10)).date(), number_of_visitors=8, user_id=2, home_id=2, created_at=datetime.now(timezone.utc)),
        Visit(id=3, full_name="Carol White", phone_number="+254 703 333 333", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=15)).date(), number_of_visitors=15, user_id=3, home_id=3, created_at=datetime.now(timezone.utc)),
        Visit(id=4, full_name="David Brown", phone_number="+254 704 444 444", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=20)).date(), number_of_visitors=6, user_id=4, home_id=4, created_at=datetime.now(timezone.utc)),
        Visit(id=5, full_name="Emma Davis", phone_number="+254 705 555 555", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=25)).date(), number_of_visitors=18, user_id=5, home_id=5, created_at=datetime.now(timezone.utc)),
        Visit(id=6, full_name="Frank Wilson", phone_number="+254 706 666 666", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=8)).date(), number_of_visitors=10, user_id=6, home_id=6, created_at=datetime.now(timezone.utc)),
        Visit(id=7, full_name="Grace Taylor", phone_number="+254 707 777 777", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=12)).date(), number_of_visitors=14, user_id=7, home_id=6, created_at=datetime.now(timezone.utc)),
        Visit(id=8, full_name="Henry Martinez", phone_number="+254 708 888 888", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=18)).date(), number_of_visitors=17, user_id=8, home_id=7, created_at=datetime.now(timezone.utc)),
        Visit(id=9, full_name="Isabella Anderson", phone_number="+254 709 999 999", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=22)).date(), number_of_visitors=9, user_id=9, home_id=7, created_at=datetime.now(timezone.utc)),
        Visit(id=10, full_name="James Thomas", phone_number="+254 710 101 010", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=7)).date(), number_of_visitors=13, user_id=10, home_id=8, created_at=datetime.now(timezone.utc)),
        Visit(id=11, full_name="Kelly Garcia", phone_number="+254 711 111 111", day_to_visit=(datetime.now(timezone.utc) + timedelta(days=28)).date(), number_of_visitors=21, user_id=11, home_id=8, created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding visits...")
        try:
            if not isinstance(visits, (list, tuple)):
                raise TypeError(f"Visits is not iterable, got type: {type(visits)}")
            db.session.add_all(visits)
            db.session.commit()
            print(f"Seeded {len(visits)} visits successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding visits: {e}")
            return

    # Seed Volunteers
    volunteers = [
        Volunteer(id=1, name="Alice Johnson", phone_number="+254 701 111 111", email="alice.johnson@gmail.com", description="Teaching assistant for literacy programs.", user_id=1, home_id=1, created_at=datetime.now(timezone.utc)),
        Volunteer(id=2, name="Bob Smith", phone_number="+254 702 222 222", email="bob.smith@gmail.com", description="Mentor for extracurricular activities.", user_id=2, home_id=1, created_at=datetime.now(timezone.utc)),
        Volunteer(id=3, name="Carol White", phone_number="+254 703 333 333", email="carol.white@gmail.com", description="Organizer for community outreach events.", user_id=3, home_id=2, created_at=datetime.now(timezone.utc)),
        Volunteer(id=4, name="David Brown", phone_number="+254 704 444 444", email="david.brown@gmail.com", description="Support staff for daily operations.", user_id=4, home_id=2, created_at=datetime.now(timezone.utc)),
        Volunteer(id=5, name="Emma Davis", phone_number="+254 705 555 555", email="emma.davis@gmail.com", description="Tutor for math and science classes.", user_id=5, home_id=3, created_at=datetime.now(timezone.utc)),
        Volunteer(id=6, name="Frank Wilson", phone_number="+254 706 666 666", email="frank.wilson@gmail.com", description="Coordinator for health and wellness programs.", user_id=6, home_id=3, created_at=datetime.now(timezone.utc)),
        Volunteer(id=7, name="Grace Taylor", phone_number="+254 707 777 777", email="grace.taylor@gmail.com", description="Assistant for recreational activities.", user_id=7, home_id=4, created_at=datetime.now(timezone.utc)),
        Volunteer(id=8, name="Henry Martinez", phone_number="+254 708 888 888", email="henry.martinez@gmail.com", description="Volunteer for facility maintenance.", user_id=8, home_id=4, created_at=datetime.now(timezone.utc)),
        Volunteer(id=9, name="Isabella Anderson", phone_number="+254 709 999 999", email="isabella.anderson@gmail.com", description="Teaching assistant for literacy programs.", user_id=9, home_id=5, created_at=datetime.now(timezone.utc)),
        Volunteer(id=10, name="James Thomas", phone_number="+254 710 101 010", email="james.thomas@gmail.com", description="Mentor for extracurricular activities.", user_id=10, home_id=5, created_at=datetime.now(timezone.utc)),
        Volunteer(id=11, name="Kelly Garcia", phone_number="+254 711 111 111", email="kelly.garcia@gmail.com", description="Organizer for community outreach events.", user_id=11, home_id=6, created_at=datetime.now(timezone.utc)),
        Volunteer(id=12, name="Liam Rodriguez", phone_number="+254 712 222 222", email="liam.rodriguez@gmail.com", description="Support staff for daily operations.", user_id=12, home_id=6, created_at=datetime.now(timezone.utc)),
        Volunteer(id=13, name="Alice Johnson", phone_number="+254 701 111 111", email="alice.johnson2@gmail.com", description="Tutor for math and science classes.", user_id=1, home_id=6, created_at=datetime.now(timezone.utc)),
        Volunteer(id=14, name="Mia Lee", phone_number="+254 713 333 333", email="mia.lee@gmail.com", description="Coordinator for health and wellness programs.", user_id=13, home_id=7, created_at=datetime.now(timezone.utc)),
        Volunteer(id=15, name="Noah Clark", phone_number="+254 714 444 444", email="noah.clark@gmail.com", description="Assistant for recreational activities.", user_id=14, home_id=7, created_at=datetime.now(timezone.utc)),
        Volunteer(id=16, name="Bob Smith", phone_number="+254 702 222 222", email="bob.smith2@gmail.com", description="Volunteer for facility maintenance.", user_id=2, home_id=7, created_at=datetime.now(timezone.utc)),
        Volunteer(id=17, name="Olivia Walker", phone_number="+254 715 555 555", email="olivia.walker@gmail.com", description="Teaching assistant for literacy programs.", user_id=15, home_id=8, created_at=datetime.now(timezone.utc)),
        Volunteer(id=18, name="Lavender Morara", phone_number="+254 716 666 666", email="lavender.morara@student.moringaschool.com", description="Mentor for extracurricular activities.", user_id=16, home_id=8, created_at=datetime.now(timezone.utc)),
        Volunteer(id=19, name="Carol White", phone_number="+254 703 333 333", email="carol.white2@gmail.com", description="Organizer for community outreach events.", user_id=3, home_id=8, created_at=datetime.now(timezone.utc))
    ]

    with app.app_context():
        print("Seeding volunteers...")
        try:
            if not isinstance(volunteers, (list, tuple)):
                raise TypeError(f"Volunteers is not iterable, got type: {type(volunteers)}")
            db.session.add_all(volunteers)
            db.session.commit()
            print(f"Seeded {len(volunteers)} volunteers successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding volunteers: {e}")
            return

    print("Database successfully seeded!!!!")

if __name__ == '__main__':
    seed_database()