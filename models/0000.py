import models
import peewee
from playhouse.migrate import *



def forward ():

    # CREATE TABLES
    models.DB.create_tables([models.User])
    models.DB.create_tables([models.Lead])

    # MIGRATE TABLES FROM ONE ITERATION TO A NEW ONE
    migrator = PostgresqlMigrator(models.DB)

    # <variabl_to_input> = ForeignKeyField(
    #     models.Company,
    #     related_name="name",
    #     on_delete="DEFAULT",
    #     to_field=models.Company.id,
    #     null=True
    # )

    # migrate(
    # migrator.add_column('table_name', 'colum_name', <variabl_to_input>)
    # )

if __name__ == '__main__':
  forward()
