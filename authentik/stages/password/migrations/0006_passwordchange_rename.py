# Generated by Django 3.2.5 on 2021-08-21 13:12
from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def rename_default_prompt_stage(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    PromptStage = apps.get_model("authentik_stages_prompt", "PromptStage")
    db_alias = schema_editor.connection.alias

    stages = PromptStage.objects.using(db_alias).filter(name="Change your password")
    if not stages.exists():
        return
    stage = stages.first()
    if PromptStage.objects.using(db_alias).filter(name="default-password-change-prompt").exists():
        return
    stage.name = "default-password-change-prompt"
    stage.save()


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_password", "0005_auto_20210402_2221"),
    ]

    operations = [
        migrations.RunPython(rename_default_prompt_stage),
    ]
