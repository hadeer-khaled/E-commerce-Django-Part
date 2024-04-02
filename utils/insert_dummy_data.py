from products.models import Product, ProductImage
from categories.models import Category

def insert_dummy_data():
    # Create or retrieve categories
    smartphones_category, _ = Category.objects.get_or_create(name="smartphones")
    laptops_category, _ = Category.objects.get_or_create(name="laptops")
    fragrances_category, _ = Category.objects.get_or_create(name="fragrances")

    # Insert dummy data for smartphones
    product_13, _ = Product.objects.update_or_create(
        product_id=13,
        category_id=smartphones_category,
        defaults={
            "name": "Google Pixel 6",
            "price": 899,
            "stock": 20,
            "description": "The Google Pixel 6 is here, with an incredible camera and smooth performance.",
            "avg_rating": 4.5,
        }
    )

    # Insert product images for product 13
    ProductImage.objects.update_or_create(
        product=product_13,
        image="https://cdn.dummyjson.com/product-images/13/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_13,
        image="https://cdn.dummyjson.com/product-images/13/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_13,
        image="https://cdn.dummyjson.com/product-images/13/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_13,
        image="https://cdn.dummyjson.com/product-images/13/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_13,
        image="https://cdn.dummyjson.com/product-images/13/thumbnail.jpg"
    )

    # Insert dummy data for laptops
    product_14, _ = Product.objects.update_or_create(
        product_id=14,
        category_id=laptops_category,
        defaults={
            "name": "MacBook Pro 2023",
            "price": 2399,
            "stock": 15,
            "description": "The ultimate MacBook Pro, with unmatched performance and stunning display.",
            "avg_rating": 4.7,
        }
    )

    # Insert product images for product 14
    ProductImage.objects.update_or_create(
        product=product_14,
        image="https://cdn.dummyjson.com/product-images/14/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_14,
        image="https://cdn.dummyjson.com/product-images/14/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_14,
        image="https://cdn.dummyjson.com/product-images/14/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_14,
        image="https://cdn.dummyjson.com/product-images/14/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_14,
        image="https://cdn.dummyjson.com/product-images/14/thumbnail.jpg"
    )

    # Insert dummy data for fragrances
    product_15, _ = Product.objects.update_or_create(
        product_id=15,
        category_id=fragrances_category,
        defaults={
            "name": "Coco Chanel",
            "price": 89,
            "stock": 40,
            "description": "Coco Chanel perfume, a timeless classic for women.",
            "avg_rating": 4.6,
        }
    )

    # Insert product images for product 15
    ProductImage.objects.update_or_create(
        product=product_15,
        image="https://cdn.dummyjson.com/product-images/15/1.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_15,
        image="https://cdn.dummyjson.com/product-images/15/2.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_15,
        image="https://cdn.dummyjson.com/product-images/15/3.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_15,
        image="https://cdn.dummyjson.com/product-images/15/4.jpg"
    )
    ProductImage.objects.update_or_create(
        product=product_15,
        image="https://cdn.dummyjson.com/product-images/15/thumbnail.jpg"
    )

    # Print IDs of inserted products
    print("Inserted Product IDs:")
    print("Google Pixel 6:", product_13.product_id)
    print("MacBook Pro 2023:", product_14.product_id)
    print("Coco Chanel:", product_15.product_id)

if __name__ == "__main__":
    insert_dummy_data()
