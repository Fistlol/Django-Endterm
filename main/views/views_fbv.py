import json
import logging
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, Category, Sub_category
from main.serializers import ProductSerializer, SubCategorySerializer

logger = logging.getLogger(__name__)


def get_needed_products(request, search_request):
    if request.method == "GET":
        products = Product.objects.filter(Q(name__contains=search_request) | Q(description__contains=search_request))
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def subcat_products(request, id):
    try:
        subcat = Sub_category.objects.get(id=id)
    except Sub_category.DoesNotExist as e:
        logger.warning('Subcategory not found!')
        return JsonResponse({'message:': str(e)}, status=400)
    products = Product.objects.filter(sub_category=subcat)
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


def subcategory_list(request, id):
    try:
        logger.warning('Search Subcategory')
        cat = Category.objects.get(id=id)
    except Sub_category.DoesNotExist as e:
        return JsonResponse({'message:': str(e)}, status=400)
    if request.method == "GET":
        subcategories = Sub_category.objects.filter(category=cat)
        serializer = SubCategorySerializer(subcategories, many=True)
        return JsonResponse(serializer.data, safe=False)


def getSubcategory(request, id):
    subcategory = Sub_category.objects.get(id=id)
    serializer = SubCategorySerializer(subcategory)
    return JsonResponse(serializer.data)
