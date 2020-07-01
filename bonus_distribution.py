import math


def get_tree_distribution(clients, max_level, percentages):
    """Get the balance distribution in the tree of a user"""
    final_distribution = []
    for client in clients:
        if client['dist_val'] == 0:
            continue
        parents = []
        if client['grouped_parents'] is not None:
            for parent in client['grouped_parents'].split('|'):
                data = parent.split(';')
                parents.append({
                    'parent_id': data[0],
                    'max_level_dist_tree': int(data[1])
                })
        i = 0
        while (i < max_level):
            not_rounded_value = (
                client['dist_val'] * percentages[i]['percentage']
            ) / 100
            comission_parent = math.floor(not_rounded_value * 100)/100.0
            # Si no hay más padres en niveles superiores, todo va al fondo
            # de comisiones no pagadas
            if len(parents) <= i or i >= parents[i]['max_level_dist_tree']:
                final_distribution.append(
                    {
                        'source_id': client['id'],
                        'destiny_id': 0,
                        'amount': comission_parent,
                        'raw_amount': not_rounded_value
                    }
                )
            else:
                final_distribution.append(
                    {
                        'source_id': client['id'],
                        'destiny_id': parents[i]['parent_id'],
                        'amount': comission_parent,
                        'raw_amount': not_rounded_value
                    }
                )
            i += 1
    return final_distribution
