from utils.menu import Menu
from utils.amba_product_loader import get_list_of_amba_brain_atlas_products, get_list_of_amba_reference_spaces
from utils.profiler import time_function
from utils.number_formatter import comma_separated_number
from utils.printer import Printer

from constants import DATA_DIR
from services.data.data_retrieval_service import DataRetrievalService
from services.file_save_service import FileSaveService

# cache the list of AMBA brain atlas product names
AMBA_BRAIN_ATLAS_PRODUCT_NAMES = get_list_of_amba_brain_atlas_products()

# Define options for the Data Retrieval Service menu


def retrieve_section_dataset_ids_prompt(reference_space_id: int):
    """
    Retrieve section dataset IDs from a gene with a reference space
    """
    section_dataset_ids = time_function(DataRetrievalService.get_section_dataset_ids_with_reference_space_id)(reference_space_id, delegate=True, should_contain_genes=True)

    if section_dataset_ids is not None:
        Printer.info(f"{comma_separated_number(len(section_dataset_ids))} section dataset IDs found in reference space {reference_space_id}")
    Menu(
        {
            "View Section Dataset IDs": lambda: print(section_dataset_ids),
            "Get Grid Expression Data": lambda: print("Getting grid expression data..."),
            #"Export Section Dataset IDs": lambda: FileSaveService.save_section_dataset_ids_to_file(section_dataset_ids, f"section_dataset_ids_{gene_acronym}_{reference_space_id}.txt"),
        },
        start_message="What would you like to do with the section dataset IDs?",
        stop_on_selection=False,
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
    reference_space_name: lambda reference_space_id=reference_space_id, reference_space_name=reference_space_name: retrieve_section_dataset_ids_prompt(reference_space_id)
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