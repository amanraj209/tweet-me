from rest_framework import serializers
from django.utils.timesince import timesince

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

import pytz

local_tz = pytz.timezone('Asia/Kolkata')


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


def as_local_time_str(utc_dt):
    return utc_to_local(utc_dt).strftime('%b %d, %Y at %I:%M %p')


class TweetModelSerializer(serializers.ModelSerializer):

    user = UserDisplaySerializer(read_only=True)
    display_date = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['user', 'content', 'timestamp', 'display_date', 'timesince']

    def get_display_date(self, obj):
        return as_local_time_str(obj.timestamp)

    def get_timesince(self, obj):
        return timesince(utc_to_local(obj.timestamp)) + ' ago'
