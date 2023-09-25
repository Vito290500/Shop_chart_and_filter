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

    def check_latest(self, request, query, latest):

        last_filter_applied = ''
        if latest == 'new':
            last_filter_applied = query.order_by('DataItem')
        else:
            last_filter_applied = query
        return last_filter_applied

    def check_filter_price(self, request, query, price_filter):

        additional_filtered_items = ''
        if price_filter == '' or price_filter == '-':
            additional_filtered_items = query.order_by(f'{price_filter}PriceItem')
        else:
            additional_filtered_items = query
        return additional_filtered_items

    def check_filter(self, request, *args):

        list_filter_to_applied = {}
        list_to_check = ['Category', 'Brand', 'Specific Category']

        for x in range(0, len(args)-2):
            if args[x] != list_to_check[x]:
                list_filter_to_applied[list_to_check[x]] = args[x]
            else:
                pass
    
        if len(list_filter_to_applied) > 0:
            return list_filter_to_applied
        else:          
            return list_filter_to_applied
        
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

        #Check all items filter
        if all_item:
            items = ShopItem.objects.all()

            additional_filtered_items = self.check_filter_price(request, items, price_filter)
            final_filter_applied_items = self.check_latest(request, additional_filtered_items, last_updated_filter)

            return render(request, "structure/homepage.html",{
                'items': final_filter_applied_items,
                "category": brand,
                "tag": tag 
            })


        else:
            filter = self.check_filter(request, category_choice, brand_filter, specific_category_filter, price_filter, last_updated_filter)
            #Check with 3 category filter
            if len(filter) == 3:
                items = ShopItem.objects.filter(category__category=category_choice, brand__brand=brand_filter, TagItem=specific_category_filter)

                if items.exists():
                    additional_filter_items = self.check_filter_price(request, items, price_filter)
                    final_filtered_items = self.check_latest(request, additional_filter_items, last_updated_filter)

                    return render(request, "structure/homepage.html",{
                        "items": final_filtered_items,
                        "category": category,
                        "brand": brand,
                        "tag": tag
                    })

                else:
                    items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
                    return render(request, "structure/homepage.html",{
                                'items': items,
                                "category" : category,
                                "brand": brand,
                                "tag": tag,
                                "message": "There is no result."
                                })  
            #Check with 2 category filter  
            elif len(filter) == 2:
                query = Q()

                if 'Brand' in filter and 'Category' in filter:
                    query &= Q(category__category=category_choice, brand__brand=brand_filter)

                if 'Category' in filter and 'Specific Category' in filter:
                    query &= Q(category__category=category_choice, TagItem=specific_category_filter)

                if 'Brand' in filter and 'Specific Category' in filter:
                    query &= Q(brand__brand=brand_filter, TagItem=specific_category_filter)

                filtered_items = ShopItem.objects.filter(query)

                if filtered_items.exists():
                    additional_filtered_items = self.check_filter_price(request, filtered_items, price_filter)
                    final_filtered_items = self.check_latest(request, additional_filtered_items, last_updated_filter)

                    return render(request, "structure/homepage.html",{
                            "items": final_filtered_items,
                            "category": category,
                            "brand": brand,
                            "tag": tag
                        })
                else:
                    items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
                    return render(request, "structure/homepage.html",{
                                'items': items,
                                "category" : category,
                                "brand": brand,
                                "tag": tag,
                                "message": "There is no result."
                                })
            #Check with 1 category filter 
            elif len(filter) == 1:
                query = Q()

                if category_choice != 'Category':
                    query &= Q(category__category=category_choice)

                if brand_filter != 'Brand':
                    query &= Q(brand__brand=brand_filter)

                if specific_category_filter != 'Specific Category':
                    query &= Q(TagItem=specific_category_filter)

                filtered_items = ShopItem.objects.filter(query)

                if filtered_items.exists():
                    additional_filtered_items = self.check_filter_price(request, filtered_items, price_filter)
                    final_filtered_items = self.check_latest(request, additional_filtered_items, last_updated_filter)

                    return render(request, "structure/homepage.html",{
                            "items": final_filtered_items,
                            "category": category,
                            "brand": brand,
                            "tag": tag
                        })
            else:
                items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
                return render(request, "structure/homepage.html",{
                            'items': items,
                            "category" : category,
                            "brand": brand,
                            "tag": tag,
                            "message": "There is no result."
                            })
            
class HomePageSearch(View):
    
    def post(self, request):
        brand = Brand.objects.all()
        category = Category.objects.all()
        all_item = ShopItem.objects.all()
        tag = ShopItem.objects.values_list('TagItem', flat=True).distinct()

        user_input = request.POST['textfield']

        filtered_objects = all_item.filter(NameItem__contains=user_input)
        
        if filtered_objects.exists():
            return render(request, "structure/homepage.html",{
                        'items': filtered_objects,
                        "category" : category,
                        "brand": brand,
                        "tag": tag
                        })  
    

        else:
            list_word = []
            split_text = user_input.split()
            for word in split_text:
                list_word.append(word)

            search_filter1 = all_item.filter(NameItem__contains=list_word[0])
            if search_filter1.exists:
                search_filter2 = search_filter1.filter(NameItem__contains=list_word[1])

                if search_filter2.exists():
                    return render(request, "structure/homepage.html",{
                        'items': search_filter2,
                        "category" : category,
                        "brand": brand,
                        "tag": tag
                        })  

                else:
                    items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
                    return render(request, "structure/homepage.html",{
                                'items': items,
                                "category" : category,
                                "brand": brand,
                                "tag": tag,
                                "message": "There is no result."
                                })
        
            else:
                items = ShopItem.objects.filter(TagItem = "abcdiefghilmnopqrstvuz")
                return render(request, "structure/homepage.html",{
                                'items': items,
                                "category" : category,
                                "brand": brand,
                                "tag": tag,
                                "message": "There is no result."
                                })

class Prefer(View):
    def get(self, request):
        prefer_item = ShopItem.objects.filter(prefer = "yes")
        return render(request, "structure/prefer.html",{
            "items" : prefer_item
        })

    def post(self, request):
        add_to_prefer = request.POST['Add']
        nameitem = request.POST.get('NameItem')
        change_prefer = ShopItem.objects.get(NameItem=nameitem)

        if add_to_prefer == ' ' or add_to_prefer == 'yes':
            print("sono nell'if")
            change_prefer.prefer = "no"
            change_prefer.save()

        else:
            print("sono nell'else")
            change_prefer.prefer = "yes"
            change_prefer.save()


        brand = Brand.objects.all()
        category = Category.objects.all()
        all_item = ShopItem.objects.all()
        tag = ShopItem.objects.values_list('TagItem', flat=True).distinct()

       
        return render(request, "structure/homepage.html",{
                      'items': all_item,
                      "category" : category,
                      "brand": brand,
                      "tag": tag,
                      })


class Chart(View):

    def get(self, request):
        added_to_chart = ShopItem.objects.filter(on_chart = "yes")
        price_session = 0
        for item in added_to_chart:
            price_session += item.PriceItem * item.quantity



        return render(request, "structure/chart.html",{
            "items" : added_to_chart,
            "price" : price_session
            })
    
    def post(self, request):
        
        name_item_to_add = request.POST.get('NameItem')
        remove = request.POST.get('remove')

        if remove == 'yes':
            
            item = ShopItem.objects.get(NameItem = name_item_to_add)
            var = item.quantity
            item.on_chart = "no"
            item.available += item.quantity
            item.quantity -= var
            item.save()

            added_to_chart = ShopItem.objects.filter(on_chart = "yes")

            return render(request, "structure/chart.html",{
                        "items" : added_to_chart,
                        })

        else:
            item = ShopItem.objects.get(NameItem = name_item_to_add)
            item.on_chart = "yes"
            item.available -= 1
            item.quantity += 1
            item.save()

            brand = Brand.objects.all()
            category = Category.objects.all()
            all_item = ShopItem.objects.all()
            tag = ShopItem.objects.values_list('TagItem', flat=True).distinct()

            return render(request, "structure/homepage.html",{
                        'items': all_item,
                        "category" : category,
                        "brand": brand,
                        "tag": tag,
                        "message_add": "Added to Chart!"
                        })








