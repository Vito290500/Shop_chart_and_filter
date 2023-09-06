from django.shortcuts import render
from django.views import View
from django.db.models import Q
# Create your views here.

from .models import ShopItem, Category, Brand

class HomePage(View):

    def get(self, request):
        brand = Brand.objects.all()
        category = Category.objects.all()
        all_item = ShopItem.objects.all()
        tag = ShopItem.objects.values_list('TagItem', flat=True).distinct()
        return render(request, "structure/homepage.html",{
                      'items': all_item,
                      "category" : category,
                      "brand": brand,
                      "tag": tag
                      })
    

    def check_filter(self, request, check_filter):
        
        print(check_filter)
        



    def post(self, request):
        
        category_choice = request.POST.get('category-choice')
        brand_filter = request.POST.get('brand-filter')
        specific_category_filter = request.POST.get('specific-category-filter')

        all_item = request.POST.get('all-item')

        price_filter = request.POST.get('price-filter')
        last_updated_filter = request.POST.get('laste-updated-filter')
        
        brand = Brand.objects.all()
        category = Category.objects.all()
        tag = ShopItem.objects.values_list('TagItem', flat=True).distinct()

        check_filter = {
            "category_filter" : {
                "category" : category_choice,
                "brand" : brand_filter,
                "sotto_category": specific_category_filter,
            },
            "price": price_filter,
            "new": last_updated_filter,
            "other" :{
                "brand" : brand,
                "category": category,
                "tag": tag
            }
        }

        if all_item:
            items = ShopItem.objects.all()
            return render(request, "structure/homepage.html",{
                      'items': items,
                      "category" : category,
                      "brand": brand,
                      "tag": tag
                      })

        else:
            self.check_filter(request, check_filter)
        
            items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
            return render(request, "structure/homepage.html",{
                        'items': items,
                        "category" : category,
                        "brand": brand,
                        "tag": tag,
                        "message": "There is no result."
                        })