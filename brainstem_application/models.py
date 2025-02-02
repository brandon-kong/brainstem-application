from pydantic import BaseModel
from typing import Optional

class Gene(BaseModel):
    acronym: str
    alias_tags: Optional[str] = None
    chromosome_id: Optional[int] = None
    ensembl_id: Optional[str] = None
    entrez_id: Optional[int] = None
    genomic_reference_update_id: Optional[int] = None
    homologene_id: Optional[int] = None
    id: int
    legacy_ensembl_gene_id: Optional[str | int] = None
    name: str
    organism_id: int
    original_name: str
    original_symbol: str
    reference_genome_id: Optional[str | int] = None
    sphinx_id: int
    version_status: Optional[str] = None


"""
 "blue_channel": null,
    "delegate": true,
    "expression": true,
    "failed": false,
    "failed_facet": 734881840,
    "green_channel": null,
    "id": 69782969,
    "name": null,
    "plane_of_section_id": 2,
    "qc_date": "2009-05-02T22:48:46Z",
    "red_channel": null,
    "reference_space_id": 10,
    "rnaseq_design_id": null,
    "section_thickness": 25,
    "specimen_id": 69370910,
    "sphinx_id": 33103,
    "storage_directory": "/external/aibssan/production32/prod329/image_series_69782969/",
    "weight": 5470,
"""
class SectionDataSet(BaseModel):
    blue_channel: Optional[str] = None
    delegate: bool
    expression: bool
    failed: bool
    failed_facet: int
    green_channel: Optional[str] = None
    id: int
    name: Optional[str] = None
    plane_of_section_id: int
    qc_date: str
    red_channel: Optional[str] = None
    reference_space_id: int
    rnaseq_design_id: Optional[int] = None
    section_thickness: int
    specimen_id: int
    sphinx_id: int
    storage_directory: Optional[str] = None
    weight: int
    genes: Optional[list[Gene]] = None


class AMBAProduct(BaseModel):
    """
    Represents an AMBA product
    """

    abbreviation: str
    description: Optional[str] = None
    id: int
    name: str
    product_name_facet: int
    resource: Optional[str] = None
    species: Optional[str] = None
    species_name_facet: int
    tags: Optional[str] = None


class AMBAReferenceSpace(BaseModel):
    age_id: int = None
    anatomy_id: str = None
    name: str
    id: int
    organism_id: int
    storage_directory: str