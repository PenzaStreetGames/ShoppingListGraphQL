from ariadne import convert_kwargs_to_snake_case
from uuid import uuid4


@convert_kwargs_to_snake_case
def create_shopping_list_item_resolver(obj, info, name, quantity, completed, user_uid):
    from api.models import ShoppingListItem
    from main import db

    try:
        uid = str(uuid4())
        item = ShoppingListItem(
            uid=uid,
            name=name,
            quantity=quantity,
            completed=completed,
            user_uid=user_uid
        )
        print(item.to_dict())
        db.session.add(item)
        db.session.commit()
        payload = {
            "success": True,
            "shopping_list_item": item.to_dict()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def update_shopping_list_item_resolver(obj, info, uid, name, quantity, completed, user_uid):
    from api.models import ShoppingListItem
    from main import db

    try:
        item = ShoppingListItem.query.get(uid)
        item.name = name
        item.quantity = quantity
        item.completed = completed
        item.user_uid = user_uid
        print(item)
        db.session.add(item)
        db.session.commit()
        payload = {
            "success": True,
            "shopping_list_item": item.to_dict()
        }
    except AttributeError as error:
        payload = {
            "success": False,
            "errors": [f"Не найден uid {uid}"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_shopping_list_item_resolver(obj, info, uid):
    from api.models import ShoppingListItem
    from main import db

    try:
        item = ShoppingListItem.query.get(uid)
        print(item)
        db.session.delete(item)
        db.session.commit()
        payload = {
            "success": True,
            "shopping_list_item": item.to_dict()
        }
    except AttributeError as error:
        payload = {
            "success": False,
            "errors": [f"Не найден uid {uid}"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
