import ast
from collections import defaultdict
from config import prefix_mapping, excluded_tags

def extract_tags(x):
    if isinstance(x, list):
        return [str(tag).strip() for tag in x]
    if isinstance(x, str):
        try:
            val = ast.literal_eval(x)
            if isinstance(val, list):
                return [str(tag).strip() for tag in val]
            else:
                return [x.strip()]
        except:
            if ',' in x:
                return [tag.strip() for tag in x.split(',')]
            else:
                return [x.strip()]
    return []

def categorize_tags(tags):
    from config import category_tree  # přidáme dovoz sem, pokud už není nahoře

    categorized = defaultdict(list)
    for tag in tags:
        if tag in excluded_tags or tag.endswith('_chat'):
            continue

        # Zkontrolujeme, jestli tag patří do nějaké subkategorie v category_tree
        found = False
        for category, subcats in category_tree.get('Product', {}).items():
            if tag in subcats:
                categorized['Product'].append(tag)
                found = True
                break

        if found:
            continue

        # Jinak klasifikujeme podle prefixu
        prefix = tag.split('_')[0] if '_' in tag else 'Request'
        category = prefix_mapping.get(prefix, 'Request')
        categorized[category].append(tag)

    return categorized




