import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nrityalay.settings')
django.setup()

from store.models import Product

products = [
    {
        "name": "Bharatanatyam Silk Costume Set",
        "category": "Bharatanatyam",
        "price": 8999.00,
        "description": "Traditional pure silk Bharatanatyam costume with temple border, pleated fan, and matching dupatta. Handcrafted by skilled artisans.",
        "stock": 12,
        "image": "https://images.unsplash.com/photo-1610189844779-3711f1c5b6d0?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Kathak Anarkali Dance Dress",
        "category": "Kathak",
        "price": 6499.00,
        "description": "Flowing Anarkali style Kathak costume in vibrant colors with intricate gota patti work, perfect for graceful spins.",
        "stock": 8,
        "image": "https://images.unsplash.com/photo-1583299935545-9c9b4f4d7c5e?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Temple Jewellery Set (Bharatanatyam)",
        "category": "Jewellery",
        "price": 3499.00,
        "description": "Complete antique gold-plated temple jewellery set including necklace, earrings, maang tikka and bangles for classical performances.",
        "stock": 20,
        "image": "https://images.unsplash.com/photo-1611652022419-a9419f74343d?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Ghungroo Anklets (Pair, 100 Bells)",
        "category": "Accessories",
        "price": 1299.00,
        "description": "Premium brass ghungroo anklets with 100 bells per leg, ideal for Kathak, Bharatanatyam and Odissi practice and performance.",
        "stock": 30,
        "image": "https://images.unsplash.com/photo-1631679706909-1844bbd07221?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Odissi Performance Saree",
        "category": "Odissi",
        "price": 7999.00,
        "description": "Authentic Sambalpuri silk saree with traditional Odissi motifs, ideal for stage performances and recitals.",
        "stock": 6,
        "image": "https://images.unsplash.com/photo-1583391733956-6c78276477e2?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Kuchipudi Dance Costume",
        "category": "Kuchipudi",
        "price": 7499.00,
        "description": "Vibrant Kuchipudi dance costume with traditional pleats and temple-style border embroidery, made from breathable silk-cotton blend.",
        "stock": 10,
        "image": "https://images.unsplash.com/photo-1599054802207-595db7e1f12e?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Classical Dance Hair Accessory Set",
        "category": "Accessories",
        "price": 899.00,
        "description": "Set of traditional hair ornaments including jadai billai, sun & moon pins, and fresh-look flower strings for classical dance performances.",
        "stock": 25,
        "image": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=600&q=80",
    },
    {
        "name": "Practice Salwar Set for Dance",
        "category": "Practice Wear",
        "price": 1599.00,
        "description": "Comfortable cotton salwar kameez set designed for daily classical dance practice sessions, breathable and durable.",
        "stock": 18,
        "image": "https://images.unsplash.com/photo-1583391733981-3e6a90c08d44?auto=format&fit=crop&w=600&q=80",
    },
]

for p in products:
    obj, created = Product.objects.update_or_create(name=p["name"], defaults=p)
    print(("Created" if created else "Updated"), obj.name)

print(f"\nTotal products: {Product.objects.count()}")
