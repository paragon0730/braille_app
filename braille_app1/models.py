# models.py

from extensions import db
from datetime import datetime

class EnGrade1(db.Model):
    __tablename__ = 'en_grade1'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False, unique=True)
    bin = db.Column(db.LargeBinary, nullable=False)  # Assuming 'bin' stores binary data for braille

    def __repr__(self):
        return f"<EnGrade1 id={self.id} word='{self.word}'>"

class DiaryEntry(db.Model):
    __tablename__ = 'diary'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<DiaryEntry id={self.id} - date={self.date}>"
    
class EnVoca(db.Model):
    __tablename__ = 'en_voca'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False, unique=True)
    # grade1_bin = db.Column(db.LargeBinary, nullable=True)  # Optional: If you decide to use it later
    # grade2_bin = db.Column(db.LargeBinary, nullable=True)  # Optional: If you decide to use it later

    def __repr__(self):
        return f"<EnVoca id={self.id} word='{self.word}'>"
    
class KoGrade1(db.Model):
    __tablename__ = 'ko_grade1'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False, unique=True)
    bin = db.Column(db.LargeBinary, nullable=False)  # 'bin'은 점자 데이터를 저장한다고 가정합니다.

    def __repr__(self):
        return f"<KoGrade1 id={self.id} word='{self.word}'>"
    
class KoVoca(db.Model):
    __tablename__ = 'ko_voca'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False, unique=True)
    # grade1_bin = db.Column(db.LargeBinary, nullable=True)  # Optional: If you decide to use it later
    # grade2_bin = db.Column(db.LargeBinary, nullable=True)  # Optional: If you decide to use it later

    def __repr__(self):
        return f"<KoVoca id={self.id} word='{self.word}'>"