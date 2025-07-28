import random
from datetime import datetime, timedelta, timezone
from app import db, create_app
from werkzeug.security import generate_password_hash
from app.models.user import User  # Adjust import based on your project structure
from app.models.children_home import ChildrenHome  # Adjust import based on your project structure
from app.models.children_home import Child  # Adjust import based on your project structure
from app.models.children_home import Photo  # Adjust import based on your project structure
from app.models.donation import Donation  # Adjust import based on your project structure
from app.models.review import Review  # Adjust import based on your project structure
from app.models.visit import Visit  # Adjust import based on your project structure
from app.models.volunteer import Volunteer  # Adjust import based on your project structure

def seed_database():
    app = create_app()  # Initialize the Flask app
    with app.app_context():
        # Clear existing data (optional, comment out to append instead of replace)
        db.session.query(Volunteer).delete()
        db.session.query(Visit).delete()
        db.session.query(Review).delete()
        db.session.query(Donation).delete()
        db.session.query(Photo).delete()
        db.session.query(Child).delete()
        db.session.query(ChildrenHome).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Seed Users (15 regular users + 1 admin, IDs 1–16)
        users_data = [
            {'id': 1, 'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'phone_number': '+254 701 111 111', 'password': 'Password123!', 'role': 'user'},
            {'id': 2, 'name': 'Bob Smith', 'email': 'bob.smith@example.com', 'phone_number': '+254 702 222 222', 'password': 'SecurePass456!', 'role': 'user'},
            {'id': 3, 'name': 'Carol White', 'email': 'carol.white@example.com', 'phone_number': '+254 703 333 333', 'password': 'MyPass789!', 'role': 'user'},
            {'id': 4, 'name': 'David Brown', 'email': 'david.brown@example.com', 'phone_number': '+254 704 444 444', 'password': 'Dav1d!2023', 'role': 'user'},
            {'id': 5, 'name': 'Emma Davis', 'email': 'emma.davis@example.com', 'phone_number': '+254 705 555 555', 'password': 'Emma#9876', 'role': 'user'},
            {'id': 6, 'name': 'Frank Wilson', 'email': 'frank.wilson@example.com', 'phone_number': '+254 706 666 666', 'password': 'Frankie!321', 'role': 'user'},
            {'id': 7, 'name': 'Grace Taylor', 'email': 'grace.taylor@example.com', 'phone_number': '+254 707 777 777', 'password': 'GracePass!654', 'role': 'user'},
            {'id': 8, 'name': 'Henry Martinez', 'email': 'henry.martinez@example.com', 'phone_number': '+254 708 888 888', 'password': 'H3nry!111', 'role': 'user'},
            {'id': 9, 'name': 'Isabella Anderson', 'email': 'isabella.anderson@example.com', 'phone_number': '+254 709 999 999', 'password': 'Bella!222', 'role': 'user'},
            {'id': 10, 'name': 'James Thomas', 'email': 'james.thomas@example.com', 'phone_number': '+254 710 101 010', 'password': 'Jam3s!333', 'role': 'user'},
            {'id': 11, 'name': 'Kelly Garcia', 'email': 'kelly.garcia@example.com', 'phone_number': '+254 711 111 111', 'password': 'K3lly!444', 'role': 'user'},
            {'id': 12, 'name': 'Liam Rodriguez', 'email': 'liam.rodriguez@example.com', 'phone_number': '+254 712 222 222', 'password': 'L1am!555', 'role': 'user'},
            {'id': 13, 'name': 'Mia Lee', 'email': 'mia.lee@example.com', 'phone_number': '+254 713 333 333', 'password': 'M1aPass!666', 'role': 'user'},
            {'id': 14, 'name': 'Noah Clark', 'email': 'noah.clark@example.com', 'phone_number': '+254 714 444 444', 'password': 'N0ah!777', 'role': 'user'},
            {'id': 15, 'name': 'Olivia Walker', 'email': 'olivia.walker@example.com', 'phone_number': '+254 715 555 555', 'password': 'Ol1v1a!888', 'role': 'user'},
            {'id': 16, 'name': 'Admin User', 'email': 'admin@example.com', 'phone_number': '+254 716 666 666', 'password': 'AdminPass!999', 'role': 'admin'},
        ]

        # User IDs for reference:
        # 1: Alice Johnson, 2: Bob Smith, 3: Carol White, 4: David Brown, 5: Emma Davis,
        # 6: Frank Wilson, 7: Grace Taylor, 8: Henry Martinez, 9: Isabella Anderson, 10: James Thomas,
        # 11: Kelly Garcia, 12: Liam Rodriguez, 13: Mia Lee, 14: Noah Clark, 15: Olivia Walker,
        # 16: Admin User
        for user_data in users_data:
            user = User(
                id=user_data['id'],
                name=user_data['name'],
                email=user_data['email'],
                role=user_data['role'],
                created_at=datetime.utcnow()
            )
            user.set_password(user_data['password'])
            db.session.add(user)

        # Seed Children's Homes (8 homes, IDs 1–8)
        homes_data = [
            {
                'id': 1,
                'name': 'Sunshine Orphanage',
                'location': 'Nairobi, Kenya',
                'phone_number': '+254 700 123 456',
                'email': 'sunshine.orphanage@example.com',
                'description': 'A loving home for children in Nairobi.',
                'images': [
                    'http://example.com/sunshine_image1.jpg',
                    'http://example.com/sunshine_image2.jpg',
                    'http://example.com/sunshine_image3.jpg',
                    'http://example.com/sunshine_image4.jpg'
                ]
            },
            {
                'id': 2,
                'name': 'Hope Haven',
                'location': 'Mombasa, Kenya',
                'phone_number': '+254 711 234 567',
                'email': 'hope.haven@example.com',
                'description': 'Providing care and education in Mombasa.',
                'images': [
                    'http://example.com/hope_image1.jpg',
                    'http://example.com/hope_image2.jpg',
                    'http://example.com/hope_image3.jpg',
                    'http://example.com/hope_image4.jpg'
                ]
            },
            {
                'id': 3,
                'name': 'Bright Future Home',
                'location': 'Kisumu, Kenya',
                'phone_number': '+254 722 345 678',
                'email': 'bright.future@example.com',
                'description': 'Empowering children in Kisumu.',
                'images': [
                    'http://example.com/bright_image1.jpg',
                    'http://example.com/bright_image2.jpg',
                    'http://example.com/bright_image3.jpg',
                    'http://example.com/bright_image4.jpg'
                ]
            },
            {
                'id': 4,
                'name': 'New Dawn Shelter',
                'location': 'Eldoret, Kenya',
                'phone_number': '+254 733 456 789',
                'email': 'new.dawn@example.com',
                'description': 'A safe haven for children in Eldoret.',
                'images': [
                    'http://example.com/dawn_image1.jpg',
                    'http://example.com/dawn_image2.jpg',
                    'http://example.com/dawn_image3.jpg',
                    'http://example.com/dawn_image4.jpg'
                ]
            },
            {
                'id': 5,
                'name': 'Peaceful Home',
                'location': 'Nakuru, Kenya',
                'phone_number': '+254 744 567 890',
                'email': 'peaceful.home@example.com',
                'description': 'Nurturing children in Nakuru.',
                'images': [
                    'http://example.com/peace_image1.jpg',
                    'http://example.com/peace_image2.jpg',
                    'http://example.com/peace_image3.jpg',
                    'http://example.com/peace_image4.jpg'
                ]
            },
            {
                'id': 6,
                'name': 'Starlight Orphanage',
                'location': 'Thika, Kenya',
                'phone_number': '+254 755 678 901',
                'email': 'starlight@example.com',
                'description': 'Brightening lives in Thika.',
                'images': [
                    'http://example.com/starlight_image1.jpg',
                    'http://example.com/starlight_image2.jpg',
                    'http://example.com/starlight_image3.jpg',
                    'http://example.com/starlight_image4.jpg'
                ]
            },
            {
                'id': 7,
                'name': 'Harmony House',
                'location': 'Nyeri, Kenya',
                'phone_number': '+254 766 789 012',
                'email': 'harmony.house@example.com',
                'description': 'A caring community in Nyeri.',
                'images': [
                    'http://example.com/harmony_image1.jpg',
                    'http://example.com/harmony_image2.jpg',
                    'http://example.com/harmony_image3.jpg',
                    'http://example.com/harmony_image4.jpg'
                ]
            },
            {
                'id': 8,
                'name': 'Unity Home',
                'location': 'Kakamega, Kenya',
                'phone_number': '+254 777 890 123',
                'email': 'unity.home@example.com',
                'description': 'Fostering unity in Kakamega.',
                'images': [
                    'http://example.com/unity_image1.jpg',
                    'http://example.com/unity_image2.jpg',
                    'http://example.com/unity_image3.jpg',
                    'http://example.com/unity_image4.jpg'
                ]
            },
        ]

        home_id_mapping = {}
        for home_data in homes_data:
            home = ChildrenHome(
                id=home_data['id'],
                name=home_data['name'],
                location=home_data['location'],
                phone_number=home_data['phone_number'],
                email=home_data['email'],
                description=home_data['description'],
                images=home_data['images'],
                created_at=datetime.now(timezone.utc)
            )
            db.session.add(home)
            home_id_mapping[home_data['name']] = home.id

        # Seed Children (12–17 children per home, IDs auto-increment)
        children_data = []
        first_names = [
            'John', 'Mary', 'Peter', 'Susan', 'Ahmed', 'Fatima', 'Omar', 'Aisha',
            'James', 'Grace', 'David', 'Mercy', 'Joseph', 'Esther', 'Samuel', 'Ruth',
            'Michael', 'Jane', 'Paul', 'Lucy', 'Daniel', 'Rose', 'Thomas', 'Ann',
            'Patrick', 'Joyce', 'Simon', 'Faith', 'Brian', 'Dorothy', 'Kevin', 'Lilian'
        ]
        last_names = [
            'Mwangi', 'Wanjiku', 'Kamau', 'Njeri', 'Ali', 'Hassan', 'Juma', 'Mohammed',
            'Ochieng', 'Atieno', 'Otieno', 'Auma', 'Kiprop', 'Chebet', 'Kiptoo', 'Jelimo',
            'Njoroge', 'Wambui', 'Mbugua', 'Nyambura', 'Kimani', 'Wanjiru', 'Kariuki', 'Wairimu',
            'Maina', 'Muthoni', 'Ndungu', 'Wanjiku', 'Omondi', 'Adhiambo', 'Owino', 'Anyango'
        ]
        genders = ['Male', 'Female']

        for home_data in homes_data:
            home_id = home_id_mapping[home_data['name']]
            num_children = random.randint(12, 17)  # Random number of children (12–17)
            used_names = set()  # Ensure unique names within each home
            for _ in range(num_children):
                # Generate a unique name
                while True:
                    first = random.choice(first_names)
                    last = random.choice(last_names)
                    full_name = f"{first} {last}"
                    if full_name not in used_names:
                        used_names.add(full_name)
                        break
                child = {
                    'name': full_name,
                    'age': random.randint(7, 15),  # Ages 7–15
                    'gender': random.choice(genders),
                    'home_id': home_id
                }
                children_data.append(child)

        for child_data in children_data:
            child = Child(
                name=child_data['name'],
                age=child_data['age'],
                gender=child_data['gender'],
                home_id=child_data['home_id'],
                created_at=datetime.utcnow()
            )
            db.session.add(child)

        # Seed Photos (4 photos per home, 32 total, IDs auto-increment)
        photos_data = []
        for home_data in homes_data:
            home_id = home_id_mapping[home_data['name']]
            for image_url in home_data['images']:
                photos_data.append({
                    'image_url': image_url,
                    'children_home_id': home_id
                })

        for photo_data in photos_data:
            photo = Photo(
                image_url=photo_data['image_url'],
                children_home_id=photo_data['children_home_id']
            )
            db.session.add(photo)

        # Seed Donations (18 total, 1–2 per home, IDs auto-increment)
        donation_types = ['cash', 'in-kind']
        donations_data = []
        home_donation_counts = {home_id: random.randint(1, 2) for home_id in home_id_mapping.values()}
        # Adjust counts to ensure exactly 18 donations
        total_donations = sum(home_donation_counts.values())
        while total_donations < 18:
            home_id = random.choice(list(home_id_mapping.values()))
            if home_donation_counts[home_id] < 2:
                home_donation_counts[home_id] += 1
                total_donations += 1
        while total_donations > 18:
            home_id = random.choice([hid for hid, count in home_donation_counts.items() if count > 1])
            home_donation_counts[home_id] -= 1
            total_donations -= 1

        for home_id, count in home_donation_counts.items():
            for _ in range(count):
                donations_data.append({
                    'amount': random.randint(1000, 50000),  # Amounts between 1,000 and 50,000
                    'donation_type': random.choice(donation_types),
                    'user_id': random.randint(1, 15),  # Exclude admin (ID 16)
                    'home_id': home_id,
                    'created_at': datetime.utcnow()
                })

        for donation_data in donations_data:
            donation = Donation(
                amount=donation_data['amount'],
                donation_type=donation_data['donation_type'],
                user_id=donation_data['user_id'],
                home_id=donation_data['home_id'],
                created_at=donation_data['created_at']
            )
            db.session.add(donation)

        # Seed Reviews (14 total, 1–2 per home, IDs auto-increment)
        review_comments = [
            'Wonderful staff and facilities!', 'Needs more resources but caring environment.',
            'Great place for children to grow.', 'Very supportive community.',
            'Clean and well-maintained home.', 'Amazing work for the kids!',
            'Could improve on activities.', 'Friendly and welcoming staff.',
            'A true home for the children.', 'Dedicated caregivers, highly recommend.',
            'Well-organized and safe.', 'Inspiring place, keep it up!',
            'Good environment but needs funding.', 'Heartwarming to see the care provided.'
        ]
        reviews_data = []
        home_review_counts = {home_id: random.randint(1, 2) for home_id in home_id_mapping.values()}
        # Adjust counts to ensure exactly 14 reviews
        total_reviews = sum(home_review_counts.values())
        while total_reviews < 14:
            home_id = random.choice(list(home_id_mapping.values()))
            if home_review_counts[home_id] < 2:
                home_review_counts[home_id] += 1
                total_reviews += 1
        while total_reviews > 14:
            home_id = random.choice([hid for hid, count in home_review_counts.items() if count > 1])
            home_review_counts[home_id] -= 1
            total_reviews -= 1

        for home_id, count in home_review_counts.items():
            for _ in range(count):
                reviews_data.append({
                    'rating': random.randint(3, 5),  # Ratings 3–5 for realism
                    'comment': random.choice(review_comments),
                    'user_id': random.randint(1, 15),  # Exclude admin (ID 16)
                    'home_id': home_id,
                    'created_at': datetime.utcnow()
                })

        for review_data in reviews_data:
            review = Review(
                rating=review_data['rating'],
                comment=review_data['comment'],
                user_id=review_data['user_id'],
                home_id=review_data['home_id'],
                created_at=review_data['created_at']
            )
            db.session.add(review)

        # Seed Visits (10 total, distributed across homes, IDs auto-increment)
        visits_data = []
        home_visit_counts = {home_id: 0 for home_id in home_id_mapping.values()}
        # Distribute 10 visits randomly
        for _ in range(10):
            home_id = random.choice(list(home_id_mapping.values()))
            home_visit_counts[home_id] += 1
        # Ensure at least one visit per home if possible, then fill remaining
        for home_id in home_id_mapping.values():
            if home_visit_counts[home_id] == 0 and sum(home_visit_counts.values()) < 10:
                home_visit_counts[home_id] = 1
        # Adjust to exactly 10 visits
        total_visits = sum(home_visit_counts.values())
        while total_visits < 10:
            home_id = random.choice(list(home_id_mapping.values()))
            home_visit_counts[home_id] += 1
            total_visits += 1
        while total_visits > 10:
            home_id = random.choice([hid for hid, count in home_visit_counts.items() if count > 1])
            home_visit_counts[home_id] -= 1
            total_visits -= 1

        for home_id, count in home_visit_counts.items():
            for _ in range(count):
                user = random.choice(users_data[:15])  # Exclude admin
                visits_data.append({
                    'full_name': user['name'],
                    'phone_number': user['phone_number'],
                    'day_to_visit': datetime.utcnow() + timedelta(days=random.randint(1, 30)),  # Future dates
                    'number_of_visitors': random.randint(1, 5),  # Reasonable number
                    'user_id': user['id'],
                    'home_id': home_id,
                    'created_at': datetime.utcnow()
                })

        for visit_data in visits_data:
            visit = Visit(
                full_name=visit_data['full_name'],
                phone_number=visit_data['phone_number'],
                day_to_visit=visit_data['day_to_visit'],
                number_of_visitors=visit_data['number_of_visitors'],
                user_id=visit_data['user_id'],
                home_id=visit_data['home_id'],
                created_at=visit_data['created_at']
            )
            db.session.add(visit)

        # Seed Volunteers (all users, each home 1–3 volunteers, IDs auto-increment)
        volunteer_descriptions = [
            'Teaching assistant for literacy programs.',
            'Mentor for children’s extracurricular activities.',
            'Organizer for community outreach events.',
            'Support staff for daily operations.',
            'Tutor for math and science classes.',
            'Coordinator for health and wellness programs.',
            'Assistant for recreational activities.',
            'Volunteer for facility maintenance.'
        ]
        volunteers_data = []
        # Ensure every user volunteers at least once
        for user in users_data:
            num_homes = random.randint(1, 3)  # Each user volunteers at 1–3 homes
            selected_homes = random.sample(list(home_id_mapping.values()), num_homes)
            for home_id in selected_homes:
                volunteers_data.append({
                    'name': user['name'],
                    'phone_number': user['phone_number'],
                    'email': user['email'],
                    'description': random.choice(volunteer_descriptions),
                    'user_id': user['id'],
                    'home_id': home_id,
                    'created_at': datetime.utcnow()
                })

        # Ensure each home has at least one volunteer
        for home_id in home_id_mapping.values():
            if not any(v['home_id'] == home_id for v in volunteers_data):
                user = random.choice(users_data)
                volunteers_data.append({
                    'name': user['name'],
                    'phone_number': user['phone_number'],
                    'email': user['email'],
                    'description': random.choice(volunteer_descriptions),
                    'user_id': user['id'],
                    'home_id': home_id,
                    'created_at': datetime.utcnow()
                })

        for volunteer_data in volunteers_data:
            volunteer = Volunteer(
                name=volunteer_data['name'],
                phone_number=volunteer_data['phone_number'],
                email=volunteer_data['email'],
                description=volunteer_data['description'],
                user_id=volunteer_data['user_id'],
                home_id=volunteer_data['home_id'],
                created_at=volunteer_data['created_at']
            )
            db.session.add(volunteer)

       
        db.session.commit()
        print(f"Successfully seeded {len(users_data)} users, {len(homes_data)} homes, "
              f"{len(children_data)} children, {len(photos_data)} photos, "
              f"{len(donations_data)} donations, {len(reviews_data)} reviews, "
              f"{len(visits_data)} visits, and {len(volunteers_data)} volunteers.")

if __name__ == '__main__':
    seed_database()