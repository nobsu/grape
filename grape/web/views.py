# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask import g, request, flash, current_app, make_response, jsonify, abort
from flask import render_template, redirect, url_for, send_from_directory


from ..classifydoc.predict import document_classify

home = Blueprint('home', __name__, static_url_path="/static", template_folder='templates', static_folder='static')


@home.route('/v3')
def index():

    return render_template('page.html')

@home.route('/hello', methods=['GET', 'POST'])
def hello():

    from config import Config
    print Config.SQLALCHEMY_DATABASE_URI
    # return "hello大坏蛋"
    return render_template('hello.html')

@home.route('/')
@home.route('/<slug>', methods=['GET', 'POST'])
def page(slug=None):
    if slug:
        if slug == 'news-classify':
            return news_classify()
        elif slug == 'search':
            return 'search'
        slug = slug.split('-')[-1]
        page = {
            'title': 'nlp',
            'content': 'content' + str(slug)
        }
    else:
        page = {
            'title': 'nlp',
            'content': 'content'
        }
    if not page:
        abort(404)
    return render_template('home.html',
                        page_content=page['content'],
                        page_title=page['title'])


def news_classify():
    if request.method == 'POST':
        classifier = request.form['classifier']
        title = request.form['title']
        content = request.form['content']

        ret = ''
        result = document_classify(classifier, title, content)
        for r in result:
            ret += r

        return render_template('classify_result.html', result=ret)
    else:
        return render_template('404.html'), 404
