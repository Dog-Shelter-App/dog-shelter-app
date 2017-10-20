import boto3

AWS_ACCESS_KEY = "AKIAIQ44FUP2X2WWJZ5Q"
AWS_SECRET_ACCESS_KEY = "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"

client = boto3.client(
  'rds',
  aws_access_key_id= AWS_ACCESS_KEY,
  aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
  region_name="us-east-1c"
)

response = client.create_db_cluster(
    AvailabilityZones=[
        'us-east-1c',
    ],
    BackupRetentionPeriod=123,
    CharacterSetName='string',
    DatabaseName='string',
    DBClusterIdentifier='string',
    DBClusterParameterGroupName='string',
    VpcSecurityGroupIds=[
        'string',
    ],
    DBSubnetGroupName='string',
    Engine='string',
    EngineVersion='string',
    Port=123,
    MasterUsername='string',
    MasterUserPassword='string',
    OptionGroupName='string',
    PreferredBackupWindow='string',
    PreferredMaintenanceWindow='string',
    ReplicationSourceIdentifier='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    StorageEncrypted=True|False,
    KmsKeyId='string',
    EnableIAMDatabaseAuthentication=True|False,
    SourceRegion='string'
)
print(RDS_CLIENT)
