from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=239)
    employee_code = models.CharField(max_length=50, unique=True, default='EM-000')  # You can set a more dynamic default if needed
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    efp_number = models.CharField(max_length=20, null=True, blank=True)


class Styles(models.Model):
    style_code = models.CharField(max_length=50, unique=True)
    operation = models.CharField(max_length=100)
    mach = models.CharField(max_length=100)
    smv = models.DecimalField(max_digits=5, decimal_places=2)  # SMV can have two decimal places
    target = models.IntegerField()

class Daily_amounts(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    style = models.ForeignKey(Styles, on_delete=models.CASCADE)
    output = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class Daily_report(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user_efficiency = models.DecimalField(max_digits=5, decimal_places=2)


# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     post  = models.CharField(max_length=239)
#     likes = models.ManyToManyField(User, related_name='liked_posts')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     timestamp = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
#     def serialize(self):
#         num_likes= self.likes.count()
#         liked_by = [user.username for user in self.likes.all()]
#         return {
#             "id": self.id,
#             "post": self.post,
#             "image_url": self.image.url if self.image else None,
#             "liked_by": liked_by,
#             "num_likes": num_likes,
#             "username": self.user.username,
#             "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
#         }
    