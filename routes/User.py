from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_claims
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource
from mongoengine import FieldDoesNotExist, NotUniqueError, DoesNotExist, InvalidQueryError

from errors import NoAuthorizationError, InternalServerError, SchemaValidationError, EmailAlreadyExistsError, \
    DeletingUserError, UpdatingUserError
from models.User import User


class User2Api(Resource):
    @jwt_required
    def get(self):
        try:
            if 'admin' in get_jwt_claims()['roles']:
                users = User.objects().to_json()
                return Response(users, mimetype='application/json', status=200)
        except NoAuthorizationError:
            raise NoAuthorizationError
        except Exception:
            raise InternalServerError

    @jwt_required
    def post(self):
        try:
            if 'admin' in get_jwt_claims()['roles']:
                body = request.get_json()
                user = User(**body)
                user.hash_password()
                user.save()
                id = user.id
                return {'id': str(id)}, 201
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError


class UserApi(Resource):
    @jwt_required
    def delete(self, id):
        try:
            if 'admin' in get_jwt_claims()['roles']:
                user = User.objects().get(id=id)
                user.delete()
                return 'None', 204
        except DoesNotExist:
            raise DeletingUserError
        except Exception:
            raise InternalServerError

    @jwt_required
    def put(self, id):
        try:
            if 'admin' in get_jwt_claims()['roles']:
                User.objects.get(id=id)
                body = request.get_json()
                User.objects.get(id=id).update(**body)
                return 'None', 204
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserError
        except Exception:
            raise InternalServerError
