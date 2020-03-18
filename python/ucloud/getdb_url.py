from ucloud.core import exc
from ucloud.client import Client
import requests 


class Udb:
	def __init__(self,region,project_id,public_key,private_key):
		self.region = region
		self.project_id = project_id
		self.client = Client({
   			"region": self.region,
			"project_id": self.project_id,
			"public_key": public_key,
			"private_key": private_key
	         })

	def get_id(self,offset=0,limit=1,dbid="udbha-eb3sqldt"):
		return self.client.udb().describe_udb_backup({
	        	"ProjectId": self.project_id,
			"Offset": offset,
			"Limit": limit,
			"DBId": dbid
		})

	def down_url(self,id,dbid="udbha-eb3sqldt",zone="cn-bj2-03"):
		return self.client.udb().describe_udb_instance_backup_url({
       			"ProjectId": self.project_id, 
       			"Region": self.region,
       			"BackupId": id,
       			"DBId": dbid,
       			"Zone": "cn-bj2-03" 
		})	


		





