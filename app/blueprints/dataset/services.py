from typing import Optional

from app.blueprints.dataset.models import DataSet, DSMetaData
from app.blueprints.dataset.repositories import (
    AuthorRepository,
    DSDownloadRecordRepository,
    DSMetaDataRepository,
    DSViewRecordRepository,
    DataSetRepository,
    FMMetaDataRepository,
    FeatureModelRepository,
    FileRepository,
    FileDownloadRecordRepository,
)
from core.services.BaseService import BaseService


class DataSetService(BaseService):
    def __init__(self):
        super().__init__(DataSetRepository())
        self.feature_model_service = FeatureModelService()
        self.author_repository = AuthorRepository()
        self.dsmetadata_repository = DSMetaDataRepository()

    def get_synchronized(self, current_user_id: int) -> DataSet:
        return self.repository.get_synchronized(current_user_id)

    def get_unsynchronized(self, current_user_id: int) -> DataSet:
        return self.repository.get_unsynchronized(current_user_id)

    def latest_synchronized(self):
        return self.repository.latest_synchronized()

    def filter(self, query="", sorting="newest", publication_type="any", tags=[], **kwargs):
        return self.repository.filter(query, sorting, publication_type, tags, **kwargs)

    def count_feature_models(self):
        return self.feature_model_service.count()

    def count_authors(self) -> int:
        return self.author_repository.count()

    def count_dsmetadata(self) -> int:
        return self.dsmetadata_repository.count()


class FeatureModelService(BaseService):
    def __init__(self):
        super().__init__(FeatureModelRepository())


class AuthorService(BaseService):
    def __init__(self):
        super().__init__(AuthorRepository())


class DSDownloadRecordService(BaseService):
    def __init__(self):
        super().__init__(DSDownloadRecordRepository())


class DSMetaDataService(BaseService):
    def __init__(self):
        super().__init__(DSMetaDataRepository())

    def update(self, id, **kwargs):
        return self.repository.update(id, **kwargs)

    def filter_by_doi(self, doi: str) -> Optional[DSMetaData]:
        return self.repository.filter_by_doi(doi)


class DSViewRecordService(BaseService):
    def __init__(self):
        super().__init__(DSViewRecordRepository())


class FMMetaDataService(BaseService):
    def __init__(self):
        super().__init__(FMMetaDataRepository())


class FileService(BaseService):
    def __init__(self):
        super().__init__(FileRepository())


class FileDownloadRecordService(BaseService):
    def __init__(self):
        super().__init__(FileDownloadRecordRepository())
