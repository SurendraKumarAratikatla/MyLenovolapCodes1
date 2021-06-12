from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from member.models import Member, Address, SevaCategory, NakshatramType, Organisation, Seva, SevaAddress


class AddressSerializer(serializers.ModelSerializer):
    isPrimary = serializers.BooleanField(source='is_primary')
    isValid = serializers.BooleanField(source='is_valid')

    class Meta:
        model = Address
        fields = (
            'address', 'city', 'country', 'created', 'district', 'id', 'isPrimary', 'isValid', 'phone', 'pin', 'state',
            'updated')


class SevaAddressSerializer(serializers.ModelSerializer):
    isValid = serializers.BooleanField(source='isvalid')

    class Meta:
        model = SevaAddress
        fields = (
            'address', 'city', 'country', 'created', 'district', 'id', 'isValid', 'phone', 'pin', 'sid', 'state',
            'updated')


class SevaCategorySerializer(serializers.ModelSerializer):
    lastSequenceNumber = serializers.CharField(source='last_sequence_number')
    showStartDate = serializers.BooleanField(source='show_start_date')

    class Meta:
        model = SevaCategory
        fields = (
            "id", "code", "amount", "location", "status", "lastSequenceNumber", "name", "created", "updated", "oid",
            "showStartDate", 'recurrence')


class NakshatramSerializer(serializers.ModelSerializer):
    class Meta:
        model = NakshatramType
        fields = ('nakshatram',)


class OrganisationSerilalizer(serializers.ModelSerializer):
    parentId = serializers.CharField(source='parentid')

    class Meta:
        model = Organisation
        fields = (
            "id", "code", "name", "description", "city", "address", "state", "country", "pincode", "email", "phone",
            "mobile", "fax", "website", "parentId", "owner", "status", "uri", "created", "updated")


class SevaSerializer(serializers.ModelSerializer):
    sevaDateStd = serializers.DateField(source='sevadatestd')
    sevaDate = serializers.CharField(source='sevadate')
    sevaDay = serializers.CharField(source='sevaday')
    isLunar = serializers.CharField(source='islunar')
    inTheNameOf = serializers.CharField(source='inthenameof')
    startDate = serializers.DateField(source='startdate')
    endDate = serializers.DateField(source='enddate')
    sevaAddress = SevaAddressSerializer(source='seva_address')
    sevaCategory = SevaCategorySerializer(source='sid')
    organisation = OrganisationSerilalizer(source='oid')

    class Meta:
        model = Seva
        fields = (
            "id", "smid", "ssid", "sevaDateStd", "sevaDate", "sevaDay", "isLunar", "inTheNameOf", "gotram", "occasion",
            "startDate", "endDate", "created", "updated", "sid", "oid", "mid", "sevaAddress", "sevaCategory",
            "organisation"
        )


class MemberSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    birthDate = serializers.CharField(source='birth_date')
    birthYear = serializers.CharField(source='birth_year')

    class Meta:
        model = Member
        fields = (
            'addresses', 'birthDate', 'birthYear', 'created', 'dob', 'email', 'gender', 'gotram', 'id', 'mid',
            'mobile', 'nakshatram', 'name', 'phone', 'photo', 'place', 'salutation', 'search', 'surname', 'updated')


class MemberSevaSerializer(MemberSerializer):
    sevas = SevaSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = (
            'addresses', 'birthDate', 'birthYear', 'created', 'dob', 'email', 'gender', 'gotram', 'id', 'mid',
            'mobile', 'name', 'phone', 'photo', 'place', 'salutation', 'search', 'sevas', 'surname', 'updated')
