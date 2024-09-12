from djangooo.shortcuts import render
def some_view(request):
    menu_name = 'main_menu'
    current_url = request.path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    menu_dict = {item.id: item for item in menu_items}

    active_item = None
    for item in menu_items:
        if item.url == current_url or (item.named_url and reverse(item.named_url) == current_url):
            active_item = item
            break
    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                tree.append({
                    'item': item,
                    'children': build_tree(items,item)
                })
        return tree

    menu_tree = build_tree(menu_items)

    context = {
        'menu_tree': menu_tree,
        'active_item': active_item,
    }
    return render(request, 'some_template.html', context)
