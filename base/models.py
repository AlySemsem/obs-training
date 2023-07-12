from django.db import models


class Account(models.Model):
    ic01 = models.CharField(max_length=8, null=False, db_column="IC01")
    account_name = models.CharField(max_length=100, null=False, db_column="Account_Name")
    benchmark_date = models.DateTimeField(null=False, db_column="Benchmark_Date")
    profit = models.FloatField(null=False, db_column="Profit")
    created_at = models.DateTimeField(auto_now_add=True, null=False, db_column="Created_At")
    updated_at = models.DateTimeField(auto_now=True, null=False, db_column="Updated_At")

    def __str__(self):
        return self.account_name


class User(models.Model):
    ftid = models.CharField(max_length=8, null=False, db_column="Ftid")
    username = models.CharField(max_length=100, null=False, db_column="Username")
    age = models.IntegerField(null=False, db_column="Age")
    email = models.EmailField(null=False, db_column="Email")
    disclaimer = models.BooleanField(null=False, db_column="Disclaimer")
    created_at = models.DateTimeField(auto_now_add=True, null=False, db_column="Created_At")
    updated_at = models.DateTimeField(auto_now=True, null=False, db_column="Updated_At")

    def __str__(self):
        return self.username


class UsersAccounts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_column="User_ID")
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, db_column="Account_ID")
    created_at = models.DateTimeField(auto_now_add=True, null=False, db_column="Created_At")
    updated_at = models.DateTimeField(auto_now=True, null=False, db_column="Updated_At")

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        account = Account.objects.get(id=self.account_id)
        return "User ID: " + user + ", Account ID: " + account


class AccountData(models.Model):
    financial_impact = models.IntegerField(null=False, db_column="Financial_Imapct")
    year = models.IntegerField(null=False, db_column="Year")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_column="User_ID", related_name="user_id")
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False, db_column="Account_ID")
    updated_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column="Updated_By", related_name="updated_by")
    created_at = models.DateTimeField(auto_now_add=True, null=False, db_column="Created_At")
    updated_at = models.DateTimeField(auto_now=True, null=False, db_column="Updated_At")

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        account = Account.objects.get(id=self.account_id)
        return "User ID: " + user + ", Account ID: " + account

