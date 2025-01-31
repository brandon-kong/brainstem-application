from utils.menu import Menu
from utils.amba_product_loader import get_list_of_amba_brain_atlas_product_names

from services.data.data_retrieval_service import DataRetrievalService


# cache the list of AMBA brain atlas product names
AMBA_BRAIN_ATLAS_PRODUCT_NAMES = get_list_of_amba_brain_atlas_product_names()

# Define options for the Data Retrieval Service menu

def export_genes(genes: list):
    """
    Export genes to a file
    """
    with open("genes.txt", "w") as file:
        for gene in genes:
            file.write(f"{gene.acronym}\n")

    print("Genes exported to genes.txt")
    


def retrieve_geneset_prompt(product_id: int, product_name: str):
    """
    Retrieve a gene set from an AMBA product
    """
    genes = DataRetrievalService.get_geneset_from_product(product_id)
    if genes is not None:
        print(f"{len(genes)} genes found in {product_name} with ID {product_id}")

    Menu(
        {
            "View Genes": lambda: print(genes),
            "Export Genes": lambda: export_genes(genes),
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