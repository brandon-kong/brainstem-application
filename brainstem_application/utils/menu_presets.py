import pandas as pd
import numpy as np

from utils.menu import Menu
from utils.amba_product_loader import get_list_of_amba_brain_atlas_products, get_list_of_amba_reference_spaces
from utils.profiler import time_function
from utils.number_formatter import comma_separated_number
from utils.printer import Printer
from utils.input_utils import InputUtility

from models import SectionDataSet

from constants import DATA_DIR, PlaneOfSection
from services.data.data_retrieval_service import DataRetrievalService
from services.file_save_service import FileSaveService

# cache the list of AMBA brain atlas product names
AMBA_BRAIN_ATLAS_PRODUCT_NAMES = get_list_of_amba_brain_atlas_products()

# Define options for the Data Retrieval Service menu


def retrieve_grid_expression_data_for_section_dataset(section_dataset_id: int, included_gene_measurements: list[str]):
    """
    Retrieve grid expression data from a section dataset ID
    """
    return time_function(DataRetrievalService.get_grid_expression_data)(section_dataset_id, include=included_gene_measurements)


def retrieve_grid_expression_data(section_dataset_ids: list[SectionDataSet]):
    """
    Retrieve grid expression data from a section dataset IDs
    """
    included_gene_measurements = InputUtility.get_comma_separated_string_input("Which gene measurements would you like to include? (intensity, density)", valid_values=["intensity", "density"])

    expression_measurements = {}

    length = len(section_dataset_ids)
    curr = 0

    for section_dataset_id in section_dataset_ids:
        if (section_dataset_id.genes is None or len(section_dataset_id.genes) != 1):
            Printer.error(f"No genes found for section dataset ID {section_dataset_id.id}")
            continue
        
        gene = section_dataset_id.genes[0]
        grid_expression_data = retrieve_grid_expression_data_for_section_dataset(section_dataset_id.id, included_gene_measurements)

        for expression_type, data in grid_expression_data.items():
            if expression_type not in expression_measurements:
                expression_measurements[expression_type] = {}

            expression_measurements[expression_type][gene.acronym] = data

        curr += 1
        Printer.info(f"Retrieved grid expression data for {gene.acronym} ({curr}/{length})")
        

    # save the grid expression data to a CSV file, where each column is a gene and each row is a measurement
    for expression_type, data in expression_measurements.items():
        df = pd.DataFrame(data)
        df.to_csv(f"{DATA_DIR}/grid_expression_data_{expression_type}.csv", index=False)
      


def retrieve_section_dataset_ids(reference_space_id: int, is_delegate: bool, plane_of_section: int):
    """
    Retrieve section dataset IDs from a gene with a reference space
    """
    section_dataset_ids: list[SectionDataSet] = time_function(DataRetrievalService.get_section_dataset_ids_with_reference_space_id)(reference_space_id, delegate=is_delegate, should_contain_genes=True, plane_of_section_id=plane_of_section)

    if section_dataset_ids is not None:
        Printer.info(f"{comma_separated_number(len(section_dataset_ids))} section dataset IDs found in reference space {reference_space_id}")
    
        section_dataset_list = [section_dataset.id for section_dataset in section_dataset_ids]
        Menu(
        {
            "View Section Dataset IDs": lambda: print(section_dataset_ids),
            "Get Grid Expression Data": lambda: retrieve_grid_expression_data(section_dataset_ids),
            "Export Section Dataset IDs": lambda: FileSaveService.save_section_dataset_ids_to_file(section_dataset_list, f"section_dataset_ids_reference_{reference_space_id}_{plane_of_section == 1 and "coronal" or "sagittal"}.txt"),
        },
        start_message="What would you like to do with the section dataset IDs?",
        stop_on_selection=False,
    ).run()


def retrieve_section_dataset_ids_prompt(reference_space_id: int):
    """
    Retrieve section dataset IDs from a gene with a reference space
    """
    is_delegate = InputUtility.get_yes_no_input("Should the section dataset be a delegate?")
    
    Menu({
        "Coronal": lambda: retrieve_section_dataset_ids(reference_space_id, is_delegate, PlaneOfSection.CORONAL),
        "Sagittal": lambda: retrieve_section_dataset_ids(reference_space_id, is_delegate, PlaneOfSection.SAGITTAL),
    }, 
    start_message="Which plane of section would you like to retrieve section dataset IDs from?",
    stop_on_selection=True,
    ).run()


def retrieve_geneset_prompt(product_id: int, product_name: str):
    """
    Retrieve a gene set from an AMBA product
    """
    genes = time_function(DataRetrievalService.get_geneset_from_product)(product_id)

    if genes is not None:
        # remove duplicates in genes
        genes = list({gene.acronym: gene for gene in genes}.values())
        Printer.info(f"{comma_separated_number(len(genes))} genes found in {product_name}")

    Menu(
        {
            "View Genes": lambda: print(genes),
            "Export Genes": lambda: FileSaveService.save_geneset_to_file(genes, f"genes_product_{product_id}.txt"),
        },
        start_message="What would you like to do with the gene set?",
        stop_on_selection=False,
    ).run()


AMBA_PRODUCTS_OPTIONS = {
    product_name: lambda product_id=product_id, product_name=product_name: retrieve_geneset_prompt(product_id, product_name) 
    for product_id, product_name in AMBA_BRAIN_ATLAS_PRODUCT_NAMES
}

AMBA_REFERENCE_SPACES_OPTIONS = {
    reference_space_name: lambda reference_space_id=reference_space_id: retrieve_section_dataset_ids_prompt(reference_space_id)
    for reference_space_id, reference_space_name in get_list_of_amba_reference_spaces()
}

DATA_RETRIEVAL_MENU = Menu(
    {
        "Get Gene Set from Product": lambda: Menu(
            options=AMBA_PRODUCTS_OPTIONS,
            start_message="Which AMBA product would you like to retrieve a gene set from?",
            stop_on_selection=True,
            max_page_size=10,
        ).run(),
        "Get Section Dataset IDs from Gene with Reference Space": lambda: Menu(
            options=AMBA_REFERENCE_SPACES_OPTIONS,
            start_message="Which AMBA reference space would you like to retrieve section dataset IDs from?",
            stop_on_selection=True,
            max_page_size=10,
        ).run()
    },
    start_message="What would you like to do with the Data Retrieval Service?",
)