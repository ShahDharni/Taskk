class Brands:
    brand_name1="Amazon"
    brand_name2="Ebay"
    brand_name3="OLX"



class Products(Brands):
    product_name1="Online Ecommerce Store"
    product_name2="Online Store"
    product_name3="Online Store"


obj1=Products()
print(obj1.brand_name1 + " " + "is an " + obj1.product_name1)
print(obj1.brand_name2 + " " + "is an " + obj1.product_name2)
print(obj1.brand_name3 + " " + "is an " + obj1.product_name3)
