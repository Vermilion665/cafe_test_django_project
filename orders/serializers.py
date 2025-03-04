from rest_framework import serializers
from .models import Item, Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(validated_data)
        for item_data in items_data:
            item, created = Item.objects.get_or_create(item_data)
            order.items.add(item)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])
        instance = super().update(instance, validated_data)
        current_item_ids = {item.id for item in instance.items.all()}
        new_item_ids = {item_data['id'] for item_data in items_data if 'id' in item_data}

        to_add = new_item_ids - current_item_ids
        to_remove = current_item_ids - new_item_ids

        items_to_add = Item.objects.filter(id__in=to_add)
        instance.items.add(items_to_add)
        instance.items.remove(to_remove)

        return instance
        instance.items.clear()
        for item_data in items_data:
            item, created = Item.objects.get_or_create(item_data)
            instance.items.add(item)
        return instance