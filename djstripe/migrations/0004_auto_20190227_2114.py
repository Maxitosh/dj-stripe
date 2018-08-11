# Generated by Django 2.1.4 on 2019-02-27 21:14

from django.db import migrations


class Migration(migrations.Migration):
	def __init__(self, *args, **kwargs):
		try:
			# Hack to support sqlite for quick testing. Without this migrations fail with:
			#    "django.db.utils.NotSupportedError: Renaming the 'djstripe_paymentmethod' table while in a transaction
			#    is not supported on SQLite because it would break referential integrity.
			#    Try adding `atomic = False` to the Migration class."
			from django.db import connection

			if connection.vendor == "sqlite":
				self.atomic = False
		except Exception:
			pass
		super().__init__(*args, **kwargs)

	dependencies = [("djstripe", "0003_auto_20181117_2328")]

	operations = [
		migrations.RenameModel(old_name="PaymentMethod", new_name="DjstripePaymentMethod")
	]