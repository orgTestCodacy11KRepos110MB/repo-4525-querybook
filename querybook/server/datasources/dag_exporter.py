from app.auth.permission import verify_data_doc_permission
from app.datasource import register
from logic.admin import get_query_engines_by_environment

from logic import (
    datadoc as logic,
)
from logic.datadoc_permission import assert_can_read, assert_can_write

from lib.dag_exporter.export_dag import export_dag
from lib.dag_exporter.all_dag_exporter import ALL_DAG_EXPORTERS


@register("/datadoc/<int:id>/dag_export/", methods=["GET"])
def get_dag_export(id):
    assert_can_read(id)
    verify_data_doc_permission(id)
    return logic.get_dag_export_by_data_doc_id(data_doc_id=id)


@register("/datadoc/<int:id>/dag_export/", methods=["POST", "PUT"])
def create_or_update_dag_export(id, dag, meta):
    assert_can_write(id)
    return logic.create_or_update_dag_export(data_doc_id=id, dag=dag, meta=meta)


@register("/dag_exporter/", methods=["GET"])
def get_dag_exporters(environment_id: int):
    """Return dag exporters which supports the given environment"""
    engines = get_query_engines_by_environment(environment_id)
    engine_ids = [engine.id for engine in engines]

    exporters = []
    for dag_exporter in ALL_DAG_EXPORTERS:
        if not set(engine_ids).isdisjoint(dag_exporter.dag_exporter_engines):
            exporters.append(dag_exporter)

    return exporters


@register("/datadoc/<int:id>/dag_export/export/", methods=["POST"])
def save_and_export_dag(id, exporter_name):
    assert_can_write(id)
    return export_dag(data_doc_id=id, dag_exporter_name=exporter_name)
