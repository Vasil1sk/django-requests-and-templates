from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'ramen': {
        'Свинина, г': 200,
        'Вода, мл': 600,
        'Чеснок, зубчик': 2,
        'Корень имбиря, г': 20,
        'Зелёный лук, г': 20,
        'Соль, г': 5,
        'Соевый соус, г': 30,
        'Сахар, г': 10,
        'Пшеничная лапша, г': 200,
        'Куриное яйцо(добавить в готовое блюдо), шт': 1,
    },
}

def home(request):
    return render(request, 'calculator/home.html')

def show_recipe(request, dish_name):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(dish_name)
    multidish = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    context = {
        'recipe': multidish,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)