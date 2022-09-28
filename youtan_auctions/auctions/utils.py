import uuid


def get_image_path(instance, filename):
    ext = filename.split(".").pop(-1)
    name = str(uuid.uuid4())
    new_name = f"{name}.{ext}"
    return f"auction_items_images/{new_name}"
