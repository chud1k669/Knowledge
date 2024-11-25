
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

max_weight_kg = float(input())

max_weight_g = max_weight_kg * 1000


sorted_things = sorted(things.items(), key=lambda x: -x[1])

selected_items = []
current_weight = 0

for item in sorted_things:
    if current_weight + item[1] <= max_weight_g:
        selected_items.append(item[0])
        current_weight += item[1]

print(' '.join(selected_items))