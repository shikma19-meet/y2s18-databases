from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session = DBSession()

def add_article(main_topic,name_of_article,article_topic,rating):
	new_row = Knowledge(
		main_topic = main_topic,
		name_of_article = name_of_article,
		article_topic = article_topic,
		rating = rating )
	session.add(new_row)
	session.commit()
# add_article("Dance","The basics abount dance","how did dance develop over the years",8)
def query_all_articles():
	new_row = session.query(Knowledge).all()
	return new_row 
print(query_all_articles())

def query_article_by_topic(main_topic):
	new_row = session.query(Knowledge).filter_by(main_topic = main_topic ).all()
	return new_row
print(query_article_by_topic("Dance"))

# def query_article_by_rating(rating):
# 	threshold = input("please enter your threshold, you will get the articals below")
# 	new_row = session.query(Knowledge).filter_by(rating<=threshold).all()
# 	return new_row
# print(query_article_by_rating(1))

def delete_article_by_topic(main_topic):
	session.query(Knowledge).filter_by(main_topic = main_topic).delete()
	session.commit()
# delete_article_by_topic("Dance")
def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
# delete_all_articles()

def edit_article_rating(main_topic, updated_rating):
	articles = session.query(Knowledge).filter_by(main_topic = main_topic).all()
	for article in articles:
		article.rating = updated_rating 
	session.commit() 
edit_article_rating("Dance", 6)

# delete_article_by_rating():






