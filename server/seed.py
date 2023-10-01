from models import User, Post, Reply, Role, Tag
from config import db, app, bcrypt


with app.app_context():

    User.query.delete()
    Post.query.delete()
    Reply.query.delete()
    Role.query.delete()
    Tag.query.delete()

    
    tag1 = Tag(name = 'Apparel')
    tag2 = Tag(name = 'Automotive')
    tag3 = Tag(name = 'Computer and Electronics')
    tag4 = Tag(name = 'Entertainment')
    tag5 = Tag(name = 'Finance')
    tag6 = Tag(name = 'Food')
    tag7 = Tag(name = 'Home and Garden')
    tag8 = Tag(name = 'Children')
    tag9 = Tag(name = 'Sports and Fitness')
    tag10 = Tag(name = 'Travel')
    tag11 = Tag(name = 'Costco')
    tag12 = Tag(name = 'Dyson')
    tag13 = Tag(name = "Osmow's")
    tag14 = Tag(name = 'Walmart')

    db.session.add_all([tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8, tag9, tag10, tag11, tag12, tag13, tag14])
    db.session.commit()


    posts = []

    p1 = Post(
        title='Winter Tire Deals (starts Sep 23)',
        link = 'https://tires.costco.ca/Home',
        expiry = 'December 31, 2023',
        retailer = 'Costco',
        category = 'Automotive',
        content='Winter tire season is fast approaching... whether you like it or not!  Save $150 instantly when you purchase four Bridgestone Tires, valid Sep 23 to Oct 1',
        user_id = 1,
    )

    p1.tagging.append(tag2)
    p1.tagging.append(tag11)

    posts.append(p1)

    p2 = Post(
        title='Buy $50 prepaid MasterCard and receive $7.50 in Walmart gift card',
        link = 'https://getmybonus.ca/CA0923VAN/en',
        expiry = 'September 27, 2023',
        retailer = 'Walmart',
        category = 'Finance',
        content='Saw this deal today in store. Expires Sept. 27 and you have until Sept. 29 to claim your gift card at get my bonus.ca', 
        user_id = 2,
    )

    p2.tagging.append(tag5)
    p2.tagging.append(tag14)

    posts.append(p2)

    p3 = Post(
        title='National Shawarma Day $5 Deals (Oct. 15 2023)',
        expiry = 'October 15, 2023',
        retailer = "Osmow's",
        category = 'Food',
        content="noticed a sign advertising national shawarma day in the window at osmow's tonight. $5 chicken on the rocks, chicken shawarma wrap, falafel on the rocks or falafel wrap", 
        user_id = 3,
    )

    p3.tagging.append(tag6)
    p3.tagging.append(tag13)

    posts.append(p3)

    p4 = Post(
        title='REFURB V8 Animal @ $300 - 15% Rakuten = $255 | V11 @ $495 - 15% Rakuten = $421 F/S',
        link = "https://www.dysoncanada.ca/en/dyson-outlet#shop-all",
        retailer = "Dyson",
        category = 'Home and Garden',
        content="The Dyson V8 Animal is listed on the Dyson website for $300 with 15% cashback from Rakuten", 
        user_id = 1,
    )

    p4.tagging.append(tag7)
    p4.tagging.append(tag12)

    posts.append(p4)

    db.session.add_all(posts)
    db.session.commit()

    replies= []

    r1 = Reply(
        post_id = 2,
        user_id = 4,
        content = "Don't you need to pay a fee or something to activate a prepaid credit card?",
    )

    replies.append(r1)

    db.session.add_all(replies)
    db.session.commit()


    roles = []

    user = Role(
        role_name = 'user',
    )

    roles.append(user)

    moderator = Role(
        role_name = 'moderator',
    )

    roles.append(moderator)

    admin = Role(
        role_name = 'admin',
    )

    roles.append(admin)

    db.session.add_all(roles)
    db.session.commit()

    users = []

    u1 = User(
        username = 'frugal',
        email = '93civic@shaw.ca',
        verified = True,
        role_id = 1,
    )
    u1.password_hash = 'choledochoduodenostomy'

    users.append(u1)

    u2 = User(
        username = 'buynowthinklater',
        email = 'captain@bell.com',
        verified = True,
        role_id = 1,
    )
    u2.password_hash = 'duodenocholedochotomy'

    users.append(u2)

    u3 = User(
        username = 'Eclipse',
        email = 'homer01@rogers.com',
        verified = True,
        role_id = 2,
    )
    u3.password_hash = 'disestablishmentarianism'

    users.append(u3)

    u4 = User(
        username = 'DealBrowser',
        email = 'fluidmin@msn.com',
        verified = True,
        role_id = 1,
    )
    u4.password_hash = 'electroencephalographically'

    users.append(u4)

    u5 = User(
        username = 'freeiscool',
        email = 'phil@hotdeals.com',
        verified = True,
        role_id = 3,
    )
    u5.password_hash = 'nonphenomenally'

    users.append(u5)

    db.session.add_all(users)
    db.session.commit()

   
   
    
    
    



