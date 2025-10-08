from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from teams.models import Team
from .models import Product


def team_products(request, team_slug):
    # Get the team (no authentication required)
    team = get_object_or_404(Team, slug=team_slug)

    data = {"products": []}

    # Get products for this team only
    query = request.GET.get("query")
    if query is None or len(query) == 0:
        products = Product.objects.filter(team=team)
    else:
        products = Product.objects.filter(team=team, title__icontains=query)

    # Handle sorting
    order = ["title", "id"]
    sort = request.GET.get("sort")
    if sort == "price":
        order.insert(0, "price")
    elif sort == "rating":
        order.insert(0, "-stars")
    products = products.order_by(*order)

    # Handle pagination
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

    # Generate output
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
