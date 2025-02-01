from utils.menu import Menu
from utils.amba_product_loader import get_list_of_amba_brain_atlas_product_names
from utils.profiler import time_function

from constants import DATA_DIR
from services.data.data_retrieval_service import DataRetrievalService
from services.file_save_service import FileSaveService

# cache the list of AMBA brain atlas product names
AMBA_BRAIN_ATLAS_PRODUCT_NAMES = get_list_of_amba_brain_atlas_product_names()

# Define options for the Data Retrieval Service menu



def retrieve_geneset_prompt(product_id: int, product_name: str):
    """
    Retrieve a gene set from an AMBA product
    """
    genes = time_function(DataRetrievalService.get_geneset_from_product)(product_id)

    if genes is not None:
        print(f"{len(genes)} genes found in {product_name}")

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

DATA_RETRIEVAL_MENU = Menu(
    {
        "Get Gene Set from Product": lambda: Menu(
            options=AMBA_PRODUCTS_OPTIONS,
            start_message="Which AMBA product would you like to retrieve a gene set from?",
            stop_on_selection=True,
        ).run(),
    },
    start_message="What would you like to do with the Data Retrieval Service?",
)