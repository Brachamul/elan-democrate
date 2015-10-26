import logging
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import boto
from boto.s3.key import Key

import datetime

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

class Command(BaseCommand):

#	help = 'Envoie la base de donnée sur Amazon Glacier'
	help = 'Envoie la base de donnée sur Amazon S3'


	def add_arguments(self, parser):
		parser.add_argument('--status',
			action='store_true',
			dest='status',
			default=False,
			help='Check status of most recent backup')

	def handle(self, *args, **options):
		bucket = boto.connect_s3(
			aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
			host="s3-eu-west-1.amazonaws.com",
			is_secure=False,
			).get_bucket("elan-democrate-db")
		k = Key(bucket)
		k.key = str(datetime.datetime.now()) + ' ' + settings.DB_NAME
		k.set_contents_from_file(settings.SQLITE3_DB_LOCATION, cb=percent_cb, num_cb=10)
#		if options['status']:
#			retrieve_job = vault.retrieve_archive(archive)
		self.stdout.write("Backup process complete with key {}".format(k.key))


#		def handle(self, *args, **options):
#			vault = boto.connect_glacier(
#				aws_access_key_id=settings.AMAZON_ACCESS_KEY_ID,
#				aws_secret_access_key=settings.AMAZON_SECRET_ACCESS_KEY
#				).create_vault("elan-democrate-database")
#			archive = vault.upload_archive(settings.SQLITE3_DB_LOCATION)
#	#		if options['status']:
#	#			retrieve_job = vault.retrieve_archive(archive)
#			self.stdout.write("Backup process complete with id {}".format(archive))


# https://thomassileo.name/blog/2012/10/24/getting-started-with-boto-and-glacier/

# os.path.dirname(os.path.realpath("__file__")



# Glacier Permissions
#
#	{
#		"Version":"2012-10-17",
#		"Statement": [
#			{
#				"Effect": "Allow",
#				"Resource": "arn:aws:glacier:us-east-1:692147942230:vaults/elan-democrate-*",
#				"Action":["glacier:*"] 
#			}
#		]
#	}



# S3 Permissions
#
#	{
#		"Version":"2012-10-17",
#		"Statement": [
#			{
#				"Effect": "Allow",
#				"Resource": "arn:aws:s3:::elan-democrate-*",
#				"Action":["s3:*"] 
#			}
#		]
#	}


