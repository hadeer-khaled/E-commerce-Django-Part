from products.models import Product, ProductImage
from categories.models import Category

def insert_dummy_data():
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert dummy data for smartphones
    product_1, _ = Product.objects.update_or_create(
        product_id=1,
        category=smartphones_category,
        defaults={
            "name": "Google Pixel 6",
            "price": 899,
            "stock": 20,
            "description": "The Google Pixel 6 is here, with an incredible camera and smooth performance.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 1
    ProductImage.objects.update_or_create(
        product=product_1,
        image="cdn.dummyjson.com/product-images/1/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_1,
        image="cdn.dummyjson.com/product-images/1/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_1,
        image="cdn.dummyjson.com/product-images/1/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_1,
        image="cdn.dummyjson.com/product-images/1/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_1,
        image="cdn.dummyjson.com/product-images/1/thumbnail.jpg"
    )

    # Insert dummy data for laptops
    product_2, _ = Product.objects.update_or_create(
        product_id=2,
        category=laptops_category,
        defaults={
            "name": "MacBook Pro 2023",
            "price": 2399,
            "stock": 15,
            "description": "The ultimate MacBook Pro, with unmatched performance and stunning display.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 2
    ProductImage.objects.update_or_create(
        product=product_2,
        image="cdn.dummyjson.com/product-images/2/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_2,
        image="cdn.dummyjson.com/product-images/2/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_2,
        image="cdn.dummyjson.com/product-images/2/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_2,
        image="cdn.dummyjson.com/product-images/2/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_2,
        image="cdn.dummyjson.com/product-images/2/thumbnail.jpg"
    )

    # Insert dummy data for fragrances
    product_3, _ = Product.objects.update_or_create(
        product_id=3,
        category=fragrances_category,
        defaults={
            "name": "Coco Chanel",
            "price": 89,
            "stock": 40,
            "description": "Coco Chanel perfume, a timeless classic for women.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 3
    ProductImage.objects.update_or_create(
        product=product_3,
        image="cdn.dummyjson.com/product-images/3/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_3,
        image="cdn.dummyjson.com/product-images/3/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_3,
        image="cdn.dummyjson.com/product-images/3/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_3,
        image="cdn.dummyjson.com/product-images/3/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_3,
        image="cdn.dummyjson.com/product-images/3/thumbnail.jpg"
    )

    # Add more data
    # Insert dummy data for smartphones
    product_4, _ = Product.objects.update_or_create(
        product_id=4,
        category=smartphones_category,
        defaults={
            "name": "iPhone 13",
            "price": 1099,
            "stock": 25,
            "description": "The latest iPhone with improved performance and battery life.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 4
    ProductImage.objects.update_or_create(
        product=product_4,
        image="cdn.dummyjson.com/product-images/4/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_4,
        image="cdn.dummyjson.com/product-images/4/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_4,
        image="cdn.dummyjson.com/product-images/4/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_4,
        image="cdn.dummyjson.com/product-images/4/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_4,
        image="cdn.dummyjson.com/product-images/4/thumbnail.jpg"
    )

    # Insert dummy data for laptops
    product_5, _ = Product.objects.update_or_create(
        product_id=5,
        category=laptops_category,
        defaults={
            "name": "Dell XPS 15",
            "price": 1799,
            "stock": 18,
            "description": "Dell's flagship laptop with powerful performance and stunning display.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 5
    ProductImage.objects.update_or_create(
        product=product_5,
        image="cdn.dummyjson.com/product-images/5/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_5,
        image="cdn.dummyjson.com/product-images/5/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_5,
        image="cdn.dummyjson.com/product-images/5/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_5,
        image="cdn.dummyjson.com/product-images/5/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_5,
        image="cdn.dummyjson.com/product-images/5/thumbnail.jpg"
    )

    # Insert dummy data for fragrances
    product_6, _ = Product.objects.update_or_create(
        product_id=6,
        category=fragrances_category,
        defaults={
            "name": "Dior Sauvage",
            "price": 79,
            "stock": 30,
            "description": "Dior Sauvage, a bold and woody fragrance for men.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 6
    ProductImage.objects.update_or_create(
        product=product_6,
        image="cdn.dummyjson.com/product-images/6/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_6,
        image="cdn.dummyjson.com/product-images/6/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_6,
        image="cdn.dummyjson.com/product-images/6/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_6,
        image="cdn.dummyjson.com/product-images/6/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_6,
        image="cdn.dummyjson.com/product-images/6/thumbnail.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Google Pixel 6:", product_1.product_id)
    print("MacBook Pro 2023:", product_2.product_id)
    print("Coco Chanel:", product_3.product_id)
    print("iPhone 13:", product_4.product_id)
    print("Dell XPS 15:", product_5.product_id)
    print("Dior Sauvage:", product_6.product_id)

##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for laptops
    product_8, _ = Product.objects.update_or_create(
        product_id=8,
        category=laptops_category,
        defaults={
            "name": "Dell XPS 17",
            "price": 2199,
            "stock": 10,
            "description": "The Dell XPS 17, a powerhouse for professionals with stunning visuals.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 8
    ProductImage.objects.update_or_create(
        product=product_8,
        image="cdn.dummyjson.com/product-images/8/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_8,
        image="cdn.dummyjson.com/product-images/8/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_8,
        image="cdn.dummyjson.com/product-images/8/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_8,
        image="cdn.dummyjson.com/product-images/8/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_8,
        image="cdn.dummyjson.com/product-images/8/thumbnail.jpg"
    )

    # Insert more dummy data for fragrances
    product_9, _ = Product.objects.update_or_create(
        product_id=9,
        category=fragrances_category,
        defaults={
            "name": "Chanel No. 5",
            "price": 129,
            "stock": 25,
            "description": "Chanel No. 5, the iconic fragrance known for its timeless elegance.",
            "avg_rating": 4.9,
        }
    )

    # Insert product images for product 9
    ProductImage.objects.update_or_create(
        product=product_9,
        image="cdn.dummyjson.com/product-images/9/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_9,
        image="cdn.dummyjson.com/product-images/9/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_9,
        image="cdn.dummyjson.com/product-images/9/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_9,
        image="cdn.dummyjson.com/product-images/9/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_9,
        image="cdn.dummyjson.com/product-images/9/thumbnail.jpg"
    )

    # Insert more dummy data for smartphones
    product_10, _ = Product.objects.update_or_create(
        product_id=10,
        category=smartphones_category,
        defaults={
            "name": "iPhone 15",
            "price": 1199,
            "stock": 18,
            "description": "The next generation iPhone with innovative features and performance.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 10
    ProductImage.objects.update_or_create(
        product=product_10,
        image="cdn.dummyjson.com/product-images/10/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_10,
        image="cdn.dummyjson.com/product-images/10/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_10,
        image="cdn.dummyjson.com/product-images/10/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_10,
        image="cdn.dummyjson.com/product-images/10/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_10,
        image="cdn.dummyjson.com/product-images/10/thumbnail.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Dell XPS 17:", product_8.product_id)
    print("Chanel No. 5:", product_9.product_id)
    print("iPhone 15:", product_10.product_id)
##############################################################################################################
  # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for laptops
    product_11, _ = Product.objects.update_or_create(
        product_id=11,
        category=laptops_category,
        defaults={
            "name": "HP Spectre x360",
            "price": 1799,
            "stock": 12,
            "description": "The HP Spectre x360, a convertible laptop with stunning design and performance.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 11
    ProductImage.objects.update_or_create(
        product=product_11,
        image="cdn.dummyjson.com/product-images/11/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_11,
        image="cdn.dummyjson.com/product-images/11/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_11,
        image="cdn.dummyjson.com/product-images/11/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_11,
        image="cdn.dummyjson.com/product-images/11/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_11,
        image="cdn.dummyjson.com/product-images/11/thumbnail.jpg"
    )

    # Insert more dummy data for fragrances
    product_12, _ = Product.objects.update_or_create(
        product_id=12,
        category=fragrances_category,
        defaults={
            "name": "Dolce & Gabbana Light Blue",
            "price": 99,
            "stock": 30,
            "description": "Dolce & Gabbana Light Blue, a fresh and citrusy fragrance for women.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 12
    ProductImage.objects.update_or_create(
        product=product_12,
        image="cdn.dummyjson.com/product-images/12/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_12,
        image="cdn.dummyjson.com/product-images/12/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_12,
        image="cdn.dummyjson.com/product-images/12/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_12,
        image="cdn.dummyjson.com/product-images/12/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_12,
        image="cdn.dummyjson.com/product-images/12/thumbnail.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("HP Spectre x360:", product_11.product_id)
    print("Dolce & Gabbana Light Blue:", product_12.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_13, _ = Product.objects.update_or_create(
        product_id=13,
        category=smartphones_category,
        defaults={
            "name": "Samsung Galaxy S22",
            "price": 1199,
            "stock": 30,
            "description": "The latest Samsung flagship smartphone with cutting-edge features.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 13
    ProductImage.objects.update_or_create(
        product=product_13,
        image="cdn.dummyjson.com/product-images/13/1.jpg"
    )

    # Insert more dummy data for laptops
    product_14, _ = Product.objects.update_or_create(
        product_id=14,
        category=laptops_category,
        defaults={
            "name": "Microsoft Surface Pro 8",
            "price": 1799,
            "stock": 20,
            "description": "The versatile Surface Pro 8 with powerful performance and portability.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 14
    ProductImage.objects.update_or_create(
        product=product_14,
        image="cdn.dummyjson.com/product-images/14/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_15, _ = Product.objects.update_or_create(
        product_id=15,
        category=fragrances_category,
        defaults={
            "name": "Dior Sauvage",
            "price": 99,
            "stock": 35,
            "description": "Dior Sauvage, a captivating fragrance for the modern man.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 15
    ProductImage.objects.update_or_create(
        product=product_15,
        image="cdn.dummyjson.com/product-images/15/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Samsung Galaxy S22:", product_13.product_id)
    print("Microsoft Surface Pro 8:", product_14.product_id)
    print("Dior Sauvage:", product_15.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_16, _ = Product.objects.update_or_create(
        product_id=16,
        category=smartphones_category,
        defaults={
            "name": "OnePlus 10",
            "price": 999,
            "stock": 25,
            "description": "Experience the speed and power of the OnePlus 10.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 16
    ProductImage.objects.update_or_create(
        product=product_16,
        image="cdn.dummyjson.com/product-images/16/1.jpg"
    )

    # Insert more dummy data for laptops
    product_17, _ = Product.objects.update_or_create(
        product_id=17,
        category=laptops_category,
        defaults={
            "name": "HP Spectre x360",
            "price": 1599,
            "stock": 18,
            "description": "Unleash your creativity with the HP Spectre x360 convertible laptop.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 17
    ProductImage.objects.update_or_create(
        product=product_17,
        image="cdn.dummyjson.com/product-images/17/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_18, _ = Product.objects.update_or_create(
        product_id=18,
        category=fragrances_category,
        defaults={
            "name": "Gucci Bloom",
            "price": 129,
            "stock": 30,
            "description": "Gucci Bloom, a fragrance designed to celebrate the authenticity, vitality, and diversity of women.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 18
    ProductImage.objects.update_or_create(
        product=product_18,
        image="cdn.dummyjson.com/product-images/18/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("OnePlus 10:", product_16.product_id)
    print("HP Spectre x360:", product_17.product_id)
    print("Gucci Bloom:", product_18.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_19, _ = Product.objects.update_or_create(
        product_id=19,
        category=smartphones_category,
        defaults={
            "name": "Samsung Galaxy S22",
            "price": 1199,
            "stock": 15,
            "description": "Experience the latest innovation with the Samsung Galaxy S22.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 19
    ProductImage.objects.update_or_create(
        product=product_19,
        image="cdn.dummyjson.com/product-images/19/1.jpg"
    )

    # Insert more dummy data for laptops
    product_20, _ = Product.objects.update_or_create(
        product_id=20,
        category=laptops_category,
        defaults={
            "name": "Dell Inspiron 15",
            "price": 899,
            "stock": 20,
            "description": "Meet your everyday computing needs with the Dell Inspiron 15 laptop.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 20
    ProductImage.objects.update_or_create(
        product=product_20,
        image="cdn.dummyjson.com/product-images/20/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_21, _ = Product.objects.update_or_create(
        product_id=21,
        category=fragrances_category,
        defaults={
            "name": "Chanel No. 5",
            "price": 199,
            "stock": 25,
            "description": "Chanel No. 5, a timeless fragrance that embodies elegance and sophistication.",
            "avg_rating": 4.9,
        }
    )

    # Insert product images for product 21
    ProductImage.objects.update_or_create(
        product=product_21,
        image="cdn.dummyjson.com/product-images/21/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Samsung Galaxy S22:", product_19.product_id)
    print("Dell Inspiron 15:", product_20.product_id)
    print("Chanel No. 5:", product_21.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_22, _ = Product.objects.update_or_create(
        product_id=22,
        category=smartphones_category,
        defaults={
            "name": "iPhone 15",
            "price": 1499,
            "stock": 18,
            "description": "Experience the next evolution of iPhone with the iPhone 15.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 22
    ProductImage.objects.update_or_create(
        product=product_22,
        image="cdn.dummyjson.com/product-images/22/1.jpg"
    )

    # Insert more dummy data for laptops
    product_23, _ = Product.objects.update_or_create(
        product_id=23,
        category=laptops_category,
        defaults={
            "name": "Lenovo ThinkPad X1 Carbon",
            "price": 1899,
            "stock": 12,
            "description": "Unleash your productivity with the Lenovo ThinkPad X1 Carbon.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 23
    ProductImage.objects.update_or_create(
        product=product_23,
        image="cdn.dummyjson.com/product-images/23/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_24, _ = Product.objects.update_or_create(
        product_id=24,
        category=fragrances_category,
        defaults={
            "name": "Dior Sauvage",
            "price": 129,
            "stock": 20,
            "description": "Dior Sauvage, an aromatic fragrance for men that exudes freshness and sensuality.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 24
    ProductImage.objects.update_or_create(
        product=product_24,
        image="cdn.dummyjson.com/product-images/24/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("iPhone 15:", product_22.product_id)
    print("Lenovo ThinkPad X1 Carbon:", product_23.product_id)
    print("Dior Sauvage:", product_24.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_25, _ = Product.objects.update_or_create(
        product_id=25,
        category=smartphones_category,
        defaults={
            "name": "Samsung Galaxy S22 Ultra",
            "price": 1299,
            "stock": 15,
            "description": "Experience the power and innovation with the Samsung Galaxy S22 Ultra.",
            "avg_rating": 4.9,
        }
    )

    # Insert product images for product 25
    ProductImage.objects.update_or_create(
        product=product_25,
        image="cdn.dummyjson.com/product-images/25/1.jpg"
    )

    # Insert more dummy data for laptops
    product_26, _ = Product.objects.update_or_create(
        product_id=26,
        category=laptops_category,
        defaults={
            "name": "Asus ROG Zephyrus G14",
            "price": 1699,
            "stock": 10,
            "description": "Experience unmatched gaming performance with the Asus ROG Zephyrus G14.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 26
    ProductImage.objects.update_or_create(
        product=product_26,
        image="cdn.dummyjson.com/product-images/26/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_27, _ = Product.objects.update_or_create(
        product_id=27,
        category=fragrances_category,
        defaults={
            "name": "Chanel No. 5",
            "price": 199,
            "stock": 25,
            "description": "Chanel No. 5, the iconic fragrance that embodies elegance and sophistication.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 27
    ProductImage.objects.update_or_create(
        product=product_27,
        image="cdn.dummyjson.com/product-images/27/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Samsung Galaxy S22 Ultra:", product_25.product_id)
    print("Asus ROG Zephyrus G14:", product_26.product_id)
    print("Chanel No. 5:", product_27.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_28, _ = Product.objects.update_or_create(
        product_id=28,
        category=smartphones_category,
        defaults={
            "name": "Xiaomi Redmi Note 11 Pro",
            "price": 399,
            "stock": 30,
            "description": "Experience performance and style with the Xiaomi Redmi Note 11 Pro.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 28
    ProductImage.objects.update_or_create(
        product=product_28,
        image="cdn.dummyjson.com/product-images/28/1.jpg"
    )

    # Insert more dummy data for laptops
    product_29, _ = Product.objects.update_or_create(
        product_id=29,
        category=laptops_category,
        defaults={
            "name": "Lenovo Legion 5 Pro",
            "price": 1799,
            "stock": 20,
            "description": "Unleash your gaming potential with the Lenovo Legion 5 Pro.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 29
    ProductImage.objects.update_or_create(
        product=product_29,
        image="cdn.dummyjson.com/product-images/29/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_30, _ = Product.objects.update_or_create(
        product_id=30,
        category=fragrances_category,
        defaults={
            "name": "Dior Sauvage",
            "price": 149,
            "stock": 35,
            "description": "Dior Sauvage, a powerful and fresh fragrance for men.",
            "avg_rating": 4.8,
        }
    )

    # Insert product images for product 30
    ProductImage.objects.update_or_create(
        product=product_30,
        image="cdn.dummyjson.com/product-images/30/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Xiaomi Redmi Note 11 Pro:", product_28.product_id)
    print("Lenovo Legion 5 Pro:", product_29.product_id)
    print("Dior Sauvage:", product_30.product_id)
##############################################################################################################
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert more dummy data for smartphones
    product_31, _ = Product.objects.update_or_create(
        product_id=31,
        category=smartphones_category,
        defaults={
            "name": "Samsung Galaxy S22 Ultra",
            "price": 1299,
            "stock": 25,
            "description": "Experience the ultimate in smartphone technology with the Samsung Galaxy S22 Ultra.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 31
    ProductImage.objects.update_or_create(
        product=product_31,
        image="cdn.dummyjson.com/product-images/31/1.jpg"
    )

    # Insert more dummy data for laptops
    product_32, _ = Product.objects.update_or_create(
        product_id=32,
        category=laptops_category,
        defaults={
            "name": "Asus ROG Zephyrus G14",
            "price": 1499,
            "stock": 15,
            "description": "Dominate the gaming arena with the Asus ROG Zephyrus G14 gaming laptop.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 32
    ProductImage.objects.update_or_create(
        product=product_32,
        image="cdn.dummyjson.com/product-images/32/1.jpg"
    )

    # Insert more dummy data for fragrances
    product_33, _ = Product.objects.update_or_create(
        product_id=33,
        category=fragrances_category,
        defaults={
            "name": "Chanel No. 5",
            "price": 199,
            "stock": 20,
            "description": "Chanel No. 5, the iconic fragrance that epitomizes luxury and elegance.",
            "avg_rating": 4.9,
        }
    )

    # Insert product images for product 33
    ProductImage.objects.update_or_create(
        product=product_33,
        image="cdn.dummyjson.com/product-images/33/1.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Samsung Galaxy S22 Ultra:", product_31.product_id)
    print("Asus ROG Zephyrus G14:", product_32.product_id)
    print("Chanel No. 5:", product_33.product_id)

##############################################################################################################
##############################################################################################################
if __name__ == "__main__":
    insert_dummy_data()
