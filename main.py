#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +\
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # commit transactions
db = SQLAlchemy(app)


clanguages = db.Table(
    "clanguages",
    db.Column('char_id', db.Integer, db.ForeignKey('characters.id'),
              primary_key=True),
    db.Column('language_id', db.Integer, db.ForeignKey('languages.id'),
              primary_key=True)
)
cfeats = db.Table(
    "cfeats",
    db.Column('char_id', db.Integer, db.ForeignKey('characters.id'),
              primary_key=True),
    db.Column('feat_id', db.Integer, db.ForeignKey('feats.id'),
              primary_key=True)
)
ctalents = db.Table(
    "ctalents",
    db.Column('char_id', db.Integer, db.ForeignKey('characters.id'),
              primary_key=True),
    db.Column('talent_id', db.Integer, db.ForeignKey('talents.id'),
              primary_key=True)
)
cskills = db.Table(
    "cfeats",
    db.Column('char_id', db.Integer, db.ForeignKey('characters.id'),
              primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skills.id'),
              primary_key=True)
)
cpowers = db.Table(
    "cpowers",
    db.Column('char_id', db.Integer, db.ForeignKey('characters.id'),
              primary_key=True),
    db.Column('power_id', db.Integer, db.ForeignKey('powers.id'),
              primary_key=True),
    db.Column('instances', db.Integer)
)


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    species_id = db.Column(db.ForeignKey('species.id'))
    age = db.Column(db.Float)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    char_class_id = db.Column(db.ForeignKey('classes.id'))
    destiny_points = db.Column(db.Integer)  # smallint
    force_points = db.Column(db.Integer)  # smallint
    dark_side_points = db.Column(db.Integer)  # smallint
    hit_points = db.Column(db.Integer)
    condition_track = db.Column(db.Integer)  # smallint, signed
    melee_bonus = db.Column(db.Integer)  # smallint
    ranged_bonus = db.Column(db.Integer)  # smallint
    b_strength = db.Column(db.Integer)  # smallint
    b_dexterity = db.Column(db.Integer)  # smallint
    b_constitution = db.Column(db.Integer)  # smallint
    b_intelligence = db.Column(db.Integer)  # smallint
    b_wisdom = db.Column(db.Integer)  # smallint
    b_charisma = db.Column(db.Integer)  # smallint
    d_fortitude = db.Column(db.Integer)  # smallint
    d_reflex = db.Column(db.Integer)  # smallint
    d_will = db.Column(db.Integer)  # smallint
    xp = db.Column(db.Integer)  # bigint
    languages = db.relationship('Language', secondary=clanguages,
                                backref=db.backref('characters', lazy='dynamic'))
    feats = db.relationship('Feat', secondary=cfeats,
                            backref=db.backref('characters', lazy='dynamic'))
    talents = db.relationship('Talent', secondary=ctalents,
                              backref=db.backref('characters', lazy='dynamic'))
    skills = db.relationship('Skill', secondary=cskills,
                             backref=db.backref('characters', lazy='dynamic'))
    powers = db.relationship('Power', secondary=cpowers,
                             backref=db.backref('characters', lazy='dynamic'))
    # inventory -- list of foreign keys


class Language(db.Model):
    __tablename__ = "languages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    rare = db.Column(db.Boolean)


# racial languages
slanguages = db.Table(
    "rlanguages",
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'),
              primary_key=True),
    db.Column('language_id', db.Integer, db.ForeignKey('languages.id'),
              primary_key=True)
)


class Species(db.Model):
    __tablename__ = "species"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # mods


class CharacterClass(db.model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # mods

