from django.contrib import admin
from .models import (
    Transaction,
    SellerAccountBalance,
    PaymentWithdrawal,
    PaymentMethod,
    Upi_id,
    Bank,
    Refund_details
)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('overview', 'sender', 'receiver', 'package_name', 'amount', 'service_fee', 'payment_status', 'timestamp', 'payment_id')
    search_fields = ('sender__username', 'receiver__username', 'package_name', 'payment_id')
    list_filter = ('payment_status', 'timestamp')

@admin.register(SellerAccountBalance)
class SellerAccountBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance_amount')
    search_fields = ('user__username',)

@admin.register(PaymentWithdrawal)
class PaymentWithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'withdrawal_method', 'status', 'created_at')
    search_fields = ('user__username', 'withdrawal_method')
    list_filter = ('status', 'withdrawal_method', 'created_at')

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'withdrawal_method')
    search_fields = ('user__username', 'withdrawal_method')

@admin.register(Upi_id)
class UpiIdAdmin(admin.ModelAdmin):
    list_display = ('user', 'upi')
    search_fields = ('user__username', 'upi')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'ifsc_code', 'bank_name')
    search_fields = ('user__username', 'account_number', 'ifsc_code', 'bank_name')

@admin.register(Refund_details)
class RefundDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'status', 'refund_id', 'created_at', 'updated_at')
    search_fields = ('user__username', 'order__id', 'refund_id')
    list_filter = ('status', 'created_at', 'updated_at')
