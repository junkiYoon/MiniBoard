from flask import request
from flask_restful import Resource

from server.controller.post import (post, delete_post, update_post,
                                    get_posts, get_post_detail)


class Post(Resource):

    def post(self):
        title = request.json['title']
        content = request.json['content']

        return post(title=title, content=content)


class DeletePost(Resource):

    def delete(self):
        post_id = request.json['post_id']

        return delete_post(post_id=post_id)


class UpdatePost(Resource):

    def put(self):
        post_id = request.json['post_id']
        title = request.json['title']
        content = request.json['content']

        return update_post(post_id=post_id, title=title, content=content)


class GetPosts(Resource):

    def get(self):
        return get_posts()


class GetPostDetail(Resource):

    def get(self, post_id):
        return get_post_detail(post_id=post_id)
