from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock  # mention here which model you want to serialize
        fields = ('ticker','open','close','volume') # if you want to return particular fields in models then we should use like this
        #fields = "__all__()" # if you want to return all fields in models then we should use like this


