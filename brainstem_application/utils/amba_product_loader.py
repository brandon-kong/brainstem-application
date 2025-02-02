import json
from typing import Optional
from pydantic import BaseModel
from constants import BRAINSTEM_APPLICATION_DIR

from models import AMBAProduct, AMBAReferenceSpace


def load_amba_reference_spaces():
    """
    Load the AMBA products from the database
    """
    # Get the AMBA products from the JSON file

    try:
        with open(
            f"{BRAINSTEM_APPLICATION_DIR}/data/metadata/amba_reference_spaces.json", "r"
        ) as file:
            data = json.load(file)
            return [AMBAReferenceSpace(**product) for product in data]
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while loading the AMBA products: {e}")
        return None
    

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


def get_list_of_amba_brain_atlas_products():
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
        ]

    return None

def get_list_of_amba_reference_spaces():
    """
    Get a list of AMBA reference spaces, sorted by Age ID
    """
    reference_spaces = load_amba_reference_spaces()

    if reference_spaces is not None:
        reference_spaces.sort(key=lambda x: x.age_id)
        return [(reference_space.id, reference_space.name) for reference_space in reference_spaces]

    return None