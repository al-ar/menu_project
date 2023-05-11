from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.all().filter(menu_name__name=menu_name)
    current_url = context.request.path
    tree = []
    for item in menu_items:

        tree.append({
            'id': item.id,
            'title': item.title,
            'parent_slug':  None if item.parent == None else f'/{item.parent.slug}/',
            'parent_id': item.parent_id,
            'slug': f'/{item.slug}/' if item.slug != '' else '/',
            'level': item.level,
            'active': False,
        })
    for item in tree:
        if item['level'] < 2:
            item['active'] = True
        elif item['parent_slug'] == current_url:
            item['active'] = True

        if item['slug'] == current_url:
            item['active'] = True
            parent_id = item['parent_id']
            while parent_id is not None:
                for parent_item in tree:
                    if parent_item['id'] == parent_id:
                        parent_item['active'] = True
                        parent_id = parent_item['parent_id']
                        break

    return {
        'menu_tree': tree,
        'menu_name': menu_name,
        }


@register.simple_tag(takes_context=True)
def render_menu(context, menu_tree, current_item=None):

    result = ''
    for item in menu_tree:

        if item['parent_id'] == current_item and item['active']:
            result += f'<li><a href="{item["slug"]}" > {item["title"]}</a>'

            sub_menu = render_menu(context, menu_tree, item['id'])
            result += f' <ul> {sub_menu} </ul> '
    return result
