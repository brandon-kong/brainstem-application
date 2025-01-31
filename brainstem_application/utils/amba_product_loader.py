import json
from typing import Optional
from pydantic import BaseModel
from constants import BRAINSTEM_APPLICATION_DIR

# Define Pydantic models for any data that is loaded from the database


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


def load_amba_products():
    """
    Load the AMBA products from the database
    """
    # Get the AMBA products from the JSON file

    try:
        with open(
            f"{BRAINSTEM_APPLICATION_DIR}/data/metadata/amba_products.json", "r"
        ) as file:
            data = json.load(file)
            return [AMBAProduct(**product) for product in data]
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while loading the AMBA products: {e}")
        return None


def get_amba_product_by_id(product_id: int):
    """
    Get an AMBA product by its ID
    """
    products = load_amba_products()
    if products is not None:
        for product in products:
            if product.id == product_id:
                return product
    return None


def get_list_of_amba_brain_atlas_product_names():
    """
    Get a list of AMBA product names
    """
    products = load_amba_products()

    # sort the products by ID, and only include products that has "Brain" and "Atlas" in the resource name
    if products is not None:
        products.sort(key=lambda x: x.id)
        return [
            (product.id, product.name)
            for product in products
            if "brain" in product.resource.lower()
            and "atlas" in product.resource.lower()
        ]

    return None
