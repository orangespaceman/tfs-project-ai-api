from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import (
    WolfProduct,
    DragonProduct,
    HedgehogProduct,
    ChickenProduct,
    EggProduct,
)


def index(request, model):
    data = {"products": []}

    # handle query param
    query = request.GET.get("query")
    if query is None or len(query) == 0:
        products = model.objects.all()
    else:
        products = model.objects.filter(title__icontains=query)

    # handle sort param
    order = ["title", "id"]
    sort = request.GET.get("sort")
    if sort == "price":
        order.insert(0, "price")
    elif sort == "rating":
        order.insert(0, "-stars")
    products = products.order_by(*order)

    # handle pagination
    page_size = int(request.GET.get("page-size", 10000))
    page_number = int(request.GET.get("page", 1))
    paginated_products = Paginator(products, page_size)
    if (
        page_size > 0
        and page_number > 0
        and page_number <= paginated_products.num_pages
    ):
        products_page = paginated_products.page(page_number)
    else:
        products_page = []

    # generate output
    for product in products_page:
        product_data = {
            "id": product.uuid,
            "title": product.title,
            "description": product.description,
            "image": product.image.url,
            "price": product.price,
            "stars": product.stars,
        }
        data["products"].append(product_data)

    return JsonResponse(data)


def wolf(request):
    model = WolfProduct
    return index(request, model)


def dragon(request):
    model = DragonProduct
    return index(request, model)


def hedgehog(request):
    model = HedgehogProduct
    return index(request, model)


def chicken(request):
    model = ChickenProduct
    return index(request, model)


def egg(request):
    model = EggProduct
    return index(request, model)
