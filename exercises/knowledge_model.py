from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	__tablename__ = 'Knowledge'
	# The first column will be the primary key
	student_id = Column(Integer, primary_key = True)
	# The second column should be a string representing
	main_topic = Column(String)
	# the name of the Wiki article that you're referencing
	name_of_article = Column(String )
	# The third column will be a string representing the 
	# topic of the article.
	article_topic = Column(String)
	# The last column will be
	# an integer, representing your rating of the article.
	rating = Column(Integer)

	def __repr__(self):
		return (" main topic : {}\n"
			    "name of article {}\n"
			    "article topic {}\n"
			    "rating {}\n").format(self.main_topic,self.name_of_article,self.article_topic,self.rating)

#print(repr(Knowledge.__table__))

