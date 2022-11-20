from ariadne import convert_kwargs_to_snake_case


def shopping_list_items_resolver(obj, info):
    from api.models import ShoppingListItem
    try:
        items = [item.to_dict() for item in ShoppingListItem.query.all()]
        print(items)
        payload = {
            "success": True,
            "shopping_list_items": items
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def get_shopping_list_item_resolver(obj, info, uid):
    from api.models import ShoppingListItem
    try:
        item = ShoppingListItem.query.get(uid)
        print(item)
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
