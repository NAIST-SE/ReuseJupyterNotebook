fake_store_names = {1: 'Albertsons', 2: 'Ahold', 3: 'Food_Lion', 4: 'Hannaford',
                    5: 'Giant', 6: 'Stop_n_Shop', 7: 'Kroger', 8: 'SpartanNash',
                    9: 'SuperValu', 10: 'Walmart'}

fake_items = {1:'Apples', 2:'Bacon', 3:'Bagles', 4:'Beans', 5:'Beer', 6:'Bread',
              7:'Carrots', 8:'Cheese', 9:'Chips', 10:'Coffee', 11:'Cream', 
              12:'Egg', 13:'Fish', 14:'Foil', 15:'Granola Bars', 16:'Grapes',
              17:'Ham', 18:'Honey', 19:'Ice Cream', 20:'Ketchup', 21:'Kielbasa',
              22:'Lemons', 23:'Lettuce', 24:'Margarine', 25:'Mayonnaise', 26:'Milk',
              27:'Mushrooms', 28:'Mustard', 29:'Oranges', 30:'Paper Towles',
              31:'Pasta', 32:'Peanut Butter', 33:'Pears', 34:'Pizza', 35:'Plastic Wrap',
              36:'Potatoes', 37:'Pretzels', 38:'Ribs', 39:'Rice', 40:'Salami', 
              41:'Salsa', 42:'Salt', 43:'Sausage', 44:'Soda', 45:'Soup', 46:'Sugar',
              47:'Tuna', 48:'Turkey', 49:'Waffles', 50:'Yoghurt'}

train['store_name'] = train['store'].replace(fake_store_names)
train['item_name'] = train['item'].replace(fake_items)
