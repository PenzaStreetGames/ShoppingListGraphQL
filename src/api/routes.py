from flask import Blueprint, request, jsonify
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType
)
from ariadne.constants import PLAYGROUND_HTML
from api.queries import (
    shopping_list_items_resolver,
    get_shopping_list_item_resolver
)
from api.mutations import (
    create_shopping_list_item_resolver,
    update_shopping_list_item_resolver,
    delete_shopping_list_item_resolver
)

urls_blueprint = Blueprint('urls', __name__)

query = ObjectType("Query")
query.set_field("listShoppingListItems", shopping_list_items_resolver)
query.set_field("getShoppingListItem", get_shopping_list_item_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createShoppingListItem", create_shopping_list_item_resolver)
mutation.set_field("updateShoppingListItem", update_shopping_list_item_resolver)
mutation.set_field("deleteShoppingListItem", delete_shopping_list_item_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, snake_case_fallback_resolvers, query, mutation
)


@urls_blueprint.route('/graphql', methods=["GET"])
def graphql_playground():  # put application's code here
    return PLAYGROUND_HTML, 200


@urls_blueprint.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
