from faker import Faker
from models import User, Post, Reply, Role
from config import db, app, bcrypt

faker = Faker()

with app.app_context():

    User.query.delete()
    Post.query.delete()
    Reply.query.delete()

    for _ in range(20):
        username = faker.profile(fields=["username"])["username"]
        user = User(
            username=username
        )
        
        user.password_hash = username # We are calling the password_hash setter method here
        db.session.add(user)
        db.session.commit()


        posts = []

        p1 = Post(
            title='Winter Tire Deals (starts Sep 23)'
            link = 'https://tires.costco.ca/Home'
            expiry = 'December 31, 2023'
            retailer = 'Costco'
            content='Winter tire season is fast approaching... whether you like it or not!  Save $150 instantly when you purchase four Bridgestone Tires, valid Sep 23 to Oct 1' 
            user_id = 1
        )

        posts.append(p1)

        p2 = Post(
            title='Buy $50 prepaid MasterCard and receive $7.50 in Walmart gift card'
            link = 'https://getmybonus.ca/CA0923VAN/en'
            expiry = 'September 27, 2023'
            retailer = 'Walmart'
            content='Saw this deal today in store. Expires Sept. 27 and you have until Sept. 29 to claim your gift card at get my bonus.ca' 
            user_id = 2
        )

        posts.append(p2)

        p3 = Post(
            title='National Shawarma Day $5 Deals (Oct. 15 2023)'
            expiry = 'October 15, 2023'
            retailer = "Osmow's"
            content="noticed a sign advertising national shawarma day in the window at osmow's tonight. $5 chicken on the rocks, chicken shawarma wrap, falafel on the rocks or falafel wrap" 
            user_id = 3
        )

        posts.append(p3)

        p4 = Post(
            title='REFURB V8 Animal @ $300 - 15% Rakuten = $255 | V11 @ $495 - 15% Rakuten = $421 F/S'
            link = "https://www.dysoncanada.ca/en/dyson-outlet#shop-all"
            retailer = "Dyson"
            content="The Dyson V8 Animal is listed on the Dyson website for $300 with 15% cashback from Rakuten" 
            user_id = 1
        )

        posts.append(p4)

        db.session.add_all(posts)
        db.session.commit()

        replies= []

        r1 = Reply(
            post_id = 2
            user_id = 4
            content = "Don't you need to pay a fee or something to activate a prepaid credit card?"
        )

        replies.append(r1)

        db.session.add_all(replies)
        db.session.commit()


        roles = []

        user = Role(
            role_name = 'user'
        )

        roles.append(user)

        moderator = Role(
            role_name = 'moderator'
        )

        roles.append(moderator)

        admin = Role(
            role_name = 'admin'
        )

        roles.append(admin)

        db.session.add_all(roles)
        db.session.commit()

        users = []

        u1 = User(
            username = 'frugal'
            email = '93civic@shaw.ca'
            verified = True
            role_id = 1
        )
        u1.password_hash = 'choledochoduodenostomy'

        user.append(u1)

        u2 = User(
            username = 'buynowthinklater'
            email = 'captain@bell.com'
            verified = True
            role_id = 1
        )
        u2.password_hash = 'duodenocholedochotomy'

        user.append(u2)

        u3 = User(
            username = 'Eclipse'
            email = 'homer01@rogers.com'
            verified = True
            role_id = 2
        )
        u3.password_hash = 'disestablishmentarianism'

        user.append(u3)

        u4 = User(
            username = 'DealBrowser'
            email = 'fluidmin@msn.com'
            verified = True
            role_id = 1
        )
        u4.password_hash = 'electroencephalographically'

        user.append(u4)

        u5 = User(
            username = 'freeiscool'
            email = 'phil@hotdeals.com'
            verified = True
            role_id = 3
        )
        u5.password_hash = 'nonphenomenally'

        user.append(u5)

        db.session.add_all(users)
        db.session.commit()



