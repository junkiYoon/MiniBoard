from flask import abort

from server.model import session
from server.model.posts import Posts


def post(title, content):
    new_post = Posts(title=title, content=content)

    session.add(new_post)

    session.commit()

    return {
        'message': 'Create post successfully'
    }, 201


def delete_post(post_id):
    del_data = session.query(Posts).filter(Posts.id == post_id).first()

    if del_data:
        session.delete(del_data)

        session.commit()

        return {
            'message': 'Delete post successfully'
        }
    else:
        return abort(404, 'There is no post you looking for')


def update_post(post_id, title, content):
    udt_post = session.query(Posts).filter(Posts.id == post_id).first()

    if udt_post:
        udt_post.title = title
        udt_post.content = content

        session.commit()

        return {
            'message': 'Update post successfully'
        }
    else:
        return abort(404, 'There is no post you looking for')


def get_posts():
    posts = session.query(Posts).all()
    if posts:
        return {
            "posts": [{
                "title": post.title,
                "content": post.content,
                "created_at": str(post.created_at)
            } for post in posts]
        }
    else:
        return abort(404, 'There is not any post')


def get_post_detail(post_id):
    post_detail = session.query(Posts).filter(Posts.id == post_id).first()
    if post_detail:
        return {
            "title": post_detail.title,
            "content": post_detail.content,
            "created_at": str(post_detail.created_at)
        }
    else:
        return abort(404, 'There is no post you looking for')
