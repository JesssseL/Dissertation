from pydantic import BaseModel

# Request
class ImageRequest(BaseModel):
    query: str

class SelectedProductsRequest(BaseModel):
    query: str
    products: list[ProductWithImage]

# Response
class ProductWithImage(BaseModel):
    productPageToken: str
    name: str
    image: str