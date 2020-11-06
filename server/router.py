from flask import Blueprint
from flask_restful import Api

bp = Blueprint("post", __name__, url_prefix="")
api_basic = Api(bp)

from server.view.ping import Ping
api_basic.add_resource(Ping, "/ping")

from server.view.post import Post
api_basic.add_resource(Post, "/post")

from server.view.post import DeletePost
api_basic.add_resource(DeletePost, '/delete')

from server.view.post import UpdatePost
api_basic.add_resource(UpdatePost, '/update')

from server.view.post import GetPosts
api_basic.add_resource(GetPosts, '/posts')

from server.view.post import GetPostDetail
api_basic.add_resource(GetPostDetail, '/posts/<int:post_id>')
