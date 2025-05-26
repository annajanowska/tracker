from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    assigned_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='devices')
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active and self.assigned_user:
            Device.objects.filter(assigned_user=self.assigned_user, active=True).exclude(id=self.id).update(active=False, assigned_user=None)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Device {self.id} (Active: {self.active})"


class LocationPing(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='pings')
    latitude = models.FloatField()
    longitude = models.FloatField()
    ping_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ping {self.id} for {self.device.id} at {self.ping_time}"
