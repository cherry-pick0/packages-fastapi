from fastapi import APIRouter
from fastapi_sqlalchemy import db
from data.models import Package as ModelPackage
from data.schema import Package as SchemaPackage

router = APIRouter()


@router.get("/api/packages", tags=["packages"])
async def get_packages():
    packages = db.session.query(ModelPackage).all()
    return packages


@router.get("/api/packages/{package_id}", response_model=SchemaPackage)
async def get_package(package_id: int):
    package = db.session.query(ModelPackage).get(package_id)
    return package


@router.post('/api/packages', response_model=SchemaPackage)
async def create_package(package: SchemaPackage):
    db_package = ModelPackage(address=package.address, weight=package.weight, recipient_id=package.recipient_id)
    db.session.add(db_package)
    db.session.commit()
    return db_package


@router.delete('/api/packages/{package_id}')
async def delete_package(package_id: int):
    package = db.session.query(ModelPackage).get(package_id)
    db.session.delete(package)
