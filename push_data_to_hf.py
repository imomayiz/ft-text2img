from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="data/outfits",
    repo_id="imomayiz/morocco-img",
    repo_type="dataset",
    path_in_repo="data/outfits/"
)