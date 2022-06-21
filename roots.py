import os.path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_SRC = os.path.join(ROOT_DIR, 'src')

ROOT_CONFIG = os.path.join(ROOT_DIR, 'config.json')
ROOT_PERFILES = os.path.join(ROOT_DIR, 'perfiles.json')
ROOT_PUNTAJES = os.path.join(ROOT_DIR, 'puntajes.csv')

ROOT_DATASETS = os.path.join(ROOT_SRC, 'datasets', 'datasets_output')
ROOT_VOLCANS = os.path.join(ROOT_DATASETS, 'dataset_volcanic.csv')
ROOT_LAGOS = os.path.join(ROOT_DATASETS, 'dataset_lagos.csv')
ROOT_FIFA = os.path.join(ROOT_DATASETS, 'dataset_fifa.csv')

if __name__ == '__main__':
    print(ROOT_DIR)
    print(ROOT_DATASETS)
    print(ROOT_VOLCANS)