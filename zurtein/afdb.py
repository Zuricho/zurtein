import requests


def download_afdb(
        uniprot_id: str,
        save_path: str = None
    ):
    """
    Download pdb file from afdb database

    Args:
        uniprot_id: uniprot id of the protein
        save_path: path to save the pdb file
    Returns:
        True if the pdb file is downloaded successfully, False otherwise
    """
    if not save_path:
        save_path = "AF-" + uniprot_id + '-F1-model_v4.pdb'


    url = "https://alphafold.ebi.ac.uk/files/AF-" + uniprot_id + '-F1-model_v4.pdb'

    # download pdb file
    r = requests.get(url, allow_redirects=True)

    # find if it is a PDB
    if r.text[:6] != 'HEADER':
        return False
    else:
        open(save_path, 'wb').write(r.content)
        return True
    

